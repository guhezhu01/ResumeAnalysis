import Vue from 'vue'
import App from './App.vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import router from './index.js';
import * as echarts from 'echarts' // echarts库
Vue.prototype.$echarts = echarts
// import echarts from'echarts';
// import ECharts from 'vue-echarts';
// 引入FontAwesome图标库 样式
import '@fortawesome/fontawesome-free/css/all.css';


Vue.config.productionTip = false

Vue.use(ElementUI);
// Vue.component('ECharts',ECharts);
// Vue.use(echarts);

new Vue({
  render: h => h(App),
  router
}).$mount('#app')
