<script setup>
defineProps({
    title: String,
    img: String,
    id: Number,
})
function Rout(id){
    console.log(id)
}
</script>
<template>
    <div @click="Rout(id)" class="grid grid-rows-5 grid-cols-1 m-5 cursor-pointer cardsize">
        <span class="grid row-span-4">
            <img 
                class="bg-no-repeat bg-cover h-full"
                style="aspect-ratio: 1 / 1;"
                :src="img"
            />
        </span>
        <div class="grid row-span-1 grid-cols-4 bg-black py-3 px-5">
            <div class="grid col-span-3 text-white text-xm" >
                <p class="">{{ title }}</p>
            </div>
            <div class="grid col-span-1 bg-secondary align-middle text-justify text-main arrow justify-self-end justify-center items-center" style="aspect-ratio: 1 / 1;">
                🠖
            </div>
        </div>
    </div>
</template>
<style scoped>
.cardsize {
    width: 320px;
}
.arrow {
    width: 90%;
    font-size: 30px;
}
p {
  line-height: 20px;
  -webkit-box-orient: vertical;
  display: block;
  display: -webkit-box;
  overflow: hidden!important;
  text-overflow: ellipsis;
  -webkit-line-clamp: 3;
}
</style>