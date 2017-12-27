import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Welcome from '@/components/Welcome'
import AuthCallback from '@/components/AuthCallback'
// import SignUp from '@/components/SignUp'
// import Login from '@/components/Login'
import Dashboard from '@/views/Dashboard'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/d',
      name: 'dashboard',
      component: Dashboard,
      children: []
    },
    {
      path: '/callback',
      name: 'Callback',
      component: AuthCallback
    },
    {
      path: '/review-apps/:project',
      name: 'Index',
      component: Index
    },
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    }
  ]
})
