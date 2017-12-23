<template>
  <div id="signup">
    <section class="hero is-success is-fullheight">
      <div class="hero-body">
        <div class="container has-text-centered">
          <div class="column is-4 is-offset-4">
            <h3 class="title has-text-grey">Login</h3>
            <p class="subtitle has-text-grey">Welcome back</p>
            <div class="box">
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
                    <input v-model="password" id="password" type="password" class="input is-large" placeholder="Enter password">
                  </div>
                  <div v-for="error in errorResp.password">
                    <p class="help is-danger">{{ error }}</p>
                  </div>
                </div>

                <a @click="authenticate" class="button is-block is-link is-large">Submit</a>
              </form>
            </div>

            <p class="has-text-grey">
              <router-link :to="{'name': 'signup'}">Sign up</router-link> &nbsp;·&nbsp;
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

export default Vue.component('Login', {
  data: function () {
    return {
      email: '',
      password: ''
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
    authenticate: async function () {
      // console.log('registering', this.email, this.password, this.$store)
      await this.$store.dispatch('authenticate', {
        email: this.email,
        password: this.password
      })
      this.$router.push({ name: 'dashboard' })
    }
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