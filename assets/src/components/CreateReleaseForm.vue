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
                  <input v-model="release_version" class="input" type="text" placeholder="5.7.0">
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
        <button @click="submit" class="button is-info is-right">Create release</button>
      </form>
    </div>
  </div>

</template>



<script>
import Vue from 'vue'

export default Vue.component('CreateReleaseForm', {
  data: function () {
    return {
      name: '',
      release_version: '',
      windows_artifact: null,
      windowsFileName: 'MyExampleApp-win-5.7.0.zip',
      darwin_artifact: null,
      darwinFileName: 'MyExampleApp-osx-5.7.0.zip'
    }
  },
  methods: {
    submit (event) {
      event.preventDefault()

      const formData = new FormData()

      this.$el.querySelectorAll('input[type="file"]').forEach(element => {
        formData.append(element.name, element.files[0])
      })

      // populate remaining input fields
      const formFields = ['name', 'release_version']
      formFields.forEach(fieldName => {
        formData.append(fieldName, this[fieldName])
      })

      // Display the key/value pairs
      for (var pair of formData.entries()) {
        console.log(pair[0] + ', ' + pair[1])
      }

      // POST data....
      // redirect to release detail page.. (where you can activate, pause, delete...)
    }
  }
})
</script>

<style lang="scss" scoped>
  div.columns {
    margin-top: 1rem;
  }

  // .section {
  //   background: white;
  // }
</style>
