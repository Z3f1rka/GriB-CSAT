<script setup></script>

<template>
  <header class="bg-zinc-900 text-white items-center">
    <div class="flex justify-between">
      <router-link :to="{ path : '/' }">
      <div class="h-20">
        <img src="/logo.svg" class="w-full h-full" />
      </div>
      </router-link>
      <div class="grid grid-rows-1 grid-cols-2 items-center pr-20 gap-4 w-1/4">
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
    </div>
  </header>
</template>
