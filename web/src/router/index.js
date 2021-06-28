import Vue from 'vue'
import VueRouter from 'vue-router'
import School from '../views/School.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'School',
    component: School
  }
]

const router = new VueRouter({
  routes
})

export default router
