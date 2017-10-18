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
              <th>OS</th>
              <th>Date</th>
              <th>Arch</th>
              <th>Branch</th>
              <th>Build Number</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="file in files">
              <td>{{ file.version }}</td>
              <td>{{ file.os }}</td>
              <td>{{ file.date }}</td>
              <td>{{ file.architecture }}</td>
              <td>{{ file.branch }}</td>
              <td><a href="https://gitlab.com/simplyahmazing/electron-fission">{{ file.build_number }}</a></td>
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
          'All': mockData,
          'Rolling': rollingOutReleases,
          'Active': activeReleases,
          'Stale': staleReleases
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
    margin-top: 64px;
    background-image: linear-gradient(141deg, #04a6d7 0%, #209cee 71%, #3287f5 100%);
  }

  #project-name {
    border-bottom: 1px solid $blue;
  }

  .table-container {
    min-width: 580px;
  }
</style>
