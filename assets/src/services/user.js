import { http, setHeader } from './http'

class UserAPI {
  async authenticate () {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/dj/profile/'
    return http.get(path)
  }

  async deauthenticate (context, payload) {
    // await axios.post(this.url)
  }

  async getData () {
    // await axios.post()
  }

  register (payload) {
    const path = '/dj/rest-auth/registration/'
    return http.post(path, payload)
  }
}

export default UserAPI
