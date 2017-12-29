import { http, setHeader } from './http'

class UserAPI {
  async authenticate () {
    setHeader('Authorization', `Bearer ${localStorage.getItem('id_token')}`)
    const path = '/api/profile/'
    return http.get(path)
  }

  async deauthenticate (context, payload) {
    // await axios.post(this.url)
  }

  async getData () {
    // await axios.post()
  }
}

export default UserAPI
