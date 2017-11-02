<template>
  <div class="index">
    <div class="card table-container">
      <div class="card-header">
        <div class="card-header-title">
          Releases for &nbsp;
          <span id="project-name">{{ $route.params.project }}</span>
        </div>
      </div>

      <div class="card-content">
        <div v-for="branch in branches" class="table-container">
          <span class="tag is-info is-medium">
            <span class="icon">
              <i class="fa fa-code-fork"></i>
            </span>
            {{ branch.name }}
          </span>
          <table class="table is-striped is-hoverable is-fullwidth">
            <thead>
              <tr>
                <th>Commit</th>
                <th><i class="fa fa-apple"></i></th>
                <th><i class="fa fa-windows"></i></th>
                <th><i class="fa fa-linux"></i></th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="commit in branch.commits">
                <td class="commit-hash"><a href="#">{{ commit.commit_hash }}</a></td>
                <td v-for="platform in ['mac', 'win', 'linux']">
                  <div><a v-if="buildURL(commit.builds, platform)" :href="buildURL(commit.builds, platform)">Build</a></div>
                  <div><a v-if="buildURL(commit.builds, platform)" :href="buildURL(commit.builds, platform)">CI Logs</a></div>
                </td>
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
        branches: []
      }
    },
    methods: {
      setBranches (branches) {
        this.branches = branches
      },
      buildURL (commit, platform) {
        const build = this.build(commit, platform)
        return build ? build.build_url : false
      },
      build (commit, platform) {
        console.log(commit)
        if (platform === 'mac') return commit.find(build => build.platform === 'darwin')
        if (platform === 'win') return commit.find(build => build.platform === 'win32' || build.platform === 'win64')
        if (platform === 'linux') return commit.find(build => build.platform === 'linux32' || build.platform === 'linux64')
      }
    },
    beforeRouteEnter (to, from, next) {
      // in the future, we will pass in our auth token/id and project name/api key
      REST.getBranches(to.params.project).then(response => {
        next(vm => vm.setBranches(response))
      })
    },
    beforeRouteUpdate (to, from, next) {
      this.branches = []
      REST.getBranches(to.params.project).then(response => {
        this.setBranches(response)
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

  table tbody tr td.commit-hash {
    vertical-align: middle;
  }
</style>
