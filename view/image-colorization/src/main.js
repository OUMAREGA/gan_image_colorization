import Vue from 'vue'
import App from './App.vue'

import axios from 'axios'
import VueAxios from 'vue-axios'

import { BootstrapVue } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)

import AOS from 'aos'
import 'aos/dist/aos.css'

import router from '../router'

Vue.use(VueAxios, axios)


import 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  mounted() {
    AOS.init()
  },
}).$mount('#app')
