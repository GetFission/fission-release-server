// // eslint-disable import/first
// import { polyfill } from 'es6-promise'
// polyfill()
import ProjectsAPI from '../services/user'

const projectsApi = new ProjectsAPI()

const user = {
  namepspaced: true,
  state: {
    projects: {},
  },
  actions: {
    async ADD_PROJECT (context, payload) {
      await projectsApi.addProject(payload)
        .then((data) => {
          console.log('new project added...')
        })
        .catch((err) => {
          console.log('failed to create project')
        })
    },
  },
  getters: {
    // TODO: properly implement these
    // GET_STATE: state => store.state,
    // GET_ERRORS: state => store.errors
  },
  mutations: {
    ADD_PROJECT (state, profile) {
      // TODO: Do I really need to add this to the state?
      state.profile = profile
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
