import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from './components/Home.vue'
import Guanli from './components/guanli.vue'
import Xinxi from './components/xinxi.vue'
import Xiangqing from './components/xiangqing.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    redirect:'/management/guanli'//默认页直接重定向到你要显示的默认页
  },
  {
    path: '/management/',
    name: 'management',
    component: Home,
    children:[
        {
          path: 'guanli',//默认显示页路径
          name: 'Guanli',
          component: Guanli, 
        },
        {
          path: 'xinxi',
          name: 'Xinxi',
          component: Xinxi
        },
        {
          path: 'xiangqing',
          name: 'Xiangqing',
          component: Xiangqing
        }
    ]
  }
]

const router = new VueRouter({
  routes
})

export default router
