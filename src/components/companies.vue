<template>
<div class="ctn-1 " role="tablist">
    <!-- COMPANY 1 -->
    <div style="margin-right: 5%;">
    <div class="card mb-1" style="width: 600px">
        <div class="row no-gutters">
            <div class="col-md-4">
                <img src="../assets/company-bethesda.png" class="card-img" style="width: 90%; margin-top: 20px;">
            </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title">Epic Games</h5>
                    <p class="card-text" style="margin-top: -10px;"><small class="text-muted">Popularity</small></p>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item" style="padding-top: 0;">
                            Positive
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 30%; background-color: #81cc00" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </li>
                        <li class="list-group-item" style="padding-top: 0;">
                            Negative
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 60%; background-color: #ff0b11" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </li>
                        <li class="list-group-item" style="padding-top: 0;">
                            Neutral
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 10%; background-color: #89999f" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </li>
                    </ul>
                    <button style="margin-top: 10px;" @click="showCol(0)">Show games</button>
                </div>
            </div>
        </div>
        
    </div>
    <b-collapse id="collapse-1" v-model="companies[0]" class="mt-4">
            <!-- GAME 1-->
            <div class="card card-body" style="width: inherit; margin-bottom: 0px;">
                <div style=" height: 50px; display: flex;">
                    <h5>1</h5>
                    <img src="../assets/company-game-fallout76.jpg" class="card-img rounded" style="width: 50px; height: 50px; margin-left: 20px;"> 
                    <div style="margin-left: 20px;">
                        <p style="font: 18px Arial; font-weight: bold;">Games Name 1</p>
                        <p style="font: 15px bold Arial; margin-top: -10px;">Platforms</p>
                    </div>
                    <div style="display: flex; margin-left: 20px; text-align: center; margin-top: 3px;">
                        <div style="width: 60px; margin-right: 25px; ">
                            <p style="font: 15px Arial; font-weight: bold;">Positive</p>
                            <p style="margin-top: -10px;">30%</p>
                        </div>
                        <div style="width: 70px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Negative</p>
                            <p style="margin-top: -10px;">60%</p>
                        </div>
                        <div style="width: 60px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Neutral</p>
                            <p style="margin-top: -10px;">10%</p>
                        </div>
                    </div>
                    <button class="btn btn-light hashtag">
                     #
                    <img src="../assets/icon-twitter.png" width="25px;">
                </button>
                </div>
            </div>
            <!-- GAME 2-->
            <div class="card card-body" style="width: inherit;">
                <div style=" height: 50px; display: flex;">
                    <h5>2</h5>
                    <img src="../assets/company-game-fallout76.jpg" class="card-img rounded" style="width: 50px; height: 50px; margin-left: 20px;"> 
                    <div style="margin-left: 20px;">
                        <p style="font: 18px Arial; font-weight: bold;">Games Name 2</p>
                        <p style="font: 15px bold Arial; margin-top: -10px;">Platforms</p>
                    </div>
                    <div style="display: flex; margin-left: 20px; text-align: center; margin-top: 3px;">
                        <div style="width: 60px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Positive</p>
                            <p style="margin-top: -10px;">60%</p>
                        </div>
                        <div style="width: 70px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Negative</p>
                            <p style="margin-top: -10px;">30%</p>
                        </div>
                        <div style="width: 60px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Neutral</p>
                            <p style="margin-top: -10px;">10%</p>
                        </div>
                    </div>
                    <button class="btn btn-light hashtag">
                     #
                    <img src="../assets/icon-twitter.png" width="25px;">
                </button>
                </div>
            </div>
    </b-collapse>
    </div>
    <!-- COMPANY 2 -->
    <div style="margin-right: 5%;">
    <div class="card mb-1" style="width: 600px;">
        <div class="row no-gutters">
            <div class="col-md-4">
                <img src="../assets/company-bethesda.png" class="card-img" style="width: 90%; margin-top: 20px;">
            </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h5 class="card-title" >Epic Games</h5>
                    <p class="card-text" style="margin-top: -10px;"><small class="text-muted">Popularity</small></p>
                    <ul class="list-group list-group-flush">
                        <li class="list-group-item" style="padding-top: 0px;">
                            Positive
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 30%; background-color: #81cc00" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </li>
                        <li class="list-group-item" style="padding-top: 0px;">
                            Negative
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 60%; background-color: #ff0b11" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </li>
                        <li class="list-group-item" style="padding-top: 0px;">
                            Neutral
                            <div class="progress">
                                <div class="progress-bar" role="progressbar" style="width: 10%; background-color: #89999f" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100"></div>
                            </div>
                        </li>
                    </ul>
                    <button style="margin-top: 10px;" @click="showCol(1)">Show games</button>
                </div>
            </div>
        </div>
    </div>
    <b-collapse id="collapse-2" v-model="companies[1]" class="mt-2">
            <!-- GAME 1-->
            <div class="card card-body" style="width: inherit; margin-bottom: 0px;">
                <div style=" height: 50px; display: flex;">
                    <h5>1</h5>
                    <img src="../assets/company-game-fallout76.jpg" class="card-img rounded" style="width: 50px; height: 50px; margin-left: 20px;"> 
                    <div style="margin-left: 20px;">
                        <p style="font: 18px Arial; font-weight: bold;">Games Name 1</p>
                        <p style="font: 15px bold Arial; margin-top: -10px;">Platforms</p>
                    </div>
                    <div style="display: flex; margin-left: 20px; text-align: center; margin-top: 3px;">
                        <div style="width: 60px; margin-right: 25px; ">
                            <p style="font: 15px Arial; font-weight: bold;">Positive</p>
                            <p style="margin-top: -10px;">30%</p>
                        </div>
                        <div style="width: 70px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Negative</p>
                            <p style="margin-top: -10px;">60%</p>
                        </div>
                        <div style="width: 60px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Neutral</p>
                            <p style="margin-top: -10px;">10%</p>
                        </div>
                    </div>
                    <button class="btn btn-light hashtag">
                     #
                    <img src="../assets/icon-twitter.png" width="25px;">
                </button>
                </div>
            </div>
            <!-- GAME 2-->
            <div class="card card-body" style="width: inherit;">
                <div style=" height: 50px; display: flex;">
                    <h5>2</h5>
                    <img src="../assets/company-game-fallout76.jpg" class="card-img rounded" style="width: 50px; height: 50px; margin-left: 20px;"> 
                    <div style="margin-left: 20px;">
                        <p style="font: 18px Arial; font-weight: bold;">Games Name 2</p>
                        <p style="font: 15px bold Arial; margin-top: -10px;">Platforms</p>
                    </div>
                    <div style="display: flex; margin-left: 20px; text-align: center; margin-top: 3px;">
                        <div style="width: 60px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Positive</p>
                            <p style="margin-top: -10px;">60%</p>
                        </div>
                        <div style="width: 70px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Negative</p>
                            <p style="margin-top: -10px;">30%</p>
                        </div>
                        <div style="width: 60px; margin-right: 25px;">
                            <p style="font: 15px Arial; font-weight: bold;">Neutral</p>
                            <p style="margin-top: -10px;">10%</p>
                        </div>
                    </div>
                    <button class="btn btn-light hashtag">
                     #
                    <img src="../assets/icon-twitter.png" width="25px;">
                </button>
                </div>
            </div>
        </b-collapse>
    </div>
</div>   
</template>

<script>
export default {
    data() {
        return {
            companies: {
                showCompanies1Games: false,
                showCompanies2Games: false
            }
            
        }
    },
    methods: {
        showCol(index){
            if(this.companies[index]){
                this.companies[index] = false;
            }else{
                this.companies[index] = true;
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
.hashtag{
    width: 70px; 
    margin-right: 5px;
    position: absolute;
    right: 0;

}
</style>

