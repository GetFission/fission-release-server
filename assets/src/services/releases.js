import { http, setHeader } from './http'

class ReleasesAPI {
  async createRelease (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/v1/releases/create/'
    return http.post(path, data)
  }

  async getReleases (data) {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/v1/releases/list/'
    return http.get(path)
  }
}

export default ReleasesAPI
