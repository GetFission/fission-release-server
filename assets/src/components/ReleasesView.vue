<template>
  <div class="releases">
    <section class="hero is-info welcome is-small">
      <div class="hero-body">
        <div class="container">
          <h1 class="title">
            {{ project.name }} Releases
          </h1>
          <h2 class="subtitle">
            View and deploy alpha, beta, and versioned releases
          </h2>
        </div>
      </div>
    </section>
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
            <button class="button is-large is-info"><i class="fa fa-plus" aria-hidden="true"></i>&nbsp;&nbsp;Create new release</button>
          </article>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import Vue from 'vue'

export default Vue.component('ReleasesPane', {
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

<style lang="scss">
  .hero.welcome.is-info {
    background: #36D1DC;
    background: -webkit-linear-gradient(to right, #5B86E5, #36D1DC);
    background: linear-gradient(to right, #5B86E5, #36D1DC);
  }

  .hero.welcome .title, .hero.welcome .subtitle {
    color: hsl(192, 17%, 99%);
  }

  .info-tiles {
    margin: 1rem 0;
  }

  .info-tiles .subtitle {
    font-weight: 300; color: #8F99A3;
  }
</style>
