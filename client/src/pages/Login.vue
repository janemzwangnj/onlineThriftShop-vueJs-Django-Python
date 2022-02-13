<template>
  <div class="form-container">
    <form v-on:submit="handleSubmit">
      <input
        @input="handleChange"
        placeholder="Email"
        :value="email"
        name="email"
        type="email"
      />
      <input
        @input="handleChange"
        placeholder="Password"
        :value="password"
        name="password"
        type="password"
      />
      <button :disabled="!email || !password">Log In</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Login',
  data: ()=>({
    email: '',
    password: '',
    user: {}
  }),
  methods: {
    handleChange(e) {
      this[e.target.name] = e.target.value
    },
    handleSubmit() {
      // let data={"email": this.email, "password":this.password}
      console.log("banana")
      const res = axios.get(`http://localhost:8000/login/${this.email}/${this.password}`)
     
      console.log(res)
       alert("before assign to user")
      this.user = res.data
      alert("after assign to user")
    }
  }
}
</script>
<style scoped>

.form-container {
  width: 70vw;
  margin: 1em auto;
  padding: 2em 1em;
  border-radius: 10px;
  background-color: #a7a7d3;
  border: 2px solid #424288;
}

form {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

input {
  background: inherit;
  border: 1px solid #47476d;
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
  background: #6c74a8;
}

button {
  cursor: pointer;
}.form-container {
  width: 70vw;
  margin: 1em auto;
  padding: 2em 1em;
  border-radius: 10px;
  background-color: #e8f5e9;
  border: 2px solid #b0b0cf;
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
  background-color: #85c1a6;
  border: none;
  font-weight: 700;
}

button:disabled {
  cursor: auto;
  background-color: #81c6a7;
  color: #374279;
}

button:hover:not([disabled]) {
  background-color: #a1a6c0;
  color: #0b0c18;
}

input:focus,
input:active {
  outline: none;
  background: #a1a5c4;
}

button {
  cursor: pointer;
}
</style>