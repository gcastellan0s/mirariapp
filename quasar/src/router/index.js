import Vue from 'vue'
import VueRouter from 'vue-router'
import Meta from 'vue-meta'
import globals from '@mirari/variables/globals'
import mirari from '@mirari/router'

Vue.use(VueRouter)
Vue.use(Meta)

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation
 */

var Routes = []
const ROUTES = Routes.concat(
  mirari,
  //SV,
  //CRYE,
)

export default function (/* { store, ssrContext } */) {
  const Router = new VueRouter({
    scrollBehavior: () => ({ y: 0 }),
    routes: ROUTES,
    // Leave these as is and change from quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    mode: process.env.VUE_ROUTER_MODE,
    base: process.env.VUE_ROUTER_BASE
  })

  Router.afterEach(() => {
    // On small screens collapse sidenav
    if (window.layoutHelpers && window.layoutHelpers.isSmallScreen() && !window.layoutHelpers.isCollapsed()) {
      setTimeout(() => window.layoutHelpers.setCollapsed(true, true), 10)
    }
    // Scroll to top of the page
    globals().scrollTop(0, 0)
  })

  Router.beforeEach((to, from, next) => {
    // Set loading state
    document.body.classList.add('app-loading')
    // Add tiny timeout to finish page transition
    setTimeout(() => next(), 10)
  })

  return Router
}
