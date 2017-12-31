import { http, setHeader } from './http'

class ProjectsAPI {
  async addProject (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/project/create/'
    return http.post(path, data)
  }
}

export default ProjectsAPI
