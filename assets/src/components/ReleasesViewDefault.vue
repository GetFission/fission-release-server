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
  </section>
</template>

<script>
import Vue from 'vue'

export default Vue.component('ReleasesViewDefault', {
  data: function () {
    return {
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
