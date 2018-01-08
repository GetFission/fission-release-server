<template>
  <section class="info-tiles">
    <div class="tile is-ancestor has-text-centered">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="title">0</p>
          <p class="subtitle">Total releases</p>
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="title">0</p>
          <p class="subtitle">Active releases</p>
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child box">
          <router-link class="button is-large is-info" tag="button" :to="{name: 'dashboard.releases.create-release', params: {slug: project.slug}}">
            <i class="fa fa-plus" aria-hidden="true"></i>&nbsp;&nbsp;Create new release</router-link>
        </article>
      </div>
    </div>
    <table class="table is-striped is-fullwidth is-hoverable">
      <tbody>
        <tr>
          <th>Name</th>
          <th>Version</th>
          <th>Created</th>
          <th>Released</th>
          <th>Status</th>
          <th></th>
        </tr>
        <tr v-for="release in releases" :key="release.id">
          <td>{{ release.name }}</td>
          <td>{{ release.version }}</td>
          <td>{{ release.created }}</td>
          <td>N/A</td>
          <td>{{ release.status }}</td>
          <td><button class="button is-info">manage</button></td>
        </tr>
      </tbody>
    </table>
  </section>

</template>

<script>
import Vue from 'vue'

export default Vue.component('ReleasesViewDefault', {
  data: function () {
    return {
      releases: [
        {id: 1, name: 'alpha', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'},
        {id: 2, name: 'beta', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'},
        {id: 3, name: 'gamma', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'},
        {id: 4, name: 'sigma', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'}
      ]
    }
  },
  computed: {
    project () {
      const projectSlug = this.$route.params.slug
      const isProjectSlug = (project) => project.slug === projectSlug
      return this.$store.state.projects.projects.find(isProjectSlug)
    }
  }
})
</script>

<style lang="scss" scoped>

</style>
