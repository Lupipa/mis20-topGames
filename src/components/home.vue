<template>
    <div>    
      <div style="height: 170px; text-align: center; background-color: #6D829E;" :style="{ backgroundColor: color}">
        <div class="tittle">
        <h1 style="font: 50px Arial; font-weight: bold; margin-top: 8px;">TOP GAMES</h1>
        </div>
        <div class="logo">
          <img src="../assets/bot-twitter.png" class="card-img" style="width: 90%; margin-top: 20px;">
        </div>
      </div>
      <nav class="sticky-top" style="width: 60%; margin-left: auto; margin-right: auto; border-radius: 0 0 20px 20px;">
        <ul class="nav nav-tabs justify-content-center" style="border-radius: 0 0 20px 20px;" :style="{ backgroundColor: color}">
            <li class="nav-item" style="width: 33.3%;  margin-left: -1px; text-align: center;">
              <a class="nav-link" :class="{ active: games }" style="font: 150% Ubuntu; cursor: pointer" :style="{ color: games ? 'black' : 'white' }" @click="goTo('games')">games</a>
            </li>
            <li class="nav-item" style="width: 33.3%; text-align: center; cursor: pointer">
              <a class="nav-link" :class="{ active: companies }" style="font: 150% Ubuntu;" :style="{ color: companies ? 'black' : 'white' }" @click="goTo('companies')">Companies</a>
            </li>
            <li class="nav-item" style="width: 33.3%; margin-left: 1px; text-align: center; cursor: pointer;">
              <a class="nav-link" :class="{ active: wit }" style="font: 150% Ubuntu;" :style="{ color: wit ? 'black' : 'white' }" @click="goTo('wit')">Support</a>
            </li>
        </ul>
      </nav>
      
      <gamesPage v-if="games"></gamesPage>
      <companiesPage v-if="companies"></companiesPage>
      <whatIsThisPage v-if="wit"></whatIsThisPage>
    </div>
</template>

<script>
import GamesPage from './games.vue'
import CompaniesPage from './companies.vue'
import WhatIsThisPage from './whatIsThis.vue'
import Tweet from 'vue-tweet-embed/src/tweet'
import Moment from 'vue-tweet-embed/src/moment'
import Timeline from 'vue-tweet-embed/src/timeline'

export default {
    components: { gamesPage: GamesPage, companiesPage: CompaniesPage, whatIsThisPage: WhatIsThisPage, Tweet: Tweet, Timeline: Timeline, Moment: Moment },
    data () {
      return {
        games: true, 
        companies: false,
        wit: false,
        color: '#6D829E'
      }
    },
    methods: {
      goTo(page){
        console.log(this.color)
        if(page == 'games'){
          this.color = '#6D829E'
          this.games = true; this.companies = false; this.wit = false;
        }else if(page == 'companies'){
          this.color = '#6D939E'
          this.games = false; this.companies = true; this.wit = false;
        }else if(page == 'wit'){
          this.color = '#6D749E'
          this.games = false; this.companies = false; this.wit = true;
        }
      },
      showMoreInf(){
            this.popOut = true;
      }
    }
}
</script>
<style scoped>
.tittle{
  width: 50%; 
  height: 70px;
  border-radius: 100px;
  border-width: 3px;
  border-style: solid;
  border-color: white;
  margin-left: auto; 
  margin-right: auto; 
  margin-top: 30px; 
  text-align: center; 
  background-color: rgb(86, 201, 195);
  position: absolute;
  left: 0;
  right: 0;
}
.twitterIframe{
  width: 300px; 
  margin-right: 20px;
  position: absolute;
  right: 0;
}
.logo{
  height: 150px; 
  width: 200px;
  position: absolute;
  right: 0;
  margin-right: -30px;
  margin-top: 30px;
  z-index: 0;
}
.nav-link.active{
  border-radius: 0 0 20px 20px;
}
</style>
