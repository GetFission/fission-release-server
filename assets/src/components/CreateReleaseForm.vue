<template>
  <div class="columns">
    <div class="column is-8 is-offset-2">
      <form enctype="multipart/form-data">
        <div class="tile is-ancestor">
          <div class="tile is-parent is-vertical">

            <div class="tile is-child box">
              <p class="title">Basic info</p>
              <div class="field">
                <label class="label">Name</label>
                <div class="control">
                  <input v-model="name" class="input" type="text" placeholder="Speed optimization feature">
                </div>
              </div>
              <div class="field">
                <label class="label">Release version</label>
                <div class="control">
                  <input v-model="version" class="input" type="text" placeholder="5.7.0">
                </div>
              </div>
            </div>

            <div class="tile is-child box">
              <p class="title">Select audience</p>
              <p>Coming soon..</p>
            </div>

            <div class="tile is-child box">
              <p class="title">Upload artifacts</p>

              <br>
              <p class="subtitle">OSX</p>
              <div class="file has-name is-fullwidth">
                <label class="file-label">
                  <input class="file-input" type="file" name="darwin_artifact" @change="darwinFileName = $event.target.files[0].name">
                  <span class="file-cta">
                    <span class="file-icon">
                      <i class="fa fa-upload"></i>
                    </span>
                    <span class="file-label">
                      Choose a file…
                    </span>
                  </span>
                  <span class="file-name">
                    {{ darwinFileName }}
                  </span>
                </label>
              </div>

              <br>
              <p class="subtitle">Windows</p>
              <div class="file has-name is-fullwidth">
                <label class="file-label">
                  <input class="file-input" type="file" name="windows_artifact" @change="windowsFileName = $event.target.files[0].name">
                  <span class="file-cta">
                    <span class="file-icon">
                      <i class="fa fa-upload"></i>
                    </span>
                    <span class="file-label">
                      Choose a file…
                    </span>
                  </span>
                  <span class="file-name">
                    {{ windowsFileName }}
                  </span>
                </label>
              </div>
            </div>
          </div>
        </div>
        <div v-if="isUploading" class="modal is-active">
          <div class="modal-background"></div>
          <div class="modal-content">
            <!-- Any other Bulma elements you want -->
            <div class="card has-text-centered">
              <header class="card-header">
                <p class="card-header-title is-centered">Creating release</p>
              </header>
              <div class="card-content">
                <div class="content">
                  Uploading artifacts...
                  <div class="spinner">
                    <img src="../../static/loading.svg" alt="loading" />
                  </div>
                  Page will automatically redirect when upload completes, do not navigate away.
                </div>
              </div>
            </div>
          </div>
          <!-- <button class="modal-close is-large" aria-label="close"></button> -->
        </div>
        <button @click="submit" class="button is-info is-right">Create release</button>
      </form>
    </div>
  </div>

</template>



<script>
import Vue from 'vue'

import ReleasesAPI from '../services/releases'

const releaseAPI = new ReleasesAPI()

export default Vue.component('CreateReleaseForm', {
  data: function () {
    return {
      name: '',
      version: '',
      windows_artifact: null,
      windowsFileName: 'MyExampleApp-win-5.7.0.zip',
      darwin_artifact: null,
      darwinFileName: 'MyExampleApp-osx-5.7.0.zip',
      isUploading: false
    }
  },
  methods: {
    submit (event) {
      event.preventDefault()

      const formData = new FormData()

      formData.append('project_slug', this.$route.params.slug)

      // Get files
      this.$el.querySelectorAll('input[type="file"]').forEach(element => {
        if (element.files[0]) {
          formData.append(element.name, element.files[0])
        }
      })

      // populate remaining input fields
      const formFields = ['name', 'version']
      formFields.forEach(fieldName => {
        formData.append(fieldName, this[fieldName])
      })

      // Display the key/value pairs
      for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1])
      }

      // POST data....
      this.isUploading = true
      const that = this
      releaseAPI.createRelease(formData)
        .then((data) => {
          that.isUploading = false
          this.$router.push({name: 'dashboard.releases', params: {slug: this.$route.params.slug}})
        })
        .catch((err) => {
          that.isUploading = false
          console.log('error', err)
        })
    }
  }
})
</script>

<style lang="scss" scoped>
  div.columns {
    margin-top: 1rem;
  }
</style>
