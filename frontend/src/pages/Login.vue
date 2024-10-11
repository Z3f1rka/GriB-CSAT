<script setup>
import LoginForm from "../components/LoginForm.vue";
import Header from "../components/Header.vue";
</script>

<template>
  <div><Header></Header>
  <div class="grid grid-cols-6 grid-rows-1 mt-10">
    <h1 class="text-4xl text-center col-start-2 col-span-4 mb-10">Вход</h1>
    <div class="w-full col-span-4 col-start-2">
      <LoginForm></LoginForm>
    </div>
  </div></div>
</template>
