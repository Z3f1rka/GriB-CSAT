<script setup>
import CardForm from "../components/CardForm.vue";
</script>

<template>
  <div class="grid grid-cols-6 grid-rows-1 mt-10">
    <h1 class="text-4xl text-center col-start-2 col-span-4 mb-10">Создание товара</h1>
    <div class="w-full col-span-4 col-start-2">
      <CardForm></CardForm>
    </div>
  </div>
</template>