import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

import user from './user'
import projects from './projects'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {},
  mutations: {},
  actions: {},
  modules: {
    user,
    projects
  },
  plugins: [createPersistedState()]
})

export default store
