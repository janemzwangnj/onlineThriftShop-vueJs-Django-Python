<template>
  <div class="item-content" v-if="itemView">
    <section class="image-container">
      <div>
        <img :src="itemView.image" width="300" height="200" />
      </div>
    </section>
    <section class="details">
        <strong>{{itemView.name}}</strong> <br>
        <strong>Asking Price: </strong>{{itemView.asking_price}} <br>
        <strong>Condition: </strong>{{itemView.condition}} <br>
        <strong>Origin Purchasing Date: </strong>{{itemView.origin_purchasing_time}}<br>
        <strong>Origin Price: </strong>{{itemView.origin_price}}<br>
        <div v-if="itemView.sold_mark">
            <strong>Sold: [ ✔️ ]</strong> 
        </div>
        <div v-else>
          <strong>Sold: [ x ]</strong> 
        </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ItemView',
  data: () => ({
    itemView: null
  }),
  mounted() {
    this.getItemView()
  },
  methods: {
    async getItemView() {   
      const itemId = this.$route.params.item_id
      const res = await axios.get(`http://localhost:8000/items/${itemId}`)
      this.itemView = res.data
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
h4 {
  margin: 0 auto;
}
</style>