<template>
  <div class="add-project-form">
    <!-- <div class="hero">
      <div class="hero-body"> -->
        <!-- <div class="container has-text-centered"> -->
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
                    <input v-model="rms_url" class="input" type="text" placeholder="github.com/zulip/zulip-electron">
                  </div>
                </div>
                <div class="control">
                  <a @click="addProject" class="button is-link is-block">Add project</a>
                </div>
              </div>
            </div>
          </div>
        <!-- </div> -->
      <!-- </div>
    </div> -->
  </div>
</template>


<script>
import Vue from 'vue'

export default Vue.component('AddProjectForm', {
  data: function () {
    return {
      projectName: ''

    }
  },
  mounted () {
    console.log('got here..')
  }
})
</script>

<style lang="scss">
  .add-project-form {
    align-items: center !important;
  }
</style>


