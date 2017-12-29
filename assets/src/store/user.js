// // eslint-disable import/first
// import { polyfill } from 'es6-promise'
// polyfill()
import UserAPI from '../services/user'
import AuthService from '../services/auth'
import { setHeader, removeHeader } from '../services/http'
import { setToken, removeToken } from '../util/token'

const userAPI = new UserAPI()
const auth = new AuthService()

const store = {}

const user = {
  namepspaced: true,
  state: {
    profile: {},
    token: '',
    data: null,
    machine: null
  },
  actions: {
    async authenticate (context, credentials) {
      auth.login()
    },
    async handleAuthentication (context) {
      await auth.handleAuthentication() // TODO: impl .then & catch
      const payload = auth.getTokenPayload()
      await userAPI.authenticate()
        .then((data) => {
          const profile = data.data
          context.commit('AUTHENTICATE', profile)
        })
        .catch((err) => { console.log('RESP', err) })
    },
    async deauthenticate (context, payload) {
      auth.logout()
      context.commit('DEAUTHENTICATE')
    },
    async load (context) {
      await userAPI.getData()
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
    AUTHENTICATE (state, profile) {
      state.profile = profile
    },
    DEAUTHENTICATE (state) {
      state.profile = {}
    },
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
