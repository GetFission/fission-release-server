/* eslint no-unused-expressions: 0 */

import Vue from 'vue'
import Login from '@/components/Login'

import { expect } from 'chai'

describe('Login.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Login)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('#email')).to.exist
    expect(vm.$el.querySelector('#password')).to.exist
  })
})
