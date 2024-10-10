<script setup>
import { defineProps, ref } from 'vue';
import vue3starRatings from "vue3-star-ratings";

const items = defineProps({
    characteristic: Array,
})
const rating_1 = ref(0)
const rating_2 = ref(0)
const rating_3 = ref(0)
</script>

<template>
    <div class="bg-zinc-900 ml-7 rounded-t-lg text-white text-center p-3 grid grid-cols-2 align-middle">
        <div class="text-left">
            <p class="text-xl mb-4 mt-2 mx-2">{{ characteristic[0] }}</p>
            <p class="text-xl m-4 mx-2">{{ characteristic[1] }}</p>
            <p class="text-xl m-4  mx-2">{{ characteristic[2] }}</p>
        </div>
        <div class="text-right">
            <vue3starRatings     
                v-model="rating_2"
                :starSize="28"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-2"
            />
            <vue3starRatings     
                v-model="rating_1"
                :starSize="28"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-2"
            />
            <vue3starRatings     
                v-model="rating_3"
                :starSize="28"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-2"
            />
        </div>
    </div>
</template>