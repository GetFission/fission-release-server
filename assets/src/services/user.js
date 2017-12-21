import { getCookie } from '../util'
import { http, setHeader } from './http'

class UserAPI {
  async authenticate (payload) {
    setHeader('X-CSRFToken', getCookie('csrftoken'))
    const path = '/dj/rest-auth/login/'
    return http.post(path, payload)
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
