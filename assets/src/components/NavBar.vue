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
        <div class="navbar-item">
          <router-link :to="{'name': 'login'}" class="button is-link">Login</router-link>
        </div>
        <div class="navbar-item">
          <router-link :to="{'name': 'signup'}" class="button is-link">Signup</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavBar'
  }
</script>

<style scoped lang="scss">
  nav {
    padding-left: 64px;
    padding-right: 64px;
  }
</style>
