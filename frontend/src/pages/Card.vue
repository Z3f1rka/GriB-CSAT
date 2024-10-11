<script setup>
import { ref } from 'vue';
import Cardinfo from '../components/Cardinfo.vue';
import Header from '../components/Header.vue';
import { useRoute } from 'vue-router';

const id = useRoute()["query"]["id"]


const Info = ref({'ListImg':[{'id':'1', 'img':'/gendalf.jpg'}, {'id':'2', 'img':'/gendalf.jpg'}, {'id':'3', 'img':'/gendalf.jpg'}], 'title':'гель для душа gendalf core..', 'rating':'1', 'maxrating':{'text':'за то', 'count':'4.5'}, 'minrating':{'text':'за это', 'count':'1'}, 'vendor': 'Vendor', 'characteristic': [{'id':1, 'text':'первая'}, {'id':2, 'text':'вторая'}, {'id':3, 'text':'третья'}, {'id':4, 'text':'третья'}, {'id':5, 'text':'третья'}, {'id':6, 'text':'третья'}, {'id':7, 'text':'третья'}, {'id':8, 'text':'третья'}, {'id':9, 'text':'третья'}, {'id':10, 'text':'третья'}, {'id':11, 'text':'третья'}, {'id':12, 'text':'третья'}, {'id':13, 'text':'третья'}, {'id':14, 'text':'третья'}, {'id':15, 'text':'третья'}, {'id':16, 'text':'третья'}], 'description':'description description description description', 'feedback':[{'name':'name Sam', 'text':'очень крутой товар', 'rating':'4.6', 'data':'20:03:2007', 'user_id':'1'}, {'name':'name Sam', 'text':'очень крутой товар', 'rating':'4.1', 'data':'20:03:2007', 'user_id':'2'}], 'user_characteristic':['Крутость', 'Яркость', 'Злость'] })
const len = Info.value.characteristic.length
</script>

<template>
    <div><Header></Header>
    <div class="grid">
        <Cardinfo 
            :ListImg="Info.ListImg" 
            :title="Info.title" 
            :vendor="Info.vendor"
            :characteristic="Info.characteristic" 
            :description="Info.description" 
            :feedback="Info.feedback"
            :rating="Info.rating"
            :len="len"
            :user_characteristic="Info.user_characteristic"
            :minrating="Info.minrating"
            :maxrating="Info.maxrating"
            :id="id"
        />
    </div></div>
</template>