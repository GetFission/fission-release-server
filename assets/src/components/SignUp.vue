<template>
  <div id="signup">
    <section class="hero is-success is-fullheight">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-4 is-offset-4">
            <h3 class="title has-text-grey">Sign up</h3>
            <p class="subtitle has-text-grey">Create your new account</p>
            <div class="box">
              <form action="">
                <div class="field">
                  <div class="control">
                    <input id="email" type="email" class="input is-large" placeholder="Your email">
                  </div>
                </div>

                <div class="field">
                  <div class="control">
                    <input id="password" type="password" class="input is-large" placeholder="Your password">
                    </div>
                </div>

                <div class="field">
                  <div class="control">
                    <input id="re_password" type="password" class="input is-large" placeholder="Your password">
                    </div>
                </div>

                <a class="button is-block is-info is-large">Submit</a>
              </form>
            </div>

            <p class="has-text-grey">
              <a :to="{'name': 'login'}">Login</a> &nbsp;·&nbsp;
              <a :to="{'name': 'need-help'}">Need help?</a> &nbsp;&nbsp;
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
import Vue from 'Vue'

export default Vue.component('SignUp', {
  mounted () {
    // alert('got here..')
  }
})
</script>

<style lang="scss">
#signup {
  font-family: 'Open Sans', serif;
  font-size: 14px;
  font-weight: 300;
}

.hero.is-success {
  background: #F2F6FA;
  -webkit-box-shadow: none;
  box-shadow: none;
}

.box {
  margin-top: 3rem;
}

input {
  font-weight: 300;
}

p {
  font-weight: 700;
}

p.subtitle {
  padding-top: 1rem;
}
</style>
