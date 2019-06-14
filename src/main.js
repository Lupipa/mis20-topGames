import Vue from 'vue'
import BootstrapVue from "bootstrap-vue"
import App from './App.vue'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap-vue/dist/bootstrap-vue.css"

import VueRouter from 'vue-router'
import WelcomePage from './components/welcomePage.vue'
import HomePage from './components/home.vue'

Vue.use(BootstrapVue)
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/', name: 'Welcome', component:   WelcomePage },
    { path: '/home', name: 'home', component: HomePage }
  ]
})

new Vue({
  el: '#app',
  router,
  render: h => h(App)
})