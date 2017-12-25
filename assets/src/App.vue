<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view></router-view>
    <div class="home is-fullheight"></div>
  </div>
</template>

<script>
  import NavBar from './components/NavBar'

  export default {
    name: 'app',
    components: {
      NavBar
    }
  }
</script>

<style lang="scss">
  @import '~bulma/bulma.sass';

  #app {
    min-height: 100vh;
  }
</style>
