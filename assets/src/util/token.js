import store from 'store'

export function getToken () {
  return store.get('token')
}

export function setToken (token) {
  store.set('token', token)
}

export function removeToken () {
  store.remove('token')
}
