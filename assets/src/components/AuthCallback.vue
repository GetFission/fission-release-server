<template>
  <div class="spinner">
    <img src="../../static/loading.svg" alt="loading"/>
  </div>
</template>

<script>
  import router from '../router/index.js'

  export default {
    name: 'callback',
    async mounted () {
      await this.$store.dispatch('handleAuthentication')
      router.push({name: 'dashboard'})
    }
  }
</script>

<style>
  .spinner {
    position: absolute;
    display: flex;
    justify-content: center;
    height: 100vh;
    width: 100vw;
    background-color: white;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
  }
</style>
