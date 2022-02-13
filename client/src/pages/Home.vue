<template>
  <div class="flex-content">
    <div>
    </div>
    <div class="hero-img">
      <img src="../../../images/selling.png" />
    </div>
    <div class="prompt">
      <h1>Sell Your Unwanted Stuff</h1>
      <p>Shopping For Saving!</p>
      <button @click="$router.push('/items')">Get Started</button>
   </div>
  </div> 
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
body {
min-height: 100vh;
}
.flex-content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  /* height: 100%; */
}
.hero-img {
  width: 60%;
}
.hero-img img {
  width: 80%;
}
.prompt {
  background: #e8f5e9;
  padding: 6em 4em;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
} 
.prompt button {
  cursor: pointer;
  margin: auto;
  padding: 1em 1.4em;
  border-radius: 14px;
  border: 0;
  width: 80%;
  background-color: #42b983;
}
</style>