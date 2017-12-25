<template>
  <aside class="menu">
    <p class="menu-label">
      General
    </p>
    <ul class="menu-list">
      <li>
        <a class="is-active">Overview</a>
      </li>
    </ul>
    <p class="menu-label">
      Projects <span class="tag is-info">2</span>
    </p>
    <ul class="menu-list">
      <li>
        <a>Zulip</a>
        <ul>
          <li>
            <a>Dashboard</a>
          </li>
          <li>
            <a>Releases</a>
          </li>
          <li>
            <a>Settings</a>
          </li>
        </ul>
      </li>
      <li>
        <a>My Other App</a>
        <ul>
          <li>
            <a>Dashboard</a>
          </li>
          <li>
            <a>Releases</a>
          </li>
          <li>
            <a>Settings</a>
          </li>
        </ul>
      </li>
    </ul>
    <a class="button">Add project</a>
    <p class="menu-label">
      Administration
    </p>
    <ul class="menu-list">
      <li>
        <a>Account Settings</a>
      </li>
      <li>
        <a>Payments</a>
      </li>
    </ul>
  </aside>
</template>

<script>
import Vue from 'vue'

export default Vue.component('dashboard-sidebar', {
  data: function () {
    return {
    }
  }
})
</script>

<style lang="scss">
  // #dashboard {
  //   // margin-top: 1rem;
  //   background: #ECF0F3;
  // }

 // .hero-body { flex-grow: 1; flex-shrink: 0; padding: 0rem 1.5rem; border: dotted}
  // .hero-body {
  //   align-items: unset;
  // }

  
  // nav.navbar {
  //   border-top: 4px solid #276cda;
  //   margin-bottom: 1rem;
  // }
  // .navbar-item.brand-text {
  //   font-weight: 300;
  // }
  // .navbar-item, .navbar-link {
  //   font-size: 14px;
  //   font-weight: 700;
  // }
  // .columns {
  //   width: 100%;
  //   height: 100%;
  // }
  // .menu-label {
  //   color: #8F99A3;
  //   letter-spacing: 1.3;
  //   font-weight: 700;
  // }
  // .menu-list a {
  //   color: #0F1D38;
  //   font-size: 14px;
  //   font-weight: 700;
  // }
  // .menu-list a:hover {
  //   background-color: transparent;
  //   color: #276cda;
  // }
  // .menu-list a.is-active {
  //   background-color: transparent;
  //   color: #276cda;
  //   font-weight: 700;
  // }
  // .card {
  //   box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.18);
  //   margin-bottom: 2rem;
  // }
  // .card-header-title {
  //   color: #8F99A3;
  //   font-weight: 400;
  // }
  // .info-tiles {
  //   margin: 1rem 0;
  // }
  // .info-tiles .subtitle {
  //   font-weight: 300;
  //   color: #8F99A3;
  // }
  // .hero.welcome.is-info {
  //   background: #36D1DC;
  //   background: -webkit-linear-gradient(to right, #5B86E5, #36D1DC);
  //   background: linear-gradient(to right, #5B86E5, #36D1DC);
  // }
  // .hero.welcome .title, .hero.welcome .subtitle {
  //   color: hsl(192, 17%, 99%);
  // }
  // .card .content {
  //   font-size: 14px;
  // }
  // .card-footer-item {
  //   font-size: 14px;
  //   font-weight: 700;
  //   color: #8F99A3;
  // }
  // .card-footer-item:hover {
  // }
  // .card-table .table {
  //   margin-bottom: 0;
  // }
  // .events-card .card-table {
  //   max-height: 250px;
  //   overflow-y: scroll;
  // }
</style>
