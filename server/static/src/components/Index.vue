<template>
  <div class="index">
    <div class="card">
      <div class="card-header">
        <div class="card-header-title">
          Releases for &nbsp;
          <span id="project-name">Zulip</span>
        </div>
      </div>

      <div class="card-content">
        <div class="tabs">
          <ul>
            <li v-for="(_, name) in fileGroups" @click="selectGroup(name)" :class=tabClass(name)>
              <a>{{ name }}</a>
            </li>
          </ul>
        </div>

        <table v-for="(files, name) in fileGroups" v-show="name === selectedGroup" class="table is-striped is-hoverable is-fullwidth">
          <thead>
            <tr>
              <th>Version</th>
              <th>Date</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="file in files">
              <td>{{ file.version }}</td>
              <td>{{ file.date }}</td>
            </tr>
          </tbody>
        </table>
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
          'Rolling': rollingOutReleases,
          'Active': activeReleases,
          'Stale': staleReleases,
          'All': mockData
        }
      }
    }
  }
</script>

<style scoped lang="scss">
  @import '~bulma/bulma.sass';

  .index {
    width: 50vw;
    margin: 0 auto;
    margin-top: 32px;
  }

  #project-name {
    border-bottom: 1px solid $blue;
  }
</style>
