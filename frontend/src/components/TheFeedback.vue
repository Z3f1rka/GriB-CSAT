<script setup>
import { ref } from "vue";
import { z } from "zod";
import router from "../router";
import { auth_get, auth_post } from "../requests";
import vue3starRatings from "vue3-star-ratings";

const items = defineProps({
    characteristic: Array,
    id: String,
})
var rating_1 = ref(0)
var rating_2 = ref(0)
var rating_3 = ref(0)
var text = ref("")
var err_text = ref("")
var ListStars = ref([])
var CardList = ref([])


function submit(){
    if (rating_1 != 0){
        ListStars.value.push({ rating: rating_1.value, criterion: items.characteristic[0] })
    }
    if (rating_2 != 0){
        ListStars.value.push({ rating: rating_2.value, criterion: items.characteristic[1] })
    }
    if (rating_3 != 0){
        ListStars.value.push({ rating: rating_3.value, criterion: items.characteristic[2] })
    }
    for (let el of ListStars.value){
        console.log(el) /* all rating */
    }
    console.log({
      feedback: { text: text.value, product_id:items.id },
      rating: ListStars._rawValue,
    })
    var resp_data = auth_post('/api/feedback/add', {
      feedback: { text: text.value, product_id:Number(items.id) },
      rating: ListStars._rawValue
    });
    if (resp_data) {
      router.push("/");
    }
}
</script>

<template>
    <div class="grid grid-cols-7">
    <div class="bg-zinc-900 ml-7 rounded-t-lg text-white text-center col-span-3 p-3 grid grid-cols-2 align-middle">
        <div class="text-left">
            <p class="text-xl mb-4 mt-2 mx-2">{{ characteristic[0] }}</p>
            <p class="text-xl m-4 mx-2">{{ characteristic[1] }}</p>
            <p class="text-xl m-4  mx-2">{{ characteristic[2] }}</p>
        </div>
        <div class="text-right">
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
                v-model="rating_2"
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
    <div class="text-center px-5 mt-4 col-span-4">
                <textarea class="rounded-lg w-full resize-none p-1 text-lg" style="height: 83%;" placeholder="Ваш отзыв..." v-model="text"></textarea>
            </div>
            <div @click="submit" class="text-white grid bg-main rounded-lg py-2 col-span-3 col-start-3 cursor-pointer text-lg">Отправить</div>

</div>
</template>