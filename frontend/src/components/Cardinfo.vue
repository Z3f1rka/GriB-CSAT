<script setup>
import { ref, defineProps } from "vue";
import vue3starRatings from "vue3-star-ratings";
import 'vue3-carousel/dist/carousel.css'
import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
import TheFeedback from "./TheFeedback.vue";
import Feedback from "./Feedback.vue";


const items = defineProps({
    ListImg: Array,
    title: String,
    vendor: String,
    characteristic: Array,
    description: String,
    feedback: Array,
    rating: String,
    len: Number,
    user_characteristic: Array,
    minrating: Object,
    maxrating: Object,
})

const modal1 = ref(false)
const show = ref(false)
const fb = ref(false)
</script>

<template>
    <div>
    <div class="grid grid-cols-2 grid-rows-1  mt-12 mx-5 ">
        <div class="p-6">
            <Carousel
                :items-to-show="1.5"
                :wrap-around="true"
            >
                <Slide v-for="img in ListImg" :key="img.id">
                    <div class="carousel__item">
                        <img 
                            class="bg-no-repeat bg-cover h-full rounded-lg"
                            style="aspect-ratio: 1 / 1;"
                            :src="img.img"
                        />
                    </div> 
                </Slide>
            <template #addons>
                <Navigation />
                <Pagination />
            </template>
            </Carousel>
        </div>
        <div class="mt-5">
            <p class="text-lg">{{ vendor }}</p>
            <p class="text-4xl mb-3">{{ title }}</p>
            <div class="flex">
                <div class="block">
            <vue3starRatings     
                v-model="items.rating"
                :starSize="32"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="true" 
                class="flex-wrap"
            /></div><div class="text-2xl ml-2 "><b>{{ rating }}</b></div></div>
            <div class="flex pt-3">
                <div class="block self-center">
            <vue3starRatings     
                v-model="items.minrating.count"
                :starSize="20"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="true" 
                class="flex-wrap"
            /></div><div class="text-xl ml-2 pb-1">{{ minrating.text }}</div></div>
            <div class="flex mt-1">
                <div class="block self-center">
            <vue3starRatings     
                v-model="items.maxrating.count"
                :starSize="20"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="true" 
                class="flex-wrap"
            /></div><div class="text-xl ml-2 pb-1 justify-start">{{ maxrating.text }}</div></div>
            <div class="flex mt-2">
                <div 
                    @click="show = false"
                    tabindex="1"
                    class="cursor-pointer des-button border-b mb-5 px-2 text-xl"
                >  
                        Описание    
                </div>
                <div 
                    @click="show = true"
                    tabindex="1"
                    class="cursor-pointer des-button border-b mb-5 px-2 w-full text-xl"
                >
                        Характеристика
                </div>
                </div>
                <div>
                <div
                    class="des-text text-2xl break-after-all" 
                    v-if="show == false">
                    <p>{{ description }}</p>
                </div>
                <div 
                    class="des-text text-2xl grid"
                    v-if="show == true">
                    <div v-for="item in characteristic" :key="item.id">
                        <p v-if="item.id < 11">
                            <b> - </b>
                            {{ item.text }}
                        </p>
                    </div>
                    <div @click="modal1 = true" v-if="len > 8" class="text-xl mt-2 border-2 py-2 px-3 cursor-pointer border-zinc-500 bg-secondary text-main rounded-lg select-none" style="width: 320px;">
                        Показать все характеристики
                    </div>
                    <Teleport v-if="modal1 == true" to="#teleport-target">
                    <div class="modal text-center rounded-lg p-9 grid border-4 border-secondary">
                        <p class="text-2xl mb-3">Все характеристики</p>
                        <div v-for="item in characteristic" :key="item.id" class="text-start text-xl my-1 break-before-all">
                        <p>
                            {{ item.text }}
                        </p>
                        </div>
                        <div @click="modal1 = false" class="border-2 cursor-pointer text-xl self-center py-1 px-7 rounded-lg bg-secondary text-main align-bottom mt-5" style="display: inline-flex;">закрыть</div>
                    </div>
                </Teleport>
                </div>
            </div>
        </div>
    </div>
    <div class="text-center">
        <p class="text-2xl mx-7 pr-12 mb-3 border-b-2 border-zinc-900 text-right">Отзыв</p>
        <div class="bg-zinc-900 mx-7 rounded-lg inline-block" style="width: 77.2%;">
        <div v-if="fb == false" @click="fb = true" class="rounded-lg text-main text-center text-xl p-2 mx-7 bg-zinc-900 cursor-pointer">
            Оставить отзыв
        </div>
        <div v-if="fb == true" @click="fb = true" class="rounded-lg text-center text-xl p-2 mx-7 bg-zinc-900 text-zinc-900 select-none">
            Оставить отзыв
        </div>
        <div class="grid grid-cols-7">
        <transition>
        <TheFeedback v-if="fb" class="col-span-3" :characteristic="user_characteristic" />
        </transition>
        <transition>
            <div v-if="fb" class="text-center px-5 mt-4 col-span-4">
                <textarea class="rounded-lg w-full resize-none p-1 text-lg" style="height: 83%;" placeholder="Ваш отзыв..."></textarea>
            </div>
        </transition>
        <transition name="fake">
            <div v-if="fb" class="text-white grid bg-main rounded-lg py-2 col-span-3 col-start-3 cursor-pointer text-lg">Отправить</div>
        </transition>
        </div>
        <transition>
        <div v-if="fb" @click="fb = false" class="rounded-b-lg text-main text-center text-2xl p-2 pt-4 mx-7 cursor-pointer border-2 border-zinc-900 bg-zinc-900">
            ^
        </div>
        </transition>
        </div>
        <div class="w-4/5 inline-block">
        <Feedback 
            v-for="item in feedback" 
            class="text-left"
            :key="item.user_id" 
            :text="item.text"
            :data="item.data"
            :name="item.name"
            :rating="item.rating"
        />
        <br>
        </div>
    </div>
