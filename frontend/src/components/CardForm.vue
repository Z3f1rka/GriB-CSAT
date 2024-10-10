<script setup>
import { ref } from "vue";
import { z } from "zod";
import { auth_get, auth_post } from "../requests";
import axios from "axios";
import router from "../router";

var title = ref("");
var description = ref("");
var characteristics = ref("");
var categList = ref([]);
var err_title = ref("");
var err_description = ref("");
var err_char = ref("");
var err_categ = ref("");
const title_validation = z
  .string()
  .max(60, { message: "Максимальная длина - 60 символов" });
var can_reg = true;
var err = ref("");
var chooseCateg = ref([]);
var selectedFile;
var choosedFiles = ref([]);

auth_get("/api/category/all").then((data) => {
  categList.value = data;
})

function onFileChange(event) {
  selectedFile = event.target.files[0];
}

function addFile() {
  if (selectedFile && selectedFile.type.includes("image")) {
    choosedFiles.value.push({
      id: choosedFiles.value.length,
      file: selectedFile,
    });
    console.log(choosedFiles._rawValue);
  }
}

function removeFile(id) {
  for (let i = 0; i < choosedFiles.value.length; i++) {
    if (choosedFiles.value[i].id == id) {
      choosedFiles.value.splice(i, 1);
      break;
    }
  }
}

async function uploadFile(file) {
  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await axios.post(
      "http://localhost:8000/upload",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );
    alert(response.data.message);
  } catch (error) {
    console.error(error);
    alert("Error uploading file.");
  }
}

function choose(x, n) {
  var num = x;
  if (n) {
    for (let el of categList.value) {
      if (el.id === num) {
        chooseCateg.value.push(el);
        categList.value = categList.value.filter((item) => item != el);
      }
    }
  } else {
    for (let el of chooseCateg.value) {
      if (el.id === num) {
        categList.value.push(el);
        chooseCateg.value = chooseCateg.value.filter((item) => item != el);
      }
    }
  }
}

function data() {
  can_reg = true;
  if (!title_validation.safeParse(title.value).success) {
    err_title.value = "Максимальная длина - 60 символов";
    can_reg = false;
  } else {
    err_title.value = "";
  }
  if (title.value == "") {
    can_reg = false;
    err_title.value = "Обязательное поле";
  }
  if (description.value == "") {
    can_reg = false;
    err_description.value = "Обязательное поле";
  }
  if (characteristics.value == "") {
    can_reg = false;
    err_char.value = "Обязательное поле";
  } else {
    err_char.value = "";
  }
  if (chategList._rawValue.length == 0) {
    can_reg = false;
    err_categ.value = "Обязательное поле";
  }
  if (can_reg) {
    const values = {
      title: title.value,
      description: description.value,
      characteristics: characteristics.value,
      categories: categList._rawValue,
    };
    console.log(values);
    var resp_data = auth_post("/api/card/add", values);
    if (resp_data) {
      router.push("/");
    }
  }
}
</script>
<template>
  <div class="bg-zinc-900 grid rounded mb-10">
    <div class="grid grid-cols-8 grid-rows-1 items-center pt-10 pb-5">
      <div></div>
      <div class="grid col-span-6">
        <input
          type="text"
          class="px-5 py-2 rounded"
          placeholder="Название"
          v-model="title"
        />
      </div>
    </div>
    <div class="grid grid-cols-8 pb-5">
      <div></div>
      <div class="col-span-6">
        <h1 class="text-main">{{ err_title }}</h1>
      </div>
    </div>
    <div class="grid grid-cols-8 pb-2 pt-1">
      <div></div>
      <div class="col-span-6 grid">
        <textarea
          style="height: 150px"
          class="px-4 pt-1 rounded resize-none overflow-auto"
          placeholder="Описание"
          v-model="description"
        ></textarea>
      </div>
    </div>
    <div class="grid grid-cols-8 pb-2">
      <div class="h-10 col-span-6 col-start-2">
        <h1 class="text-main">{{ err_description }}</h1>
      </div>
    </div>
    <div class="grid grid-cols-8 pb-5">
      <div></div>
      <div class="rounded col-span-6">
        <textarea
          style="height: 150px"
          class="w-full px-4 pt-2 rounded resize-none overflow-auto"
          placeholder="Характеристики"
          v-model="characteristics"
        ></textarea>
      </div>
    </div>
    <div class="grid grid-cols-8 pb-2">
      <div class="col-span-6 col-start-2">
        <h1 class="text-main">{{ err_char }}</h1>
      </div>
    </div>
    <div class="grid grid-cols-8 pb-5">
      <div></div>
      <div class="grid grid-cols-2 col-span-6 grid-rows-1">
        <div class="mr-1">
          <div class="text-white text-center mb-2">Список категорий</div>
          <div class="bg-zinc-600 rounded overflow-auto" style="height: 280px">
            <div
              v-for="item in categList"
              :key="item.id"
              class="p-2 text-white hover:bg-main cursor-pointer"
            >
              <p @click="choose(item.id, 1)">+ {{ item.title }}</p>
            </div>
          </div>
        </div>
        <div class="ml-1">
          <div class="text-white text-center mb-2">Ваши категории</div>
          <div class="bg-zinc-600 rounded overflow-auto" style="height: 280px">
            <div
              v-for="item in chooseCateg"
              :key="item.id"
              class="p-2 text-white hover:bg-main cursor-pointer"
            >
              <p @click="choose(item.id, 0)">- {{ item.title }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="grid grid-cols-8 pb-5">
      <div class="col-span-2"></div>
      <div class="col-start-2 col-span-6 h-40 text-white">
        <div class="grid grid-rows-1 grid-cols-3">
          <input type="file" @change="onFileChange" class="col-span-2 mt-3" />
          <button
            @click="addFile"
            class="rounded col-start-3 bg-secondary m-2 p-2 text-white"
          >
            Добавить
          </button>
        </div>
        <div>
          <div
            v-for="file in choosedFiles"
            :key="file"
            class="cursor-pointer bg-tgray m-2 px-3 rounded hover:bg-main"
            @click="removeFile(file.id)"
          >
            <p>{{ file.file.name }}</p>
          </div>
        </div>
      </div>
      <div class="rounded col-span-4 bg-main grid justify-center col-start-3">
        <button class="px-5 rounded text-white text-center" @click="data">
          <p class="block text-center self-center p-2"><b>Подтвердить</b></p>
        </button>
      </div>
    </div>
  </div>
</template>
