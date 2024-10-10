import { createApp } from 'vue';
import './style.css';
import App from './App.vue';
import router from './router';
import Vue3StarRatings from 'vue3-star-ratings';

const app = createApp(App)

app.component("vue3StarRatings", Vue3StarRatings);
app.use(router)

app.mount('#app')
