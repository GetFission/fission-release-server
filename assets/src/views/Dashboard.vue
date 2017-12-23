<template>
  <div id="dashboard">
    <dashboard-sidebar></dashboard-sidebar>
  </div>
</template>


<script>
import Vue from 'vue'
import '@/components/DashboardSidebar'

export default Vue.component('dashboard', {
  name: 'Dashboard'
})
</script>

