// eslint-disable import/first
import { polyfill } from 'es6-promise'
polyfill()
import UserAPI from '../services/user'
import { setHeader, removeHeader } from '../services/http'
import { setToken, removeToken } from '../util/token'

const userAPI = new UserAPI()

const store = {}

const user = {
  namepspaced: true,
  state: {
    token: '',
    data: null,
    error: {email: [], password1: [], password2: []},
    machine: null
  },
  actions: {
    async authenticate (context, credentials) {
      await userAPI.authenticate(credentials)
        .then((data) => {
          console.log('got token', data.data.key)
          context.commit('SET_TOKEN', data.data.key)
        })
        .catch((err) => {
          // TODO: check types of errors possible here...
          console.log('fail...', err)
          context.commit('SET_ERROR', err.response.data)
        })

      // // request (load) user data after authenticating
      // if (context.getters.GET_STATE !== 'handling') {
      //   await context.dispatch('load')
      // }
    },
    async deauthenticate (context, payload) {
      // TODO: implement
      await userAPI.deauthenticate(context, payload)
    },
    async load (context) {
      // await REST.getData()
      // write mutation to set data on success
      await userAPI.getData()
    },
    async register (context, payload) {
      console.log('action to register', payload)
      await userAPI.register(payload)
        .then((data) => {
          context.commit('SET_DATA', data)
        })
        .catch((err) => {
          // TODO: check types of errors possible here...
          context.commit('SET_ERROR', err.response.data)
        })
    },
    async restore (context, token) {
      // restore token from local storage
      if (token) {
        context.commit('SET_TOKEN', {auth_token: token})
        await context.dispatch('load')
      }
    }
  },
  getters: {
    // TODO: properly implement these
    GET_STATE: state => store.state,
    GET_ERRORS: state => store.errors
  },
  mutations: {
    /* eslint-disable */
    SET_TOKEN (state, { auth_token }) {
      state.token = auth_token
      setToken(auth_token)
      setHeader('Authorization', `Token ${auth_token}`)
    },
    /* eslint-enable */
    REMOVE_TOKEN (state) {
      state.token = ''
      removeToken()
      removeHeader('Authorization')
    },
    SET_DATA (state, message = {}) {
      state.data = message
    },
    SET_ERROR (state, message = {}) {
      state.error = message
    },
    SET_STATE (state, action) {
      // TODO: revisit use of statemachine to indicate UI loading
      // state.machine.do(action)
    }
  }
}

export default user
