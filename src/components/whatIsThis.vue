<template>
<div class="ctn-1">
    <div>
        <div class="card mb-1" style="width: 600px;">
            <div class="row no-gutters">
                <div class="col-md-4" style="height: 250px; text-align: center;">
                    <img src="../assets/python-logo.png" class="card-img" style="height: 80%; width: auto; margin-top: 20px;">
                </div>
                <div class="col-md-8" style="width: 600px;">
                    <div class="card-body">
                        <h5 class="card-title">Made with Python</h5>
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="card mb-1" style="width: 600px; margin-top: 30px;">
            <div class="row no-gutters">
                <div class="col-md-4" style="height: 250px; text-align: center;">
                    <img src="../assets/twitter-dev.png" class="card-img" style="height: 80%; width: auto; margin-top: 20px;">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Made with Twitter Developers</h5>
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
                </div>
            </div>
        </div>
        <div class="card mb-1" style="width: 600px; margin-top: 30px;">
            <div class="row no-gutters">
                <div class="col-md-4" style="height: 250px; text-align: center;">
                    <img src="../assets/machine-learning.png" class="card-img" style="height: 80%; width: auto; margin-top: 20px;">
                </div>
                <div class="col-md-8">
                    <div class="card-body">
                        <h5 class="card-title">Using machine lerning</h5>
                        <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div class="card text-center" style="width: 700px; height: 100%; margin-left: 2%;">
        <div class="card-header">
            <ul class="nav nav-tabs card-header-tabs">
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: general }" style="cursor: pointer;" @click="showInf('general')">General Information</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link" :class="{ active: cards }" style="cursor: pointer;" @click="showInf('cards')">How it works</a>
                </li>
            </ul>
        </div>
        <div v-if="general" class="card-body">
            <img src="../assets/welcome.jpg" class="img-fluid">
            <p class="card-text" style="margin-top: 30px;"> 
                {{ textoGeneral[0] }} <br>
                {{ textoGeneral[1] }}
            </p>
            <br>
            <img src="../assets/menu.jpg" class="img-fluid">
            <p class="card-text" style="margin-top: 20px;"> {{ textoGeneralMenu[0] }} </p>
            <p class="card-text"> {{ textoGeneralMenu[1] }} </p>
            <p class="card-text"> {{ textoGeneralMenu[2] }} </p>
            <p class="card-text"> {{ textoGeneralMenu[3] }} </p>
            <p class="card-text"> 
                {{ textoGeneralMenu[4] }}<br>
                {{ textoGeneralMenu[5] }} 
            </p>
            <p class="card-text"> {{ textoGeneralMenu[6] }} </p>
            <p class="card-text"> {{ textoGeneralMenu[7] }} </p>
        </div>
        <div v-if="cards" class="card-body">
            <img src="../assets/cards.jpg" class="img-fluid">
            <h5 class="card-title" style="margin-top: 30px;">Cards</h5>
            <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
        </div>
    </div>
</div>
</template>

<script>
export default {
    data(){
        return {
            general: true,
            cards: false,
            textoGeneral: [
                'Es el proyecto de la Asignatura de MIS 2.0.',
                'Pensamos en crear una herramienta para ayudar a los gamers a tomar la dura decision de comprar un videojuego.',          
                ''
            ],
            textoGeneralMenu: [
                'Top Games consta de 3 vistas.',
                'Games',
                'En esta vista se muestran cartas de los videojuegos que están por salir.',
                'Companies',
                'En esta vista se visualizan las comapñías y su reputación. Esta reputación es la media de la reputación de todos sus juegos*.',
                '* Se tendrán en cuenta los juegos analizados via análisis de sentimientos.',
                'What Is This',
                'En esta vista se muestra información relativa a las herramientas usadas en el proyecto así como este escueto tutorial.'
            ]
        }
    },
    methods:{
        showInf(text){
            if(text == "general"){
                this.general = true,
                this.cards = false
            }else{
                this.cards = true,
                this.general = false
            }
        }
    }
}
</script>

<style scoped>
.ctn-1{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    
    margin-top: 60px;
}
</style>