<template>
  <div id="app">
    <img alt="Vue logo" src="../../images/vue.png">
    <img alt="Python3 logo" src="../../images/python3.png">
    <img alt="Django logo" src="../../images/restframework.png">
    <img alt="PostgreSql logo" src="../../images/postgres.png">
    <SignInForm :email='email' :password='password' @handleFormChange="handleFormChange" @handleSubmit="handleSubmit"/>
    <!-- <div class="form-container">
      <form @submit="handleSubmit">
        <input placeholder="Email" :value="email" name="email" type="email" v-on:input="handleFormChange"/>
        <input
          placeholder="Password"
          :value="password"
          name="password"
          type="password"
          @input="handleFormChange"
        />
        <button>Log In</button>
      </form>
    </div> -->

  </div>
</template>

<script>

import SignInForm from './components/SignInForm.vue'

export default {
  name: 'App',
  components: {
    //  HelloWorld
    SignInForm
  },
  data: ()=> ({
    email: '',
    password: ''
  }),
  methods: {
    // handleFormChange(e){
    //   this[e.target.name] = e.target.value
    // },
    // handleSubmit(e){
    //   e.preventDefault()
    //   alert('Form Submitted')
    //   this.email=''
    //   this.password=''
    // }
    handleFormChange(name, value){
      this[name] = value
    },
    handleSubmit(){
      alert('Form Submitted')
      this.email = ''
      this.password = ''
    }
  }
}
</script>

<style>
html {
  background-color: #a4aad3;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #bbcbde;
  margin-top: 60px;
}

.form-container {
  width: 70vw;
  margin: 1em auto;
  padding: 2em 1em;
  border-radius: 10px;
  background-color: #d7d7eb;
  border: 2px solid #07070b;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

input {
  background: inherit;
  border: 1px solid #07070b;
}

input,
button {
  width: 70%;
  margin: 0.5em auto;
  padding: 0.6em 1em;
  border-radius: 10px;

  color: #d4d2d2;
  font-size: 1.2rem;
  transition: all 0.2s ease;
}

button {
  background-color: #596799;
  border: none;
  font-weight: 700;
}

button:disabled {
  cursor: auto;
  background-color: #252734;
  color: #a1a6c0;
}

button:hover:not([disabled]) {
  background-color: #a1a6c0;
  color: #252734;
}

input:focus,
input:active {
  outline: none;
  background: #252734;
}

button {
  cursor: pointer;
}
</style>
