<template>
<div><!-- The launh date has to be passed by paramenter by server -->
    <div class="twitterIframe"> 
        <Timeline id="top_mes" sourceType="profile" :options="{ tweetLimit: '15' }"/>
    </div>
    <div class="card" style="margin-top: 20px; width: 70%; margin-left: auto; margin-right: auto; text-align: center;">
        <div class="card-body" style="font: 25px Arial;">
            Games that will be launched in June 2019
        </div>
    </div>
    <div v-if="server" class="flex-row-ctn" style="width: 80%;">
        <div class="card flex-row-item" style="width: 250px;" v-for="(game, index) in games" :key="index">
            <template>
            <b-carousel :id="String(index)" v-model="slide[index]" :interval="0" fade indicators img-height="250" style="text-align: center;" @sliding-start="onSlideStart(index)" @sliding-end="onSlideEnd(index)">
                <b-carousel-slide>
                    <img slot="img" src="../assets/game-card.png" style="height: 248px; width: inherit;">
                </b-carousel-slide>
                <b-carousel-slide img-blank img-blank-color="black">
                    <div style="margin-bottom: 4px;">
                        <div>
                            <h5>Number of Tweets</h5>
                            <p style="margin-bottom: 0px;"> Positive tweets: {{ game.positive.totalTweets }}</p>
                            <p style="margin-bottom: 0px;"> Negative tweets: {{ game.negative.totalTweets }}</p>
                            <p style="margin-bottom: 0px;"> Neutral tweets: {{ game.neutral.totalTweets }}</p>
                        </div>
                        <div style="margin-top: 20px;">
                            <h5> Release date: 15/06/19</h5>
                        </div>    
                    </div>
                </b-carousel-slide>
            </b-carousel>
            <div class="card-body game-name"><h5>{{ game.name }}</h5></div>
            <ul class="list-group list-group-flush">
                <li class="list-group-item" style="height: 60px; padding-top: 5px;">
                    Positive
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="background-color: #81cc00" :style="{width: game.positive.percentage}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </li>
                <li class="list-group-item" style="height: 60px; padding-top: 5px;">
                    Negative
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="background-color: #ff0b11" :style="{width: game.negative.percentage}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </li>
                <li class="list-group-item" style="height: 60px; padding-top: 5px;">
                    Neutral
                    <div class="progress">
                        <div class="progress-bar" role="progressbar" style="background-color: #89999f" :style="{width: game.neutral.percentage}" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                    </div>
                </li>
            </ul>
            <div class="card-body" style="height: 50px; text-align: center; padding-top: 5px;">
                <button class="btn btn-light" @click="goToTwitter(index)">
                    Hashtag
                    <img src="../assets/icon-twitter.png" width="25px;">
                </button>
            </div>
            </template>
        </div>
    </div>
    <div v-else class="card" style="margin-top: 20px; width: 70%; margin-left: auto; margin-right: auto; text-align: center;">
    <div class="card-body" style="font: 25px Arial;">
        The server does not response
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';
import Tweet from 'vue-tweet-embed/src/tweet'
import Moment from 'vue-tweet-embed/src/moment'
import Timeline from 'vue-tweet-embed/src/timeline'

export default {
        components: {Tweet: Tweet, Timeline: Timeline, Moment: Moment },

    data(){
        return{
            server: false,
            games: [],
            slide: [0, 0, 0, 0, 0],
            sliding: [null, null, null, null, null]
        }
    },
    methods: {
        onSlideStart(i) {
            this.sliding[i] = true
        },
        onSlideEnd(i) {
            this.sliding[i] = false
        },
        getGames(){
            axios.get("http://127.0.0.1:5000/games").then(response => {
                this.games = response.data.games
                this.server = true;
            }) .catch (error => {
                this.server = false;
                console.error(error)
            })
        },
        goToTwitter(i){
            var aux = this.games[i].name.replace(/\s+/g,'');
            window.open("https://twitter.com/search?q=%23"+aux+"&src=typd", "_blank"); 
        }
    },
    created() {
        this.getGames();
    }
}
</script>
<style scoped>
.flex-row-ctn{
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;

    margin-top: 50px;
}
.flex-row-ctn{
    flex-grow: 1;
    flex: 1 1 30%;
}
.flex-row-item{
    width: 400px;

    margin-right: 2%;
    margin-bottom: 40px;
}
.game-name{
    margin-top: -5px;
    text-align: center;
}
.twitterIframe{
  width: 20%;
  height: 100%; 
  margin-right: 20px;
  margin-top: 100px;
  position: absolute;
  right: 0;
  overflow: scroll;
}
</style>
