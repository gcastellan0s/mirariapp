import Vue from 'vue'
import Router from 'vue-router'
import Meta from 'vue-meta'
import globals from '@/vendor/globals'

import mirari from '@/app/mirari/router'
import SV from '@/app/SV/router'
import CRYE from '@/app/CRYE/router'

Vue.use(Router)
Vue.use(Meta)

var Routes = []

const ROUTES = Routes.concat(
  mirari,
  SV,
  CRYE,
)

const router = new Router({
  mode: 'history',
  //saveScrollPosition: true,
  routes: ROUTES
})

router.afterEach(() => {
  if (window.layoutHelpers && window.layoutHelpers.isSmallScreen() && !window.layoutHelpers.isCollapsed()) {
    setTimeout(() => window.layoutHelpers.setCollapsed(true, true), 10)
  }
  globals().scrollTop(0, 0)
})

router.beforeEach((to, from, next) => {
  document.body.classList.add('app-loading')
  setTimeout(() => next(), 10)
})

export default router