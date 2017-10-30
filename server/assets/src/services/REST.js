import Vue from 'vue'

class REST {
  constructor (url) {
    const version = 'v1'
    this.url = (url || 'http://localhost:8000')
    this.reviewAppsUrl = this.url + `/api/${version}/review-apps`
  }

  getReviewApps (project) {
    return Vue.http.get(`${this.reviewAppsUrl}/${project}/`).then(response => {
      return response.body.results
    })
  }
}

export default new REST()
