import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter);


  const routes = [
  {
    path: '/gan',
    name: 'gan',
    component: () => import(/* webpackChunkName: "about" */ '../src/components/GAN.vue'),
  },
  {
    path: "*",
    redirect: "/"
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  window.scrollTo(0, 0)
  next()
})

export default router
