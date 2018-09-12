import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import Popper from 'popper.js'
import globals from '@/vendor/globals'
import router from './router'
import store from './store'
import App from './App'

window.is_mobile = true

Popper.Defaults.modifiers.computeStyle.gpuAcceleration = false
Vue.config.productionTip = false
Vue.config.devtools = true
Vue.use(BootstrapVue)

import VueCurrencyFilter from 'vue-currency-filter'
Vue.use(VueCurrencyFilter, {
  symbol: '$',
  thousandsSeparator: ',',
  fractionCount: 2,
  fractionSeparator: '.',
  symbolPosition: 'front',
  symbolSpacing: true
})

import Print from 'vue-print-nb'
Vue.use(Print);

Vue.mixin({
  data: globals
})

new Vue({
  components: {
    App
  },
  router,
  store,
  template: '<App/>',
}).$mount('#app')

if (module.hot) {
  module.hot.accept()
}