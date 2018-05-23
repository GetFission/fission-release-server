<template>
  <div>
    <div class="field">
      <label class="label">OSX %</label>
      <div class="control rollout-input">
        <input class="input" type="text" placeholder="100">
      </div>
    </div>
    <div class="field">
      <label class="label">Windows %</label>
      <div class="control rollout-input">
        <input class="input" type="text" placeholder="100">
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue'

  // import ProjectsAPI from '../services/projects'
  // const projectsAPI = new ProjectsAPI()

  export default Vue.component('ReleaseAudienceForm', {
    data: function () {
      return {
      }
    }
  })
</script>

<style>
</style>
