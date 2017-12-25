<template>
  <div id="welcome">
    <section class="hero is-fullheight">
      <div class="hero-body columns is-multiline is-centered is-gapless">
        <div class="column is-5">
          <div id="description">
            <h1 class="title is-2">
              Electron releases made <span id="simple">simple</span>.
            </h1>
            <div class="subcontainer">
              <h2 class="subtitle is-4">
                <div>
                  <span class="icon"><i class="fa fa-check"></i></span>
                  Advanced release strategies
                </div>
                <div>
                  <span class="icon"><i class="fa fa-check"></i></span>
                  Simple release rollbacks
                </div>
                <div>
                  <span class="icon"><i class="fa fa-check"></i></span>
                  Powerful release analytics
                </div>
              </h2>
            </div>
          </div>
        </div>
        <div class="column is-2"></div>
        <div class="column is-5">
          <div class="browser-mockup">
            <div class="browser-mockup-background"></div>
          </div>
        </div>
        <div class="column is-4">
          <div class="field is-grouped">
            <p class="control is-expanded">
              <input ref="email" class="input extra-padding" type="text" placeholder="Enter your email">
            </p>
            <p class="control">
              <a @click="collectEmail" class="button extra-padding">
                Sign me up 
              </a>
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
  import REST from '../services/REST'

  export default {
    name: 'Welcome',
    methods: {
      collectEmail () {
        REST.collectEmail(this.$refs.email.value)
      }
    }
  }
</script>

<style scoped lang="scss">
  @import '~bulma/bulma.sass';

/*  .extra-padding {
    padding: 25px;
    }
*/

  #welcome {
    background: linear-gradient(140deg, #209cee 0%, $blue 100%);
  }

  #welcome h1, #welcome h2 {
    color: white;
  }

  #description {
    float: right;
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
    min-width: 250px;
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
