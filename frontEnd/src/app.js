import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import routerConfig from './router'
import app from './main'
var common = require('commonFunc')
import $ from 'jquery'

// Router
Vue.use(VueRouter)

const router = new VueRouter({
  history: true,
  hashbang: false,
})
routerConfig(router)

// Resource
Vue.use(VueResource)

Vue.http.options.root = '/root'
Vue.http.headers.common['Content-Type'] = 'application/json'

Vue.http.interceptors.push((request, next) => {
  $('.btn').addClass('disabled')
  var token = common.getStoreData('token')
  if (typeof (token) === 'string') {
    Vue.http.headers.common['authorization'] = token
  }

  // continue to next interceptor
  next((response) => {
    $('.btn').removeClass('disabled')
    if (response.status === 401) {
      router.go({ path: '/error401', replace: true })
    }
  })
})

router.start(app, '#app')

window.router = router
