import axios from 'axios'
import { getCookie, setHeader } from '../util'

const IS_DEV = process.env.NODE_ENV === 'development'
console.log('is dev is', IS_DEV)

const http = axios.create({
  // baseURL: IS_DEV ? 'http://localhost:8000/' : undefined,  // eslint-disable-line
  // withCredentials: true
})

class UserAPI {
  async authenticate (payload) {
    setHeader(http, 'X-CSRFToken', getCookie('csrftoken'))
    const path = '/dj/rest-auth/login/'
    console.log('login payload', payload)
    return http.post(path, payload)
  }

  async deauthenticate (context, payload) {
    await axios.post(this.url)
  }

  async getData () {
    await axios.post()
  }

  register (payload) {
    const path = '/dj/rest-auth/registration/'
    return http.post(path, payload)
  }
}

export default UserAPI
