<script setup>
const items = defineProps({
  title: String,
  id: Number,
});
</script>
<template>
  <div
    class="rounded text-white text-center bg-zinc-900 w-60 cursor-pointer text-xl h-14 px-2 mt-2"
  > 
    <h1 class="text-wrap h-full break-after-all">
      {{ items.title }}
    </h1>
  </div>
</template>
