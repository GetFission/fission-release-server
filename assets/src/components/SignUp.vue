<template>
  <div id="signup">
    <section class="hero is-success is-fullheight">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-4 is-offset-4">
            <h3 class="title has-text-grey">Sign up</h3>
            <p class="subtitle has-text-grey">Create your new account</p>
            <div class="box">
              <div v-show="!submissionComplete">
                <form action="">
                  <div v-for="error in errorResp.non_field_errors">
                      <p class="help is-danger">{{ error }}</p>
                    </div>
                  <div class="field">
                    <label class="label has-text-grey">Email</label>
                    <div class="control">
                      <input v-model="email" id="email" type="email" class="input is-large" placeholder="user@gmail.com">
                    </div>
                    <div v-for="error in errorResp.email">
                      <p class="help is-danger">{{ error }}</p>
                    </div>
                  </div>

                  <div class="field">
                    <label class="label has-text-grey">Password</label>
                    <div class="control">
                      <input v-model="password1" id="password1" type="password" class="input is-large" placeholder="Enter password">
                    </div>
                    <div v-for="error in errorResp.password1">
                      <p class="help is-danger">{{ error }}</p>
                    </div>
                  </div>

                  <div class="field">
                    <div class="control">
                      <input v-model="password2" id="password2" type="password" class="input is-large" placeholder="Enter password again">
                    </div>
                    <div v-for="error in errorResp.password2">
                      <p class="help is-danger">{{ error }}</p>
                    </div>
                  </div>

                  <a @click="register" class="button is-block is-link is-large">Submit</a>
                </form>
              </div>
              <div v-show="submissionComplete">
                <p class="has-text-gre">Registration successful. Check your email to validate your account</p>
              </div>
            </div>

            <p class="has-text-grey">
              <router-link :to="{'name': 'login'}">Login</router-link> &nbsp;·&nbsp;
              <router-link :to="{'name': 'need-help'}">Need help?</router-link> &nbsp;&nbsp;
            </p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>


<script>
import Vue from 'vue'
import { mapGetters } from 'vuex'

export default Vue.component('SignUp', {
  data: function () {
    return {
      email: '',
      password1: '',
      password2: '',
      submissionComplete: false
    }
  },
  computed: {
    ...mapGetters('user', {
      state: 'GET_STATE',
      error: 'GET_ERROR'
    }),
    errorResp: function () {
      return this.$store.state.user.error
    }
  },
  methods: {
    register: async function () {
      // console.log('registering', this.email, this.password, this.$store)
      await this.$store.dispatch('register', {
        email: this.email,
        password1: this.password1,
        password2: this.password2
      })
      this.submissionComplete = true
    }
  },
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
