import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Welcome from '@/components/Welcome'
import AuthCallback from '@/components/AuthCallback'
import Dashboard from '@/views/Dashboard'
import AddProjectForm from '@/components/AddProjectForm'
import Oops from '@/components/Oops'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      children: [
        // {
        //   path: '/',
        //   name: 'dashboard',
        //   component: Dashboard
        // },
        {
          path: 'add-project',
          name: 'AddProjectForm',
          component: AddProjectForm
        }
      ]
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
    },
    {
      path: '*',
      name: 'Oops',
      component: Oops
    }
  ]
})
