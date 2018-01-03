<template>
  <div id="dashboard">
    <div class="hero is-fullheight">
      <div id="dashboard" class="hero-body is-fullheight">
        <div class="container">
          <div class="columns">
            <div class="column is-2">
              <dashboard-sidebar></dashboard-sidebar>
            </div>
            <div class="column is-10 dashboard-body">
              <router-view></router-view>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>


<script>
import Vue from 'vue'
import DashboardSidebar from '@/components/DashboardSidebar'

export default Vue.component('Dashboard', {
  components: {
    DashboardSidebar
  },
  async created () {
    await this.$store.dispatch('LOAD_PROJECTS')
  }
})
</script>

<style lang="scss">
  #dashboard {
    background: #ECF0F3;
    align-items: flex-start;
  }
</style>
