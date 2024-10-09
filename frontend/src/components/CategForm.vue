<script setup>
import { ref } from "vue";
import { z } from "zod";
import router from "../router";
import { auth_post } from "../requests";

var title = ref("");
var new_char = ref("");
var err_title = ref("");
var err_char = ref("");
var charList = ref([]);
const title_validation = z
  .string()
  .max(30, { message: "Максимальная длина имени - 30 символов" });
const char_validation = z
  .string()
  .max(20, { message: "Максимальная длина имени - 20 символов" });
var can_log = true;
var can_add = true;
var err = ref("");
function remove(char) {
  charList.value = charList.value.filter((item) => item != char);
}
function add() {
  can_add = true;
  if (!char_validation.safeParse(new_char.value).success) {
    err_char.value = "Максимальная длина - 20 символов";
    can_add = false;
  }
  if (charList._rawValue.indexOf(new_char.value) != -1) {
    err_char.value = "Такая характеристика уже есть";
    can_add = false;
  }
  if (new_char.value == "") {
    can_add = false;
    err_char.value = "Нельзя отправить пустую строку";
  }
  if (can_add) {
    charList.value.push(new_char.value);
    err_char.value = "";
  }
}
function data() {
  can_log = true;
  if (!title_validation.safeParse(title.value).success) {
    can_log = false;
    err_title.value = "Максимальная длина - 20 символов";
  }
  if (can_log) {
    var resp_data = auth_post("/", {
      title: title.value,
      list: charList._rawValue,
    });
    if (resp_data) {
      router.push("/admin");
    }
  }
}
</script>

<template>
  <div class="bg-zinc-900 h-2/3 w-full rounded">
    <div
      class="grid grid-cols-8 grid-rows-8 items-center h-full w-full gap-10 py-10"
    >
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Название"
          v-model="title"
        />
      </div>
      <div class="h-10 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_title }}</h1>
      </div>
      <div class="rounded row-span-1 col-span-5 col-start-2 h-10 w-full">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Добавить характеристику"
          v-model="new_char"
        />
      </div>
      <div
        @click="add()"
        class="col-span-1 rounded bg-secondary text-main text-center cursor-pointer p-2 px-5"
      >
        <b> Добавить</b>
      </div>
      <div class="h-10 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_char }}</h1>
      </div>
      <div
        class="bg-zinc-800 row-span-3 col-span-6 col-start-2 row-start-5 h-full w-full rounded flex justify-start p-2"
      >
      <div style="display: flex;" class=" text-start flex-wrap content-start overflow-auto">
        <div
          class="bg-main rounded-lg text-center text-white truncate cursor-pointer px-2 mx-2 select-none mb-1"
          v-for="char in charList"
          :key="char"
          @click="remove(char)"
        >
          {{ char }}
    </div></div>
      </div>
      <div
        class="rounded row-span-1 col-span-4 col-start-3 row-start-8 h-10 w-full bg-main"
      >
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
