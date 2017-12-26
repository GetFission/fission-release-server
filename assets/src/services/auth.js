import auth0 from 'auth0-js'
import router from '../router/index.js'
// import { EventBus } from './EventBus.js'

export default class AuthService {
  authenticated = this.isAuthenticated()
  // authNotifier = EventBus

  constructor () {
    this.login = this.login.bind(this)
    this.setSession = this.setSession.bind(this)
    this.logout = this.logout.bind(this)
    this.isAuthenticated = this.isAuthenticated.bind(this)
  }

  // eslint-disable-next-line new-cap
  auth0 = new auth0.WebAuth({
    domain: 'electronfission.auth0.com',
    clientID: 'WjvVSgMgFT4FaetHIYabzuny1DLplb5n',
    redirectUri: 'http://localhost:8080/callback',
    audience: 'https://electronfission.auth0.com/userinfo',
    responseType: 'token id_token',
    scope: 'openid'
  })

  handleAuthentication () {
    this.auth0.parseHash((err, authResult) => {
      if (authResult && authResult.accessToken && authResult.idToken) {
        this.setSession(authResult)
        router.replace('Index')
      } else if (err) {
        router.replace('/')
        console.log(err)
      }
    })
  }

  setSession (authResult) {
    // Set the time that the access token will expire at
    let expiresAt = JSON.stringify(
      authResult.expiresIn * 1000 + new Date().getTime()
    )
    localStorage.setItem('access_token', authResult.accessToken)
    localStorage.setItem('id_token', authResult.idToken)
    localStorage.setItem('expires_at', expiresAt)

    // TODO: use store...
    this.authNotifier.$emit('authChange', { authenticated: true })

  }

  logout () {
    // Clear access token and ID token from local storage
    localStorage.removeItem('access_token')
    localStorage.removeItem('id_token')
    localStorage.removeItem('expires_at')
    this.userProfile = null

    // TODO: use store
    this.authNotifier.$emit('authChange', false)
    // navigate to the home route
    router.replace('/')
  }

  isAuthenticated () {
    // Check whether the current time is past the access token's expiry time
    let expiresAt = JSON.parse(localStorage.getItem('expires_at'))
    return new Date().getTime() < expiresAt
  }

  login () {
    this.auth0.authorize()
  }
}
