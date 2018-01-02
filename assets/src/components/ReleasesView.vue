<template>
  <div class="releases">
    Manage releases for {{ project }}
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
      return this.$route.params.slug
    }
  }
})
</script>

<style lang="scss">
</style>


