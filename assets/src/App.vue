<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view></router-view>
  </div>
</template>

<script>
  import NavBar from './components/NavBar'
  // import SignUp from './components/SignUp'

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
    background-image: linear-gradient(140deg, #209cee 0%, $blue 100%);
    min-height: 100vh;
  }
</style>
