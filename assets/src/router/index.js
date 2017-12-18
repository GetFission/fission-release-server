import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Welcome from '@/components/Welcome'
import SignUp from '@/components/SignUp'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/sign-up',
      name: 'signup',
      component: SignUp
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
