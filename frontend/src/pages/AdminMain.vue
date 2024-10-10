<script setup>
import { ref, onMounted, watch } from "vue";
import Card from "../components/Card.vue";
import Category from "../components/Category.vue";

var isCateg = ref(false);

const ListCateg = ref([ 
  { id: 1, title: "ttt" },
  { id: 1, title: "ttt" },
  { id: 1, title: "ttt" },
  { id: 1, title: "ttt" },
  { id: 1, title: "ttt" },
  { id: 1, title: "ttt" },
  { id: 1, title: "ttt" },
])
const ListCards = ref([
  { id: 1, title: "Бытовая техника", img: "/gendalf.jpg" },
  { id: 1, title: "FFFFFF FFFFFFFFFFF FFFFFFFFFF FFFFFFF", img: "/gendalf.jpg" },
  { id: 1, title: "Техника", img: "/gendalf.jpg" },
  { id: 1, title: "Техника", img: "/gendalf.jpg" },
  { id: 1, title: "Техника", img: "/gendalf.jpg" },
  { id: 1, title: "Техника", img: "/gendalf.jpg" },
]);
const FilteredCards = ref([])
const FilteredCateg = ref([])
const SearchResult = ref('')
const input = defineModel()


function search(n, k){
  if(!k){
    FilteredCards.value = []
    var text = String(n).toLowerCase()
    for (let el of ListCards.value) {
        if (el.title.toLowerCase().includes(text)){
            FilteredCards.value.push(el)
        }
    }    
    if (text) {
        SearchResult.value = FilteredCards.value.length
    }
    else {
        SearchResult.value = ''
    }
    if (!FilteredCards.value.length && !SearchResult) {
        FilteredCards.value = ListCards.value
    }
    if (!FilteredCards.value.length && SearchResult) {
        SearchResult.value = '0'
    }}
  if(k){
    FilteredCateg.value = []
    var text = String(n).toLowerCase()
    for (let el of ListCateg.value) {
        if (el.title.toLowerCase().includes(text)){
            FilteredCateg.value.push(el)
        }
    }    
    if (text) {
        SearchResult.value = FilteredCateg.value.length
    }
    else {
        SearchResult.value = ''
    }
    if (!FilteredCateg.value.length && !SearchResult) {
        FilteredCateg.value = ListCateg.value
    }
    if (!FilteredCateg.value.length && SearchResult) {
        SearchResult.value = '0'
    }}
}
onMounted(() => {
    search('');
})
</script>
<template>
  <div class="text-center">
    <div class="border-b-2 border-zinc-900 mt-10 inline-flex">
      <div 
        tabindex="1"
        class="h-15 w-80 text-3xl cursor-pointer select-none cat-button" 
        @click="isCateg = false; search('', isCateg); input='';"
      >
        Запросы товаров
      </div>
      <div
        tabindex="1"
        class=" h-15 w-80 text-3xl cursor-pointer des-button select-none cat-button"
        @click="isCateg = true; input=''; search('', isCateg);"
      >
        Категории
      </div>
    </div>
      
    <div>
      <span class="input text-center my-10 border shadow-sm border-slate-300 placeholder-slate-400 focus:outline-none focus:border-sky-500 focus:ring-sky-500 w-full rounded sm:text-sm focus:ring-1 relative">
            <div class="grid grid-rows-1 grid-cols-12">
                <div class="grid text-left col-span-11">
                        <input 
                            class="outline-none p-0 pl-11" 
                            style="background: #E5E5E5; resize: vertical;" 
                            placeholder="Поиск "
                            v-model="input" 
                        />
                </div>
                <div @click="search(input, isCateg)" class="grid text-right cursor-pointer">
                    <img 
                        src="/search.png" 
                        class="icon text-align-right self-center select-none"
                    />
                </div>
            </div>
        </span>
    <div class="mx-9 content-center">
      <div>
        <div class="line">
            <h1 class="mt-4 mb-1 text-3xl" v-if="SearchResult">
                По вашему запросу найдено {{ SearchResult }} результатов:
            </h1>
        </div>
        <transition name="slide-right">
      <div
        style="display: flex"
        class="ml-8 text-start flex-wrap"
        v-if="isCateg"
      >
      <transition name="slide-right">
      <router-link :to="{ path: '/createcategory' }">
        <div
          class="rounded text-main text-center bg-secondary w-60 cursor-pointer text-5xl h-14 px-2 mt-2 mx-2"
        >
          <b class="text-wrap h-full break-after-all select-none">
            +
          </b>
        </div>
      </router-link>
    </transition>
        <Category
          class="mx-2"
          v-for="item in FilteredCateg"
          :key="item.id"
          :title="item.title"
          :id="item.id"
        />
      </div>
      </transition>
      <transition name="slide-right">
      <div
        style="display: flex"
        class="justify-start text-start flex-wrap"
        v-if="isCateg == false"
      >
        <Card
          v-for="item in FilteredCards"
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
.cat-button{
  background: white;
}
.cat-button:active, .cat-button:focus {
  background: #00bc72;
}
.slide-right-leave-active{
  transition: all .4s cubic-bezier(1.0, 0.5, 0.8, 1.0);

}
.slide-right-enter-active,
.slide-left-enter-active,
.slide-left-leave-active{
  transition: all .5s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}

.slide-left-enter {
  transform: translateX(100%);
}

.slide-left-leave-to {
   transform: translateX(-100%);
}

.slide-right-enter {
  transform: translateX(-100%);
}

.slide-right-leave-to {
   transform: translateX(100%);
}
.v-enter-active {
    animation: added 0.1s;
}
.v-leave-active {
  animation: added 0.1s reverse;
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
  margin-left: 30%;
  translate: 60px 0px;
}
to {
  margin-left: 0;
  translate: 0 0px;
}
}
</style>
