import Vue from 'vue'
import VueRouter from 'vue-router'
import Info from '../views/Info.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Info',
    component: Info
  },
  {
    path: '/Miljo',
    name: 'Miljo',
    component: () => import('../views/Miljo.vue')
  },
  {
    path: '/Kontakt',
    name: 'Kontakt',
    component: () => import('../views/Kontakt.vue')
  }
]

const router = new VueRouter({
  routes
})

export default router
