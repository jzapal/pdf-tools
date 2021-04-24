import { createRouter, createWebHashHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Merge from '../views/Merge.vue'
import Scan from '../views/Scan.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/merge',
    name: 'Połącz pliki PDF',
    component: Merge
  },
  {
    path: '/scan',
    name: 'Skan',
    component: Scan
  }
]

const router = createRouter({
  history: createWebHashHistory(process.env.BASE_URL),
  routes
})

export default router
