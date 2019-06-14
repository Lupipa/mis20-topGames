<template>
    <div class = "wp">
        <img src="../assets/bot-twitter.png" style="width: 20%; height: 50%;">
        <div style="text-align: center;">
            <h1> Bienvenido a </h1>
            <h2>Top Games</h2>
        </div>
        <div>
            <button type="button" class="btn btn-primary" @click="goToHomePage"> acceder </button>  
        </div>
    </div>
</template>

<script>
export default {
    methods: {
     goToHomePage: function(){
       this.$router.push('/home');
     }
   }
}
</script>

<style scoped>
.wp {
    text-align: center;
    color: #2c3e50;
    margin-top: 2%;
}
h1{
  margin-top: 20px; 
  font: 50px Arial; 
  font-weight: normal;
}
h2{
  font: 100px Arial; 
  font-weight: bold;
}
.btn {
  height: 50%; 
  width: 20%; 
  margin-top: 30px; 
  border-radius: 50px; 
  font: 30px Arial;
}
</style>
