<template>
  <div class="form-container">
    <form v-on:submit="handleSubmit">
      <input
        @input="handleChange"
        placeholder="user_id"
        :value="user_id"
        name="user_id"
        type="user_id"
      />
      <input
        @input="handleChange"
        placeholder="Name"
        :value="name"
        name="name"
        type="name"
      />
      <input
        @input="handleChange"
        placeholder="Asking Price"
        :value="asking_price"
        name="asking_price"
        type="asking_price"
      />
      <input
        @input="handleChange"
        placeholder="Condition"
        :value="condition"
        name="condition"
        type="condition"
      />
      <input
        @input="handleChange"
        placeholder="Origin Purchasing Date"
        :value="origin_purchasing_time"
        name="origin_purchasing_time"
        type="origin_purchasing_time"
      />
      <input
        @input="handleChange"
        placeholder="Origin Price"
        :value="origin_price"
        name="origin_price"
        type="origin_price"
      />
      <input
        @input="handleChange"
        placeholder="Image"
        :value="image"
        name="image"
        type="image_link"
      />
      <button :disabled="!name || !asking_price">Add</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'AddItem',
  data: ()=>({
      user_id: 0,
      name: "",
      asking_price: "",
      condition: "",
      origin_purchasing_time:"",
      origin_price: "",
      image:""
  }) ,
  methods: {
    handleChange(e) {
      this[e.target.name] = e.target.value
    },
    handleSubmit(e) {
      e.preventDefault()
      let item = {"user_id":this.user_id,"name":this.name,"asking_price":this.asking_price,
      "condition":this.condition, "origin_purchasing_time":this.origin_purchasing_time,
      "origin_price":this.origin_price,"image":this.image}
      axios.post('https://mysterious-lake-42419.herokuapp.com/items/', item);
      this.user_id= 0;
      this.name= "";
      this.asking_price= "";
      this.condition= "";
      this.origin_purchasing_time="";
      this.origin_price= "";
      this.image="";
      this.$router.push('/items')
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
  background-color: #71c29e;
  border: none;
  font-weight: 700;
}

button:disabled {
  cursor: auto;
  background-color: #76d2a9;
  color: #3d4c98;
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