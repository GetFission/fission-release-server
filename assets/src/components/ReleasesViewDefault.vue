<template>
  <section class="info-tiles">
    <div class="tile is-ancestor has-text-centered">
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="title">0</p>
          <p class="subtitle">Total releases</p>
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child box">
          <p class="title">0</p>
          <p class="subtitle">Active releases</p>
        </article>
      </div>
      <div class="tile is-parent">
        <article class="tile is-child box">
          <router-link class="button is-large is-info" tag="button" :to="{name: 'dashboard.releases.create-release', params: {slug: project.slug}}">
            <i class="fa fa-plus" aria-hidden="true"></i>&nbsp;&nbsp;Create new release</router-link>
        </article>
      </div>
    </div>
    <table class="table is-striped is-fullwidth is-hoverable">
      <tbody>
        <tr>
          <th>Name</th>
          <th>Version</th>
          <th>Platforms</th>
          <th>Created</th>
          <th>Released</th>
          <th>Status</th>
          <th></th>
        </tr>
        <tr v-for="release in releases" :key="release.id">
          <td>{{ release.name ? release.name : 'N/A' }}</td>
          <td>{{ release.version }}</td>
          <td>Mac, Linux, Win</td>
          <td>{{ release.created }}</td>
          <td>N/A</td>
          <td>{{ release.status ? release.status : 'N/A' }}</td>
          <td><button @click="showModal(release.id)" class="button is-info">manage</button></td>
        </tr>
      </tbody>
    </table>
    <div v-if="isModalActive" class="modal is-active">
      <div class="modal-background"></div>
      <div class="modal-content">
        <div class="card">
          <div class="card-header">
            <div class="card-header-title is-centered">
              Manage Release
            </div>
          </div>
         <div class="card-content">
           <div class="level">
             <div class="level-left">
               <div class="level-item">
                 <table class="table">
                   <thead>
                       <tr>
                         <th></th>
                         <th>Mac</th>
                         <th>Win</th>
                         <th>Linux</th>
                       </tr>
                   </thead>
                   <tbody>
                    <tr>
                      <td>Release Target</td>
                      <td>40</td>
                      <td>4</td>
                      <td>45</td>
                    </tr>
                   <tr>
                      <td>Release Progress</td>
                      <td>250</td>
                      <td>90</td>
                      <td>40</td>
                    </tr>
                   </tbody>
                 </table>
               </div>
             </div>
             <div class="level-right">
               <div class="level-item">
                 <div class="tile is-ancestor">
                   <div class="tile is-parent is-vertical">
                     <div class="tile is-child">
                       <ReleaseAudienceForm></ReleaseAudienceForm>
                     </div>
                     <div class="tile is-child">
                       <a @click="updateReleaseAudience()" class="button is-centered">Update audience</a>
                     </div>
                   </div>
                 </div>
               </div>
             </div>
           </div>
           <div class="level">
             <div class="level-left">
               <div class="level-item">
               </div>
             </div>
           </div>
         </div>
          <div class="card-footer">
            <a class="card-footer-item">Deactivate</a>
            <router-link :to="{name: 'dashboard.releases.create-release', params: {slug: $route.params.slug}}" class="card-footer-item">Edit</router-link>
            <a @click="isModalActive = false" class="card-footer-item">Close</a>
          </div>
        </div>
      </div>
    </div>
  </section>

</template>

<script>
import Vue from 'vue'

import ReleaseAudienceForm from '@/components/ReleaseAudienceForm'
import ReleasesAPI from '../services/releases'

const releasesAPI = new ReleasesAPI()

export default Vue.component('ReleasesViewDefault', {
  components: {
    ReleaseAudienceForm
  },
  data: function () {
    return {
      isModalActive: true,
      modalRelease: null,
      releases: [
        // {id: 1, name: 'alpha', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'},
        // {id: 2, name: 'beta', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'},
        // {id: 3, name: 'gamma', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'},
        // {id: 4, name: 'sigma', version: '1.1.1', created: 'Jan 1st', status: 'Deployed'}
      ]
    }
  },
  computed: {
    project () {
      const projectSlug = this.$route.params.slug
      const isProjectSlug = (project) => project.slug === projectSlug
      return this.$store.state.projects.projects.find(isProjectSlug)
    }
  },
  methods: {
    showModal (modalId) {
      this.isModalActive = true
      this.modalRelease = this.releases[modalId]
      console.log(modalId)
    },
    updateReleaseAudience () {
      alert('implement update...')
    }
  },
  mounted () {
    const that = this
    const projectSlug = this.$route.params.slug
    releasesAPI.getReleases(projectSlug) // eventually take page #
      .then((data) => {
        console.log(data)
        that.releases = data.data.results
      })
      .catch((err) => {
        console.log('error fetching releases', err)
      })
  }
})
</script>

<style lang="scss" scoped>

</style>
