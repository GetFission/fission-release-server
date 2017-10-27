import Vue from 'vue'

class REST {
  constructor (url) {
    this.url = ''
    if (process.env.NODE_ENV === 'development') this.url = 'http://localhost:8000'
    this.reviewAppsUrl = this.url + '/review-apps'
  }

  getReviewApps () {
    return Vue.http.get(this.reviewAppsUrl).then(response => {
      return response.body.results
    })
  }
}

export default new REST()
