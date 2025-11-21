import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Personnel from '../views/Personnel.vue'
import Roster from '../views/Roster.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/personnel', component: Personnel },
  { path: '/roster', component: Roster },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
