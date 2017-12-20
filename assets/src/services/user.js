import axios from 'axios'

const IS_DEV = process.env.NODE_ENV === 'development'
console.log('is dev is', IS_DEV)

const http = axios.create({
  baseURL: IS_DEV ? 'http://localhost:8000/' : undefined,  // eslint-disable-line
  // withCredentials: true
})

class UserAPI {
  async authenticate (context) {
    await axios.post(this.url)
  }

  async deauthenticate (context, payload) {
    await axios.post(this.url)
  }

  async getData () {
    await axios.post()
  }

  register (payload) {
    const path = 'rest-auth/registration/'
    console.log('post', payload)
    return http.post(path, payload)
  }
}

export default UserAPI
