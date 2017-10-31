import Vue from 'vue'

class REST {
  constructor (url) {
    const version = 'v1'
    this.url = `/api/${version}/`
    if (process.env.NODE_ENV === 'development') this.url = `http://localhost:8000/api/${version}/`
    this.reviewAppsUrl = this.url + 'review-apps'
  }

  getReviewApps (project) {
    return Vue.http.get(`${this.reviewAppsUrl}/${project}/`).then(response => {
      return response.body.results
    })
  }
}

export default new REST()