</div>
</template>
<style scoped>

/*
.ImageAnimation:hover {
    animation-name: CardButton;
    animation-duration: 0.5s;
}
*/
.modal {
  display: block;
  position: fixed;
  z-index: 999;
  left: 35%;
  top: 25%;
  align-self: right;
  width: 30%;
  height: 50%;
  overflow: auto;
  text-align: center;
  background-color: white;
}
.v-enter-active {
    background-color: #18181B;
    animation: added 0.5s;
}
.v-leave-active {
  background-color: #18181B;
  animation: added 0.3s reverse;
}
.fade-leave-active {
    background-color: #18181B;
    animation: added 0.5s;
}
.fade-enter-active {
  background-color: #18181B;
  animation: added 0.5s reverse;
}
.fake-leave-active {
    animation: added 0.5 reverse;
}
.fake-enter-active {
  animation: added 0.5s;
}
@keyframes added {
from {
  opacity: 0;
  translate: 0 -60px;
}
to {
  opacity: 1;
  translate: 0 0px;
}
}
.des-button {
    color: #044443;
    border-bottom-color: #044443;
}
.char-button {
    color: #044443;
    border-bottom-color: #044443;
}
.char-focus {
    color: #00BC72;
    border-bottom-color: #00BC72;
}
.des-button:hover {
    color: #00BC72;
    border-bottom-color: #00BC72;
}
.des-button:focus {
    color: #00BC72;
    border-bottom-color: #00BC72;
}
.des-text {
    animation-duration: 0.5s;
    animation-name: slidein;
}
@keyframes slidein {
  from {
    margin-left: 50%;
    width: 300%;
  }

  to {
    margin-left: 0%;
    width: 100%;
  }
}
@keyframes descript {
    from {
        color: #044443;
        border-bottom-color: #044443;
    }
    to {
        color: #00BC72;
        border-bottom-color: #00BC72;        
    }
};
</style>