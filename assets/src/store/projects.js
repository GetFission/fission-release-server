// // eslint-disable import/first
// import { polyfill } from 'es6-promise'
// polyfill()
import ProjectsAPI from '../services/projects'

const projectsApi = new ProjectsAPI()

const user = {
  namepspaced: true,
  state: {
    projects: []
  },
  actions: {
    // async ADD_PROJECT (context, payload) {
    //   await projectsApi.addProject(payload)
    //     .then((data) => {
    //       console.log('new project added...')
    //     })
    //     .catch((err) => {
    //       console.log('failed to create project')
    //     })
    // },
    async LOAD_PROJECTS ({ commit }) {
      await projectsApi.loadProjects()
        .then((data) => {
          if (data.status === 200) {
            commit('UPDATE_PROJECTS', data.data.results)
          }
        })
        .catch((err) => {
          console.log('Error loading projects', err)
        })
    }
  },
  getters: {
    // TODO: properly implement these
    // GET_STATE: state => store.state,
    // GET_ERRORS: state => store.errors
  },
  mutations: {
    UPDATE_PROJECTS (state, projects) {
      state.projects = projects
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
