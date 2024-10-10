<script setup>
import { ref } from "vue";
import Search from "../components/Search.vue";
import Card from "../components/Card.vue";
import Category from "../components/Category.vue";

var isCateg = ref(false);

const ListCards = ref([]);
const ListCateg = ref([
  { id: 1, title: "Бытовая техника" },
  { id: 1, title: "FFFFFF FFFFFFFFFFF FFFFFFFFFF FFFFFFF" },
  { id: 1, title: "Техника" },
  { id: 1, title: "Техника" },
  { id: 1, title: "Техника" },
  { id: 1, title: "Техника" },
]);
</script>
<template>
  <div class="text-center">
    <div class="border-b-2 border-zinc-900 mt-10 inline-flex">
      <div 
        class="bg-secondary h-15 w-80 text-main text-3xl cursor-pointer select-none" 
        @click="isCateg = false"
      >
        Запросы товаров
      </div>
      <div
        class="bg-main h-15 w-80 text-white text-3xl cursor-pointer des-button select-none"
        @click="isCateg = true"
      >
        Категории
      </div>
    </div>
      
    <div>
    <Search />
    <div class="mx-9 content-center">
      <div>
        <transition>
      <div
        style="display: flex"
        class="justify-around text-start flex-wrap"
        v-if="isCateg"
      >
        <div
          class="rounded text-main text-center bg-secondary w-60 cursor-pointer text-5xl h-14 px-2 mt-2"
        >
          <b class="text-wrap h-full break-after-all">
            +
          </b>
        </div>
        <Category
          v-for="item in ListCateg"
          :key="item.id"
          :title="item.title"
          :id="item.id"
        />
      </div>
      </transition>
      <transition>
      <div
        style="display: flex"
        class="justify-around text-start flex-wrap"
        v-if="isCateg == false"
      >
        <Card
          v-for="item in ListCards"
          :key="item.id"
          :title="item.title"
          :id="item.id"
          :img="item.img"
        />
      </div>
    </transition>
    </div>
    </div>
    </div>
  </div>
</template>
<style scoped>
.v-enter-active {
    animation: added 0.5s;
}
.v-leave-active {
  animation: added 0.3s reverse;
}
.fade-leave-active {
    animation: added 0.5s;
}
.fade-enter-active {
  animation: added 0.5s reverse;
}

.line::after {
  display: inline-block;
  content: "";
  border-top: 2px solid black;
  width: 95%;
  transform: translateY(0.2rem);
}
span:focus-within {
  border: 1px solid #00bc72;
}
.icon {
  position: relative;
  height: 40%;
}
.focus\:border-sky-500:focus {
  --tw-border-opacity: 0.5;
  border-color: rgb(78 82 91 / var(--tw-border-opacity)) /* #0ea5e9 */;
}
.focus\:ring-sky-500:focus {
  --tw-ring-opacity: 0.5;
  --tw-ring-color: rgb(78 82 91 / var(--tw-ring-opacity)) /* #0ea5e9 */;
}
.input {
  display: block;
  width: 20cm;
  margin: 20px auto;
  background: #e5e5e5;
  background-size: 15px 15px;
  font-size: 26px;
  border: none;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
@keyframes added {
from {
  margin-top: 5%;
  translate: 0 -60px;
}
to {
  margin-top: 0;
  translate: 0 0px;
}
}
</style>
