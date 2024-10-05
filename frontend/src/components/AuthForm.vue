<script setup>
import { ref } from "vue";

var name = ref("");
var role = ref(false);
var email = ref("");
var password = ref("");
var password_a = ref("");

function data() {
  console.log(
    name.value,
    email.value,
    password.value,
    password_a.value,
    role.value
  );
}
</script>

<template>
  <div class="bg-zinc-700 h-full w-full rounded pt-5">
    <div class="grid grid-cols-8 grid-rows-5 items-center">
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Имя"
          v-model="name"
        />
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Почта"
          v-model="email"
        />
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Пароль"
          v-model="password"
        />
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Повторите пароль"
          v-model="password_a"
        />
      </div>
      <div class="rounded row-span-1 col-span-4 col-start-3 h-10 bg-main mb-10">
        <button
          class="w-full h-full px-5 rounded text-white text-center"
          @click="data"
        >
          Подтвердить
        </button>
      </div>
    </div>
  </div>
</template>
