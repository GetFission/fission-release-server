import auth0 from 'auth0-js'
import router from '../router/index.js'

export default class AuthService {
  authenticated = this.isAuthenticated()

  constructor () {
    this.login = this.login.bind(this)
    this.setSession = this.setSession.bind(this)
    this.logout = this.logout.bind(this)
    this.isAuthenticated = this.isAuthenticated.bind(this)
  }

  // eslint-disable-next-line new-cap
  auth0 = new auth0.WebAuth({
    domain: 'electron-fission.auth0.com',
    clientID: '3noCCWzrdQyu8l2v8yGXuEMHOU5TgLrp',
    redirectUri: 'http://localhost:8080/callback',
    audience: 'https://api.electron-fission.com/v1/',
    responseType: 'token id_token',
    scope: 'openid profile email'
  })

  handleAuthentication () {
    return new Promise((resolve, reject) => {
      this.auth0.parseHash((err, authResult) => {
        if (authResult && authResult.accessToken && authResult.idToken) {
          this.setSession(authResult)
          resolve()
        } else if (err) {
          reject(err)
        }
      })
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
    localStorage.setItem('token_payload', JSON.stringify(authResult.idTokenPayload))
  }

  getTokenPayload () {
    return JSON.parse(localStorage.getItem('token_payload'))
  }

  logout () {
    // Clear access token and ID token from local storage
    localStorage.removeItem('access_token')
    localStorage.removeItem('id_token')
    localStorage.removeItem('expires_at')
    localStorage.removeItem('token_payload')
    this.idTokenPayload = null
    router.push('/')
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
