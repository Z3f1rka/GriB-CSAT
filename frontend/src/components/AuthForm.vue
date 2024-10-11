<script setup>
import { ref } from "vue";
import { z } from "zod";
import axios from "axios";
import router from "../router";

var name = ref("");
var role = ref(false);
var email = ref("");
var password = ref("");
var password_a = ref("");
var err_name = ref("");
var err_email = ref("");
var err_pass = ref("");
var err_end_pass = ref("");
const name_validation = z
  .string()
  .max(30, { message: "Максимальная длина имени - 30 символов" });
const email_validation = z
  .string()
  .email({ message: "Неверно указан адрес почты" });
const password_validation = z.string();
var can_reg = true;
var err = ref("");
var data_role = "user";

function data() {
  can_reg = true;
  if (!name_validation.safeParse(name.value).success) {
    err_name.value = "Максимальная длина имени - 30 символов";
    can_reg = false;
  } else {
    err_name.value = "";
  }
  if (name.value == "") {
    can_reg = false;
    err_name.value = "Обязательное поле";
  }
  if (!email_validation.safeParse(email.value).success) {
    can_reg = false;
    err_email.value = "Неправильно указан адрес почты";
  } else {
    err_email.value = "";
  }
  if (email.value == "") {
    can_reg = false;
    err_email.value = "Обязательное поле";
  }
  if (password.value == password_a.value) {
    err_end_pass.value = "";
  } else {
    can_reg = false;
    err_end_pass.value = "Пароли не совпадают";
  }
  if (password.value == "") {
    can_reg = false;
    err_pass.value = "Обязательное поле";
  } else {
    err_pass.value = "";
  }
  if (role._rawValue) {
    data_role = "vendor";
  }
  if (!role._rawValue) {
    data_role = "user";
  }
  if (can_reg) {
    const values = {
      name: name.value,
      email: email.value,
      pswd: password.value,
      pswd_repeated: password_a.value,
      role: data_role
    };
    axios
      .post("http://127.0.0.1:8080" + "/api/auth/register", values)
      .then((response) => {
        err.value = response.data.error;
        if (err.value) {
        } else {
          localStorage.setItem("access_token", response.data.access_token);
          localStorage.setItem("refresh_token", response.data.refresh_token);
          router.push("/");
        }
      }).catch((err) => {
        alert(err.response.data)
      });
  }
}
</script>

<template>
  <div class="bg-zinc-900 h-2/3 w-full rounded pt-4">
    <div
      class="grid grid-cols-8 grid-rows-10 items-center h-full w-full gap-10 py-10"
    >
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <p class="text-zinc-300 mb-2">Имя</p>
        <input
          type="text"
          class="w-full py-2 px-5 rounded"
          placeholder="Имя"
          v-model="name"
        />
      </div>
      <div class="mt-5 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_name }}</h1>
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <p class="text-zinc-300 mb-2">Почта</p>
        <input
          type="text"
          class="w-full py-2 px-5 rounded"
          placeholder="Почта"
          v-model="email"
        />
      </div>
      <div class="mt-5 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_email }}</h1>
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <p class="text-zinc-300 mb-2">Пароль</p>
        <input
          type="password"
          class="w-full py-2 px-5 rounded"
          placeholder="Пароль"
          v-model="password"
        />
      </div>
      <div class="col-span-6 col-start-2">
        <h1 class="mt-5  text-main">{{ err_pass }}</h1>
      </div>
      <div class="rounded row-span-1 col-span-6 col-start-2 h-10 w-full">
        <p class="text-zinc-300 mb-2">Повторите пароль</p>
        <input
          type="password"
          class="w-full py-2 px-5 rounded"
          placeholder="Повторите пароль"
          v-model="password_a"
        />
      </div>
      <div class="mt-5 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_end_pass }}</h1>
      </div>
      <div class="col-span-6 col-start-2 inline-flex">
        <input type="checkbox" v-model="role" style="width: 20px; height: 20px;" class="mt-1 mr-2" />
        <h1 class="text-white text-lg mb-4">- Я собираюсь выставлять свои товары</h1>
      </div>
      <div
        class="rounded row-span-1 col-span-4 col-start-3 h-10 w-full bg-main"
      >
        <button
          class="w-full h-full px-5 rounded text-white text-center text-lg"
          @click="data"
        >
          Подтвердить
        </button>
      </div>
    </div>
  </div>
</template>
