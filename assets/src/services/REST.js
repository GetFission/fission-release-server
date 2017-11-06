import Vue from 'vue'

class REST {
  constructor (url) {
    const version = 'v1'
    this.url = `/api/${version}/`
    if (process.env.NODE_ENV === 'development') this.url = `http://localhost:8000/api/${version}/`
    this.reviewAppsUrl = this.url + 'review-apps'
    this.collectEmailUrl = this.url + 'getdata/collect-email'
  }

  getBranches (project) {
    return Vue.http.get(`${this.reviewAppsUrl}/${project}/`).then(response => {
      return response.body.results
    })
  }

  collectEmail (email) {
    return Vue.http.post(`${this.collectEmailUrl}/`, { email }).then(response => {
      return response.body
    })
  }
}

export default new REST()
