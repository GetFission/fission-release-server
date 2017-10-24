<template>
  <div class="index">
    <div class="card table-container">
      <div class="card-header">
        <div class="card-header-title">
          Releases for &nbsp;
          <span id="project-name">Zulip</span>
        </div>
      </div>

      <div class="card-content">
        <div v-for="(files, branch) in branchGroups" class="table-container">
          <span class="tag is-info is-medium">
            <span class="icon">
              <i class="fa fa-code-fork"></i>
            </span>
            {{ branch }}
          </span>
          <table class="table is-striped is-hoverable is-fullwidth">
            <thead>
              <tr>
                <th>Version</th>
                <th>Date</th>
                <th>OS</th>
                <th>Arch</th>
                <th>Commit</th>
                <th>Build</th>
                <th>Image</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="file in files">
                <td>{{ file.version }}</td>
                <td>{{ file.date }}</td>
                <td>{{ file.os }}</td>
                <td>{{ file.architecture }}</td>
                <td><a href="#">{{ Math.random().toString(36).substring(7) }}</a></td>
                <td><a href="https://gitlab.com/simplyahmazing/electron-fission">{{ file.build_number }}</a></td>
                <td><a href="#">S3</a></td>
              </tr>
            </tbody>
          </table>
          <hr />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  const mockData = require('../../static/files.json')
  
  export default {
    name: 'Index',
    data: function () {
      return {
        mockData: mockData,
        selectedGroup: 'All'
      }
    },
    methods: {
      selectGroup (name) {
        this.selectedGroup = name
      },
      tabClass (name) {
        return name === this.selectedGroup ? 'is-active' : ''
      }
    },
    computed: {
      fileGroups () {
        const staleReleases = mockData.filter(release => !release.active)
        const activeReleases = mockData.filter(release => release.active)
        const rollingOutReleases = mockData.filter(release => release.rollout)
        return {
          'All': mockData,
          'Rolling': rollingOutReleases,
          'Active': activeReleases,
          'Stale': staleReleases
        }
      },
      branchGroups () {
        const uniqueBranches = [...new Set(mockData.map(build => build.branch))]
        const branchBuilds = {}
        uniqueBranches.map(branch => {
          const builds = mockData.filter(build => build.branch === branch)
          branchBuilds[branch] = builds
        })
        return branchBuilds
      }
    },
    beforeRouterEnter (to, from, next) {
      // fetch data from Flask - send client auth object with ID and token
      // if user exists and has associated builds, return them.
      // another option would be to handle that logic immediately after authentication,
      // and have this component simply redirect home if there is no proper data fed to it.
    },
    beforeRouteUpdate (to, from, next) {
      // see above
    }
  }
</script>

<style scoped lang="scss">
  @import '~bulma/bulma.sass';
  
  .index {
    width: 50vw;
    margin: 0 auto;
    margin-top: 64px;
    background-image: linear-gradient(141deg, #04a6d7 0%, #209cee 71%, #3287f5 100%);
  }
  
  #project-name {
    border-bottom: 1px solid $blue;
  }
  
  .table-container {
    min-width: 580px;
  }
  
  .table, {
    margin-bottom: 0px;
  }
  
  hr {
    margin-top: 0px;
  }
</style>
