<script setup>
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <div>
    <Header></Header>
    <router-view></router-view>
  </div>
</template>
