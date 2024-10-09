<script setup>
import { ref } from "vue";
import { z } from "zod";
import axios from "axios";
import router from "../router";

var name = ref("");
var password = ref("");
var err_name = ref("");
var err_pass = ref("");
const name_validation = z
  .string()
  .max(30, { message: "Максимальная длина имени - 30 символов" });
var can_log = true;
var err = ref("");

function data() {
  can_log = true;
  if (!name_validation.safeParse(name.value).success) {
    err_name.value = "Максимальная длина имени - 30 символов";
    can_log = false;
  } else {
    err_name.value = "";
  }
  if (name.value == "") {
    can_log = false;
    err_name.value = "Обязательное поле";
  }

  if (password.value == "") {
    can_log = false;
    err_pass.value = "Обязательное поле";
  } else {
    err_pass.value = "";
  }
  if (can_log) {
    const values = {
      name: name.value,
      pswd: password.value
    };
    axios
      .post("http://127.0.0.1:8080" + "/api/auth/login", values)
      .then((response) => {
        err.value = response.data.error;
        if (err.value) {
          console.log(err.value);
        } else {
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
          router.push("/");
        }
      });
  }
}
</script>

<template>
  <div class="bg-zinc-900 h-2/3 w-full rounded">
    <div
      class="grid grid-cols-8 grid-rows-5 items-center h-full w-full gap-10 py-10"
    >
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Имя"
          v-model="name"
        />
      </div>
      <div class="h-10 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_name }}</h1>
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <input
          type="text"
          class="w-full h-full px-5 rounded"
          placeholder="Пароль"
          v-model="password"
        />
      </div>
      <div class="h-10 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_pass }}</h1>
      </div>
      <div
        class="rounded row-span-1 col-span-4 col-start-3 h-10 w-full bg-main"
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
