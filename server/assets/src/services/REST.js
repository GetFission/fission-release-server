import Vue from 'vue'

class REST {
  constructor (url) {
    this.url = '/api/v1'
    if (process.env.NODE_ENV === 'development') this.url = 'http://localhost:8000/api/v1'
    this.reviewAppsUrl = this.url + '/review-apps'
  }

  getReviewApps () {
    return Vue.http.get(this.reviewAppsUrl).then(response => {
      return response.body.results
    })
  }
}

export default new REST()
