<template>
  <div class="item-content" v-if="itemView">
    <section class="image-container">
      <div>
        <img :src="itemView.image" width="300" height="200" />
      </div>
    </section>
    <section class="details">
        <strong>{{itemView.name}}</strong> <br>
        Asking Price: <strong>{{itemView.asking_price}}</strong> <br>
        Condition:<strong> {{itemView.condition}}</strong> <br>
        Origin Purchasing Date:<strong> {{itemView.origin_purchasing_time}}</strong><br>
        Origin Price: <strong>{{itemView.origin_price}}</strong><br>
        <div v-if="itemView.sold_mark">
          Sold:  <strong>[ ✔️ ]</strong> 
        </div>
        <div v-else>
          Sold:<strong> [   ]</strong> 
        </div> <br>
        <button class="new" @click="addItem">New Item</button>
        <button class="update" @click="updateItem">Update Item</button>
        <button class="delete" @click="deleteItem">Delete Item</button>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ItemView',
  data: () => ({
    itemView: null,
    itemId: null
  }),
  mounted() {
    this.getItemView()
  },
  methods: {
    async getItemView() {   
      this.itemId = this.$route.params.item_id
      const res = await axios.get(`https://mysterious-lake-42419.herokuapp.com/items/${this.itemId}`)
      this.itemView = res.data
    },
    addItem(){
      this.$router.push('/additem')
    },
    updateItem(){
      this.$router.push(`/updateitem/${this.itemId}`)
    },
    deleteItem(){
    axios.delete(`https://mysterious-lake-42419.herokuapp.com/items/${this.itemId}`);
    // axios.delete(`http://localhost:8000/items/${this.itemId}`);
    this.$router.push('/items')
    }
  }
}
</script>
<style scoped>
.item-content {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  gap: 40px;
  align-items: center;
  margin: 20px;

}
.details {
  text-align: left;
}
h4 {
  margin: 0 auto;
}
.new {
  background-color: #a1a6c0;
  border-radius: 10px;
  border: 1px solid #07070b
}
.update {
  background-color: rgb(162, 219, 162);
  border-radius: 10px;
}
.delete {
  background-color: rgb(210, 155, 166);
  border-radius: 10px;
}
</style>