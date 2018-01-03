import ProjectsAPI from '../services/projects'

const projectsApi = new ProjectsAPI()

const user = {
  namepspaced: true,
  state: {
    projects: []
  },
  actions: {
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
  mutations: {
    UPDATE_PROJECTS (state, projects) {
      state.projects = projects
    },
    SET_DATA (state, message = {}) {
      state.data = message
    },
    SET_ERROR (state, message = {}) {
      state.error = message
    }
  }
}

export default user
