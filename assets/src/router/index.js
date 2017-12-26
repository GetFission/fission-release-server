import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Welcome from '@/components/Welcome'
import SignUp from '@/components/SignUp'
import Login from '@/components/Login'
import Dashboard from '@/views/Dashboard'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/sign-up',
      name: 'signup',
      component: SignUp
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/d',
      name: 'dashboard',
      component: Dashboard,
      children: []
    },
    {
      path: '/',
      name: 'Welcome',
      component: Welcome
    },
    {
      path: '/review-apps/:project',
      name: 'Index',
      component: Index
    }
  ]
})
