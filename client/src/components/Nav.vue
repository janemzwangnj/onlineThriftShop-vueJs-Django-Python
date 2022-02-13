<template>
  <div class="nav">
  <h2>
  Local Online Thrift Store
  </h2>
  <nav>
    <!-- Nav Links Go Here -->
    <router-link to="/" name="Home">Home</router-link>
    <router-link to="/items" name="Items">Items</router-link>
    <router-link to="/login" name="Login">Login</router-link>
    <router-link to="/signup" name="SignUp">SignUp</router-link> 
  </nav>
  </div>
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
.nav {
  background: #8bbba5;
  padding: 0 1em; 
  display: flex;
  justify-content:space-around;
  align-items: center;
}
nav a {
  margin: 1em;
  color: #2c3e50;
  text-decoration: none;
  font-weight: 800;
}
</style>
