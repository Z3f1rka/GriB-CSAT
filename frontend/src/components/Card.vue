<script setup>
defineProps({
    title: String,
    img: String,
    id: Number,
})

</script>

<template>
    <div class="grid grid-rows-5 grid-cols-1 m-5" style="width: 320px;">
        <span class="grid row-span-4 bg-no-repeat bg-cover">
        </span>
        <div class="grid row-span-1 grid-cols-4 bg-black py-3 px-5">
            <div class="grid col-span-3" style="color: white; font-size: 15px;">
                {{ title }}
            </div>
            <div class="grid col-span-1 bg-secondary align-middle text-justify text-main" style="aspect-ratio: 1 / 1; width: 90%; display: flex; justify-self: flex-end; justify-content: center; align-items: center; font-size: 30px;">🠖{{ id }}</div>
        </div>
    </div>
</template>
