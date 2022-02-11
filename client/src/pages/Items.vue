<template>
  <div class="flex-content">
    <div>
    hello from Items
    </div>
    <div class="hero-img">
      <img src="../../../images/django.png" />
    </div>
    <div class="prompt">
      <h1>Fancy Rentals</h1>
      <p>One Stop Shop For All Of Your Car Rental Needs!</p>
      <!-- <button @click="$router.push('/listings')">Get Started</button> -->
   </div>
  </div> 
</template>

<script>
export default {
  name: 'Items'
}
</script>

<style scoped>
.flex-content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 100%;
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