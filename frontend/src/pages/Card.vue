<script setup>
import { ref } from "vue";
import { auth_get } from "../requests.js";
import { useRoute } from "vue-router";
import Cardinfo from "../components/Cardinfo.vue";
import Header from '../components/Header.vue';

const id = useRoute()["query"]["id"];

var Info;
var canRender = ref(false);
var reschar = [];
var len = 0;

auth_get(`/api/product/${id}`).then((res) => {
  Info = res;
  console.log(Info);
  const splitchar = Info.characteristic.split("\n")
  console.log(splitchar)
  for (let i = 0; i < splitchar.length; i++){
    reschar.push({id: i, text: splitchar[i]})
  }
  len = Info.characteristic.length;
  console.log(reschar)
  canRender.value = true;
});
</script>

<template>
  <div><Header></Header>
  <div class="grid" v-if="canRender">
    <Cardinfo
      :ListImg="Info.ListImg"
      :title="Info.title"
      :vendor="Info.vendor"
      :characteristic="reschar"
      :description="Info.description"
      :feedback="Info.feedback"
      :rating="Info.rating"
      :len="len"
      :user_characteristic="Info.user_characteristic"
      :minrating="Info.minrating"
      :maxrating="Info.maxrating"
    />
  </div>
  </div>
</template>
