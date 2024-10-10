<script setup>

import { onMounted, ref } from 'vue';

let isAuth = ref(false)
function logout(){  
  localStorage.removeItem('refresh_token');
  isAuth.value = false
}
function Auth(){
  if (localStorage.getItem('refresh_token')){
    isAuth.value = true
  }
  else {
    isAuth.value = false
  }
}
onMounted(() => {
  Auth()
})
</script>

<template>
  <header class="bg-zinc-900 text-white items-center">
    <div class="flex justify-between">
      <router-link :to="{ path : '/' }">
      <div class="h-20">
        <img src="/logo.svg" class="w-full h-full" />
      </div>
      </router-link>
      <div v-if="!isAuth" class="grid grid-rows-1 grid-cols-2 items-center pr-20 gap-4 w-1/4">
        <router-link :to="{ path : '/login' }">
          <div>
            <button class="bg-white py-2 w-full rounded text-main text-2xl">
              Войти
            </button>
          </div>
        </router-link>
        <router-link :to="{ path : '/register' }">
          <div>
          <button class="bg-secondary py-2 w-full rounded text-main text-2xl">
            Регистрация
          </button>
        </div>
        </router-link>
      </div>
      <div v-if="isAuth" @click="logout" class="grid self-center mr-16" >
        <router-link :to="{ path : '/' }">
          <div class="grid">
            <div class="bg-white p-2 px-10 w-full rounded text-main text-2xl cursor-pointer cat-button">
              Выйти
            </div>
          </div>
        </router-link>
      </div>
    </div>
  </header>
</template>
<style scoped>
.cat-button:hover {
  background-color: #01bb72;
  color: white;
}
</style>
