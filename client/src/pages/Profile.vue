<template>
    <div class="Items">
      <h3>Selling Items</h3>
      <section class="container-grid">
        <div :key="item.id" v-for="item in items" @click="navigateItem(item.id)">
          <!-- <ItemCard :item="item"/> -->
          <div class="image-wrapper">
          <img alt="item" :src="item.image" width="300" height="200">
          <h4>Item: {{item.name}}</h4>
          <h4>Asking Price: {{item.asking_price}}</h4>
          <h4>Condition: {{item.condition}}</h4>
          </div>
        </div>
      </section>
      </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'Items',
  data: ()=>({
    items:[]
  }),
  mounted() {
    this.getItems()
    },
  methods:{
    async getItems() {
      const res = await axios.get('http://localhost:8000/items')
      this.items = res.data
    },
    navigateItem(id){
      this.$router.push(`/items/${id}`)
    }
  }
}

</script>

<style scoped>
/* .flex-content {
  display: flex;
  justify-content: space-around;
  align-items: center;
  height: 100%;
} */
.container-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  align-items: center;
}
.image-wrapper {
  width: 100%;
  border-radius: 20px;
  border: 2px solid rgba(0, 0, 0, 0.4);
  background: #fff;
  box-shadow: 4px 4px 14px 0px rgba(50, 50, 50, 0.39);
  transition: all 0.2s ease;
  cursor: pointer;
  padding-top: 10px;
}
h4 {
  margin: 0 auto;
}

</style>