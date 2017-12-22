import axios from 'axios'
// import { getCookie } from '../util'

const IS_DEV = process.env.NODE_ENV === 'development'
console.log('is dev is', IS_DEV)

export const http = axios.create({
  // baseURL: IS_DEV ? 'http://localhost:8000/' : undefined,  // eslint-disable-line
  // withCredentials: true
})

export function getHttp () {
  return http
}

export function setHeader (key, value) {
  http.defaults.headers.common[key] = value
}

export function removeHeader (key) {
  delete http.defaults.headers.common[key]
}
