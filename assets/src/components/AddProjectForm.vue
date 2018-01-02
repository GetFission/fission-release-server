<template>
  <div class="add-project-form">
    <div class="columns has-text-centered">
      <div class="column is-5 is-offset-4">
        <h3 class="title has-text-grey">New Project Form</h3>
        <p class="subtitle has-text-grey">Give us a little extra information about your project</p>
        <div class="box">
          <div class="field">
            <label class="label">Project name</label>
            <div class="control">
              <input v-model="projectName" class="input" type="text" placeholder="Electron Foo">
            </div>
          </div>
          <div class="field">
            <label class="label">Repository URL (if open source)</label>
            <div class="control">
              <input v-model="rmsUrl" class="input" type="text" placeholder="github.com/zulip/zulip-electron">
            </div>
          </div>
          <div class="control">
            <a @click="addProject" class="button is-link is-block">Add project</a>
          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
import Vue from 'vue'

import ProjectsAPI from '../services/projects'

const projectsAPI = new ProjectsAPI()

export default Vue.component('AddProjectForm', {
  data: function () {
    return {
      projectName: '',
      rmsUrl: ''
    }
  },
  methods: {
    addProject: async function () {
      let isSuccessful = false
      let resp = null

      await projectsAPI.addProject({
        name: this.projectName,
        rms_url: this.rmsUrl
      })
        .then((data) => {
          if (data.status === 201) {
            isSuccessful = true
            resp = data
          }
          resp = data
        })
        .catch((err) => {
          resp = err
        })

      if (isSuccessful) {
        // refresh user projects list (don't add project to users project
        //   in store, instead rely on backend to give us a consistent data set)
        // redirect to project page, project page should fetch data from backend from url param
        this.$router.push(`${resp.data.slug}/releases`)
      } else {
        // show errors to user
        console.log('Error creating project...', resp)
      }
    }
  }
})
</script>

<style lang="scss">
  .add-project-form {
    align-items: center !important;
  }
</style>


