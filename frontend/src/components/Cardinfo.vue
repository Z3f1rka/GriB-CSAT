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
    characteristic: String,
    description: String,
    product_type: String,
    feedback: Array,
    rating: String,
})

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
            <p class="text-2xl mb-3">{{ title }}</p>
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
            <div class="flex mt-7">
                <div 
                    @click="show = false"
                    class="cursor-pointer des-button border-b mb-5 px-2 text-xl"
                >  
                        Описание    
                </div>
                <div 
                    @click="show = true"
                    class="cursor-pointer des-button border-b mb-5 px-2 w-full text-xl"
                >
                        Характеристика
                </div>
                </div>
                <div>
                <div
                    class="des-text text-2xl" 
                    v-if="show == false">
                    <p>{{ description }}</p>
                </div>
                <div 
                    class="des-text text-2xl"
                    v-if="show == true">
                    <p>{{ characteristic }}</p>
                </div>
            </div>
        </div>
    </div>
    <div class="text-right">
        <p class="text-2xl mx-7 mb-3 border-b-2 border-zinc-900">Отзыв</p>
        <div class="bg-zinc-900 mx-7 rounded-lg">
        <div v-if="fb == false" @click="fb = true" class="rounded-lg text-main text-center text-xl p-2 mx-7 bg-zinc-900 cursor-pointer">
            Оставить отзыв
        </div>
        <div v-if="fb == true" @click="fb = true" class="rounded-lg text-center text-xl p-2 mx-7 bg-zinc-900 text-zinc-900 select-none">
            Оставить отзыв
        </div>
        <transition>
        <TheFeedback v-if="fb" :product_type="product_type" />
        </transition>
        <transition>
        <div v-if="fb" @click="fb = false" class="rounded-b-lg text-main text-center text-2xl p-2 pt-4 mx-7 cursor-pointer border-2 border-zinc-900 bg-zinc-900">
            ^
        </div>
        </transition>
        </div>
        <Feedback 
            v-for="item in feedback" 
            class="text-left"
            :key="item.user_id" 
            :img="item.img"
            :text="item.text"
            :data="item.data"
            :name="item.name"
            :rating="item.rating"
        />
        <br>
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