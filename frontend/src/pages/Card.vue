<script setup>
import { ref } from 'vue';
import Cardinfo from '../components/Cardinfo.vue';

const Info = ref({'ListImg':[{'id':'1', 'img':'/gendalf.jpg'}, {'id':'2', 'img':'/gendalf.jpg'}, {'id':'3', 'img':'/gendalf.jpg'}], 'title':'гель для душа gendalf core..', 'rating':'1', 'vendor': 'Vendor', 'characteristic': 'При этом обратите внимание на наш магазин, мы будем часто обновлять стиль одежды! В нашем магазине много модныхfffff', 'description':'description description description description', 'product_type':'1', 'feedback':[{'name':'name Sam', 'text':'очень крутой товар', 'img': '/gendalf.jpg', 'rating':'4.6', 'data':'20:03:2007', 'user_id':'1'}, {'name':'name Sam', 'text':'очень крутой товар', 'img': '/gendalf.jpg', 'rating':'4.1', 'data':'20:03:2007', 'user_id':'2'}] })
</script>

<template>
    <div class="grid">
        <Cardinfo 
            :ListImg="Info.ListImg" 
            :title="Info.title" 
            :vendor="Info.vendor"
            :characteristic="Info.characteristic" 
            :description="Info.description" 
            :product_type="Info.product_type" 
            :feedback="Info.feedback"
            :rating="Info.rating"
        />
    </div>
</template>