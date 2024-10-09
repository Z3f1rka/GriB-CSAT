import { createRouter, createWebHistory } from 'vue-router'
import Register from '../pages/Register.vue'
import Home from '../pages/Home.vue'
import Login from '../pages/Login.vue'
import Card from '../pages/Card.vue'
import AdminMain from '../pages/AdminMain.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/register', name: 'Register', component: Register },
    { path: '/login', name: 'Login', component: Login },
    { path: '/card', name: 'Card', component: Card },
    { path: '/admin', name: 'AdminPanel', component: AdminMain },
  ]
})

export default router