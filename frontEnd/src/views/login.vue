<template>
  <div class="login-box">
    <div class="login-logo">
      <a href="/"><b>Putbox</b> Co.</a>
    </div>
    <!-- /.login-logo -->
    <div class="login-box-body">
      <p class="login-box-msg">登录进入工作台</p>

      <div>
        <div class="alert alert-danger" v-bind:class="{ 'hidden': isA }">{{ errorMessage }}</div>
        <div class="form-group has-feedback">
          <input v-model="username" type="text" class="form-control" placeholder="用户名">
          <span class="glyphicon glyphicon-envelope form-control-feedback"></span>
        </div>
        <div class="form-group has-feedback">
          <input v-model="password" type="password" class="form-control" placeholder="密码">
          <span class="glyphicon glyphicon-lock form-control-feedback"></span>
        </div>
        <div class="row">
          <div class="col-xs-4">
            <button v-on:click="login" class="btn btn-primary btn-block btn-flat">登录</button>
          </div>
          <!-- /.col -->
        </div>
      </div>

      <div class="social-auth-links text-center">
        <p></p>
      </div>
      <!-- /.social-auth-links -->

      <a href="#">忘记密码</a><br>
      <a href="register.html" class="text-center">注册新账户</a>

    </div>
    <!-- /.login-box-body -->
  </div>
  <!-- /.login-box -->
</template>
<script>
import $ from 'jquery'
var common = require('commonFunc')
var CryptoJS = require('crypto-js')

function aesEncryptModeCFB (msg, key, iv) {
  return CryptoJS.AES.encrypt(msg, key, { iv: iv, mode: CryptoJS.mode.CFB, padding: CryptoJS.pad.Pkcs7 }).toString()
}

// function aesDecryptModeCFB (ciphertext, key, iv) {
//   return CryptoJS.AES.decrypt(CryptoJS.enc.Base64.parse(ciphertext), key, { iv: iv, mode: CryptoJS.mode.CFB }).toString(CryptoJS.enc.Utf8)
// }

function generateRandomAlphaNum (len) {
  var rdmString = ''
  // toSting接受的参数表示进制，默认为10进制。36进制为0-9 a-z
  for (; rdmString.length < len;) { rdmString += Math.random().toString(16).substr(2) }
  return rdmString.substr(0, len)
}

export default{
  name: 'login',
  data: function () {
    return {
      username: '',
      password: '',
      errorMessage: '',
      isA: true
    }
  },
  created: function () {
    $('body').removeClass()
    $('body').addClass('hold-transition')
    $('body').addClass('login-page')
  },
  methods: {
    login: function (event) {
      var magicNo = generateRandomAlphaNum(32)
      var key = CryptoJS.enc.Hex.parse(CryptoJS.MD5(this.password).toString())
      var iv = CryptoJS.enc.Hex.parse(magicNo)
      // console.log(aesDecryptModeCFB('r19YcF8gc8bgk5NNui6I3w==', key, iv))
      var username = this.username
      var identifyCode = aesEncryptModeCFB(username, key, iv)
      this.$http.post('/api/auth', { oid: 2, username: username, identifyCode: identifyCode, magicNo: magicNo }).then((response) => {
        var token = response.headers['authorization']
        if (!token) {
          console.log(response.headers['Authorization'])
          token = response.headers['Authorization']
        }
        if (token) {
          common.clearStoreData()
          common.setStoreData('token', token)
          common.setStoreData('userinfo', response.json()['data'])
          $('body').removeClass()
          $('body').addClass('hold-transition')
          $('body').addClass('skin-blue')
          $('body').addClass('sidebar-mini')
          this.$router.go({ path: '/system/home' })
        } else {
          this.errorMessage = '系统错误'
          this.isA = false
          common.clearStoreData()
        }
      }, (response) => {
        // error callback
        this.errorMessage = '用户名或者密码错误'
        this.isA = false
        console.log(response.status)
        console.log(response.data)
        common.clearStoreData()
      })
    }
  }
}
</script>
<style>
</style>
