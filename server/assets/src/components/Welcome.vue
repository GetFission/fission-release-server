<template>
  <div id="welcome">
    <div id="motto">
      <section class="hero is-info is-bold is-fullheight">
        <div class="hero-body">
          <div class="container">
            <h1 class="title">
              Electron deployments made <span id="simple">simple</span>.
            </h1>
            <div class="subcontainer">
              <h2 class="subtitle">
                <div>
                  <span class="icon has-text-info"><i class="fa fa-check"></i></span>
                  Advanced release strategies
                </div>
                <div>
                  <span class="icon has-text-info"><i class="fa fa-check"></i></span>
                  Simple release rollbacks
                </div>
                <div>
                  <span class="icon has-text-info"><i class="fa fa-check"></i></span>
                  Comprehensive elease analytics
                </div>
              </h2>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'Welcome'
  }
</script>

<style>
  @import '~bulma/bulma.sass';

  #motto {
    color: white;
  }

  #simple {
    border-bottom: 1px solid $blue;
  }

  .subcontainer {
    margin-top: 32px;
  }
</style>
