import { http, setHeader } from './http'

class ReleasesAPI {
  async createRelease (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/v1/releases/create/'
    return http.post(path, data)
  }

  async deleteRelease (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/v1/releases/delete/'
    return http.post(path, data)
  }

  async getReleases (projectSlug) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = `/api/v1/releases/list/${projectSlug}/`
    return http.get(path)
  }
}

export default ReleasesAPI
