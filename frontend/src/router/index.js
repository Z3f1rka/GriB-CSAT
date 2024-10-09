import { createRouter, createWebHistory } from 'vue-router'
import Home from '../pages/Home.vue'
import Card from '../pages/Card.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/card', name: 'Card', component: Card },
  ]
})

export default router