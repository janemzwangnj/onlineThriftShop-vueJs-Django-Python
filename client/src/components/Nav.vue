<template>
  <nav>
    <!-- Nav Links Go Here -->
    <router-link to="/" name="Home">Home</router-link>
    <router-link to="/items" name="Items">Items</router-link>
    <router-link to="/users/:id" name="Login">Login</router-link>
    <router-link to="/users" name="SignUp">SignUp</router-link> 
  </nav>
</template>

<script>
export default {
  name: 'Nav'
}
</script>

<style>
.router-link-exact-active {
  color: #fff;
}
nav {
  background: #8bbba5;
  padding: 1em;
  display: flex;
  justify-content: right;
}
nav a {
  margin: 1em;
  color: #2c3e50;
  text-decoration: none;
  font-weight: 800;
}
</style>
