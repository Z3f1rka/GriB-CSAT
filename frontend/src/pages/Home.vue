<script setup>
import { computed, onMounted, ref } from 'vue';
import Card from '../components/Card.vue';

const SearchResult = ref('x')
let ListCards = ref([{'title':'ttt', 'id':1, 'img':'/gendalf.jpg'}, {'title':'aaa', 'id':2, 'img':'/gendalf.jpg'}, {'title':'ttt', 'id':3, 'img':'/gendalf.jpg'}, {'title':'aaa', 'id':4, 'img':'/gendalf.jpg'}, {'title':'ttt', 'id':5, 'img':'/gendalf.jpg'}, {'title':'aaa', 'id':2, 'img':'/gendalf.jpg'}])
const FilteredCards = ref([])
const input = defineModel()

function search(n){
    FilteredCards.value = []
    var text = String(n)
    console.log(ListCards.value)
    for (let el of ListCards.value) {
        if (el.title.includes(text)){
            FilteredCards.value.push(el)
        }
    }    
}
onMounted(() => {
    search('');
})
</script>
<template>
    <div class="text-center">
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
                <div @click="search(input)" class="grid text-right">
                    <img 
                        src="/search.png" 
                        class="icon text-align-right self-center noselect"
                    />
                </div>
            </div>
        </span>
        <div class="line">
            <h1 class="mt-9 mb-1 text-3xl">
                По вашему запросу найдено {{ SearchResult }} результатов:
            </h1>
        </div>
        <div class="mx-9 content-center"> 
            <div style="display: flex;" class="justify-start text-start flex-wrap">
                <Card 
                    v-for="item in FilteredCards" 
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
    content: '';
    width: 90%;
    height: 1px;
    background-color: black;
    display: inline-flex;
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