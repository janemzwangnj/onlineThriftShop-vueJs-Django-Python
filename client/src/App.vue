<template>
  <div id="app">
    <Nav />
    <main>
      <router-view header="test"></router-view>
    </main>
    <Footer />
  </div>
</template>

<script>
import Nav from './components/Nav.vue'
import Footer from './components/Footer.vue'
export default {
  name: 'App',
  components: {
    Nav,
    Footer
  },
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
  margin-top: 10px; 
  margin-bottom: 10px;
  min-height: 100vh;

}

body {
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  /* height: 100%; */
}
main {
    min-height: 80vh;
    margin-bottom: 1rem;
}
</style>
