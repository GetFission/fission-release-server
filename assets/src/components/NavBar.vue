<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <router-link to="/" class="navbar-item" href="/#">
        <img src="../../static/electron.png" alt="Electron Fission Logo">
      </router-link>
    </div>

    <div class="navbar-menu">
      <div class="navbar-start">
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Documentation
          </a>

          <div class="navbar-dropdown">
            <a class="navbar-item">
              Quick Start
            </a>
            <a class="navbar-item">
              Overview
            </a>
            <hr class="navbar-divider">
            <div class="navbar-item">
              Version 0.1.0
            </div>
          </div>
        </div>

        <a class="navbar-item" href="https://gitlab.com/simplyahmazing/electron-fission">
          <span class="bd-emoji">⭐️</span>
          &nbsp; Star
        </a>
      </div>

      <div class="navbar-end">
        <div v-show="email" class="navbar-item">
          <p>Welcome, {{ email }}</p>
        </div>
        <div v-show="!isAuthenticated" class="navbar-item">
          <a @click="authenticate" class="button is-link">Login / Signup</a>
        </div>
        <div v-show="isAuthenticated" class="navbar-item">
          <a @click="deauthenticate" class="button is-link">Logout</a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavBar',
    computed: {
      isAuthenticated () {
        const profile = this.$store.state.user.profile
        return profile && profile.email
      },
      email () {
        const profile = this.$store.state.user.profile
        return profile ? profile.email : null
      }
    },
    methods: {
      async deauthenticate () {
        await this.$store.dispatch('deauthenticate')
        this.$router.push({name: 'Welcome'})
      },
      async authenticate () {
        this.$store.dispatch('authenticate')
      }
    }
  }
</script>

<style scoped lang="scss">
  nav {
    padding-left: 64px;
    padding-right: 64px;
  }
</style>
