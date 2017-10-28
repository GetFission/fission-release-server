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
                <th>Platform</th>
                <th>Commit</th>
                <th>Build</th>
                <th>Image</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="file in files">
                <td>{{ file.app_version }}</td>
                <td>{{ file.platform }}</td>
                <td><a href="#">{{ file.commit_hash }}</a></td>
                <td><a href="https://gitlab.com/simplyahmazing/electron-fission">{{ file.ci_job_id }}</a></td>
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
  import REST from '../services/REST'
  
  export default {
    name: 'Index',
    data: function () {
      return {
        selectedGroup: 'All',
        releases: []
      }
    },
    methods: {
      selectGroup (name) {
        this.selectedGroup = name
      },
      tabClass (name) {
        return name === this.selectedGroup ? 'is-active' : ''
      },
      setReleases (releases) {
        this.releases = releases
      }
    },
    computed: {
      branchGroups () {
        const uniqueBranches = [...new Set(this.releases.map(build => build.branch_name))]
        const branchBuilds = {}
        uniqueBranches.map(branch => {
          const builds = this.releases.filter(build => build.branch_name === branch)
          branchBuilds[branch] = builds
        })
        return branchBuilds
      }
    },
    beforeRouteEnter (to, from, next) {
      // in the future, we will pass in our auth token/id and project name/api key
      REST.getReviewApps(to.params.project).then(response => {
        next(vm => vm.setReleases(response))
      })
    },
    beforeRouteUpdate (to, from, next) {
      this.releases = []
      REST.getReviewApps(to.params.project).then(response => {
        this.setReleases(response)
        next()
      })
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
