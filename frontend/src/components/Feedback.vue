<script setup>
import { ref, defineProps } from 'vue';
import vue3starRatings from "vue3-star-ratings";

const items = defineProps({
    name: String,
    data: String,
    text: String,
    rating: String,
})
</script>

<template>
    <div class="bg-zinc-900 mx-7 rounded-lg text-white p-5 mt-3 grid">
        <div class="flex grid-cols-12 grid-rows-1 justify-between">
            <div class="grid col-span-10">
                <div class="flex">
            <div class="ml-1 mt-1">
                <p class="text-xl text-main">{{ name }}</p>
                <p class="text-l text-zinc-600">{{ data }}</p>
            </div>
            </div>
            </div>
            <div class="col-span-2 text-right items-start" style="display: flex;">
                    <div class="block">
                        <vue3starRatings     
                            v-model="items.rating"
                            :starSize="22"
                            starColor="#00be73"
                            inactiveColor="#034844"
                            :numberOfStars="5"
                            :disableClick="true" 
                            class="flex-wrap"
                        />
                    </div>
                    <div class="text-l ml-2">
                        <b>
                            {{ rating }}
                        </b>
                    </div>
            </div>  
        </div>
        <div class="my-4 bg-white rounded-lg text-zinc-900 p-3">
            <p class="text-lg">{{ text }}</p>
        </div>
    </div>
</template>