<template>
  <nav class="navbar" role="navigation" aria-label="main navigation">
    <div class="navbar-brand">
      <a class="navbar-item" href="#">
        <img src="../../static/electron.png" alt="Electron Fission Logo">
      </a>
    </div>

    <div class="navbar-item has-dropdown is-hoverable">
      <a class="navbar-link">
        Documentation
      </a>

      <div class="navbar-dropdown">
        <a class="navbar-item">
          Overview
        </a>
        <a class="navbar-item">
          Quick Start
        </a>
        <a class="navbar-item">
          FAQ
        </a>
        <hr class="navbar-divider">
        <div class="navbar-item">
          Version 0.1.0
        </div>
      </div>
    </div>

    <a class="navbar-item " href="#">
      <span class="bd-emoji">⭐️</span>
      &nbsp; Star
    </a>

    <div class="navbar-end">
      <div class="navbar-item">
        <div class="button">Login</div>
      </div>
      <div class="navbar-item">
        <div class="button is-link">Signup</div>
      </div>
    </div>
  </nav>
</template>

<script>
  export default {
    name: 'NavBar'
  }
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Courgette|Pacifico');
  @import '~bulma/bulma.sass';

  nav {
    padding-left: 64px;
    padding-right: 64px;
  }
</style>
