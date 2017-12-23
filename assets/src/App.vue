<template>
  <div id="app">
    <NavBar></NavBar>
    <router-view></router-view>
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

  // html, body {
  //   //background: linear-gradient(140deg, #209cee 0%, $blue 100%);
  // }

  #app {
    background-image: linear-gradient(140deg, #209cee 0%, $blue 100%);
    // background: linear-gradient(140deg, #209cee 0%, $blue 100%);
    min-height: 100vh;
  }
</style>
