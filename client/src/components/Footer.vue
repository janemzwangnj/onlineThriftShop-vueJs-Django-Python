<template>
  <div class="footer">
    <div>
    <img alt="Vue logo" src="../../../images/vue.png">
    <img alt="Python3 logo" src="../../../images/python3.png">
    <img alt="Django logo" src="../../../images/restframework.png">
    <img alt="PostgreSql logo" src="../../../images/postgres.png">
    </div><div>
   <a href="https://github.com/janemzwangnj/onlineThriftShop"> <img alt="Github" src="../../../images/github.png"></a>
   <a href="https://www.linkedin.com/in/janemzwangnj/"> <img alt="Linkedin" src="../../../images/linkedin.png"></a>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>

.footer {
  background: #8bbba5;
  display: flex;
  justify-content: space-evenly;
  align-items:flex-end;
  padding: 0.2em;
}

</style>
