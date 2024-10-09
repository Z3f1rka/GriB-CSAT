<script setup>
import { defineProps, ref } from 'vue';
import vue3starRatings from "vue3-star-ratings";

const items = defineProps({
    product_type: String,
})
const rating_1 = ref(0)
const rating_2 = ref(0)
const rating_3 = ref(0)
const rating_4 = ref(0)
</script>

<template>
    <div v-if="items.product_type == 1" class="bg-zinc-900 mx-7 rounded-t-lg text-white text-center p-3 grid grid-rows-2 grid-cols-2">
        <div>
            <p class="text-xl mt-2">Оценка за сам товар</p>
            <vue3starRatings     
                v-model="rating_1"
                :starSize="32"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-4"
            />
        </div>
        <div>
            <p class="text-xl mt-2">Качество упаковки</p>
            <vue3starRatings     
                v-model="rating_2"
                :starSize="32"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-4"
            />
        </div>
        <div>
            <p class="text-xl mt-2">Скорость доставки</p>
            <vue3starRatings     
                v-model="rating_3"
                :starSize="32"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-4"
            />
        </div>
        <div>
        <p class="text-xl mt-2">Взаимодействие с продавцом</p>
        <vue3starRatings     
                v-model="rating_4"
                :starSize="32"
                starColor="#00be73"
                inactiveColor="#034844"
                :numberOfStars="5"
                :disableClick="false" 
                class="inline-flex m-4"
            />
        </div>
    </div>
</template>