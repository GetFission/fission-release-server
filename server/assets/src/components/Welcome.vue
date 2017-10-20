<template>
  <div id="welcome">
      <section class="hero is-fullheight">
        <div class="hero-body columns">
          <div class="column is-5 is-offset-1">
            <h1 class="title is-2">
              Electron releases made <span id="simple">simple</span>.
            </h1>
            <div class="subcontainer">
              <h2 class="subtitle is-4">
                <div>
                  <span class="icon has-text-info"><i class="fa fa-check-square"></i></span>
                  &#10004;
                  Advanced release strategies
                </div>
                <div>
                  <span class="icon has-text-info"><i class="fa fa-check"></i></span>
                  &#10004;
                  Simple release rollbacks
                </div>
                <div>
                  <span class="icon has-text-info"><i class="fa fa-check"></i></span>
                  &#10004;
                  Powerful release analytics
                </div>
              </h2>
            </div>
          </div>
          <div class="column is-5">
            <div class="browser-mockup">
              <div class="browser-mockup-background"></div>
            </div>
          </div>
        </div>
      </section>
  </div>
</template>

<script>
  export default {
    name: 'Welcome'
  }
</script>

<style scoped lang="scss">
  @import '~bulma/bulma.sass';

  #welcome h1, #welcome h2 {
    color: white;
  }

  #simple {
    border-bottom: 2px solid white;
  }

  .subcontainer {
    margin-top: 32px;
  }

  .browser-mockup {
    border-top: 2em solid rgba(230, 230, 230, 0.7);
    box-shadow: 0 0.1em 1em 0 rgba(0, 0, 0, 0.4);
    position: relative;
    border-radius: 3px 3px 0 0;
    max-width: 500px;
    width: 100%;
  }

  .browser-mockup:before {
    display: block;
    position: absolute;
    content: '';
    top: -1.25em;
    left: 1em;
    width: 0.5em;
    height: 0.5em;
    border-radius: 50%;
    background-color: #f44;
    box-shadow: 0 0 0 2px #f44, 1.5em 0 0 2px #9b3, 3em 0 0 2px #fb5;
  }

  .browser-mockup > * {
    display: block;
  }

  .browser-mockup-background {
    background-color: white; 
    height: 300px;
    width: 100%;
  }
</style>
