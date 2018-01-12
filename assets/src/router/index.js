import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/components/Index'
import Welcome from '@/components/Welcome'
import AuthCallback from '@/components/AuthCallback'
import Dashboard from '@/views/Dashboard'
import AddProjectForm from '@/components/AddProjectForm'
import ReleasesView from '@/components/ReleasesView'
import ReleasesViewDefault from '@/components/ReleasesViewDefault'
import CreateReleaseForm from '@/components/CreateReleaseForm'
import Oops from '@/components/Oops'

Vue.use(Router)

export default new Router({
  mode: 'history',
  linkActiveClass: 'is-active',
  linkExactActiveClass: 'is-active',
  routes: [
    {
      path: '/dashboard',
      name: 'dashboard',
      component: Dashboard,
      children: [
        // {
        //   path: '',
        //   name: 'dashboard',
        //   component: Dashboard
        // },
        {
          path: 'add-project',
          name: 'add-project-form',
          component: AddProjectForm
        },
        {
          path: ':slug/releases',
          component: ReleasesView,
          children: [
            {
              path: '',
              name: 'dashboard.releases',
              component: ReleasesViewDefault
            },
            {
              path: 'create-release',
              name: 'dashboard.releases.create-release',
              component: CreateReleaseForm
            }
          ]
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
