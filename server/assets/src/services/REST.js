import Vue from 'vue'

class REST {
  constructor (url) {
    this.url = (url || 'http://localhost:8000')
    this.reviewAppsUrl = this.url + '/review-apps'
  }

  getReviewApps () {
    return Vue.http.get(this.reviewAppsUrl).then(response => {
      return response.body.results
    })
  }
}

export default new REST()
