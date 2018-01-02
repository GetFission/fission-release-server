import { http, setHeader } from './http'

class ProjectsAPI {
  async addProject (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/v1/projects/create/'
    return http.post(path, data)
  }

  async loadProjects (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/v1/projects/list/'
    return http.get(path)
  }
}

export default ProjectsAPI
