<script setup>
import { ref } from 'vue';
import Search from '../components/Search.vue';
import Card from '../components/Card.vue';

const SearchResult = ref('x')
const ListCards = ref([{'title':'ttt', 'id':'1', 'img':'/gendalf.jpg'}])
</script>
<template>
    <div class="text-center">
        <Search />
        <div class="line">
            <h1 class="mt-9 mb-1 text-3xl">
                По вашему запросу найдено {{ SearchResult }} результатов:
            </h1>
        </div>
        <div class="mx-9 content-center"> 
            <div style="display: flex;" class="justify-around text-start flex-wrap">
                <Card 
                    v-for="item in ListCards" 
                    :key="item.id" 
                    :title="item.title" 
                    :id="item.id" 
                    :img="item.img"
                />
            </div>
        </div>
    </div>
</template>
<style scoped>
.line::after {
    display: inline-block;
    content: "";
    border-top: 2px solid black;
    width: 95%;
    transform: translateY(0.2rem);
}
span:focus-within{
    border: 1px solid #00BC72;
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
  background: #E5E5E5;
  background-size: 15px 15px;
  font-size: 26px;
  border: none;
  box-shadow: rgba(50, 50, 93, 0.25) 0px 2px 5px -1px,
    rgba(0, 0, 0, 0.3) 0px 1px 3px -1px;
}
</style>
