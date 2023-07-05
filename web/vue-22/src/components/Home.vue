<template>
  <Transition>
    <div class="container">
      <video id="startVideo" autoplay loop muted @ended="handlevideoEnded" v-if="!videoEnded" class="fade-out">
        <source src="../assets/进度条_1.mp4" type="video/mp4">
      </video>
      
      <div class="aside" :style="{ left: asideVisible ? '0' : '-200px' }">
        <ul class="menu-vertical-demo">
          <li class="menu-item" :class="{ active: path === '/management/guanli' }">
            <a href="#/management/guanli">提交</a>
          </li>
          <li class="menu-item" :class="{ active: path === '/management/xinxi' }">
            <a href="#/management/xinxi">显示</a>
          </li>
          <li class="menu-item" :class="{ active: path === '/management/xiangqing' }">
            <a href="#/management/xiangqing">统计</a>
          </li>
        </ul>
      </div>
      <div class="button" @click="toggleAside">C</div>
      <div class="main">
        <router-view :key="path"/>
      </div>
    </div>
  </Transition>
</template>
<script>
export default {
  methods: {
    toggleAside() {
      this.asideVisible = !this.asideVisible;
    },
    handlevideoEnded() {
      this.videoEnded = true;
    }
  },
  data() {
    return {
      path: '',
      videoEnded: false,
      asideVisible: true
    };
  },
  mounted() {
    setTimeout(() => {
      this.videoEnded = true;
    }, 4000);
  }
};
</script>
<style scoped>
/* @import '../assets/css/globle.css'; */
.container {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

#startVideo {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 9999;
}


.aside {
  width: 70px;
  background-color: #D3DCE6;
  color: #333;
  text-align: center;
  line-height: 50px;
  position: fixed;
  top: 10%;
  padding-left: 0px;
  border-radius: 10px;
  transition: width 1s ease;
  z-index: 9998;
}

.menu-vertical-demo {
  list-style: none;
  padding: 0;
  margin: 0;
}

.menu-item {
  background-color: #cbdcec;
  padding: 10px;
  margin-bottom: 5px;
  border-radius: 5px;
}

.menu-item a {
  text-decoration: none;
  color: #333;
}

.menu-item.active {
  background-color: rgb(209, 153, 153);
  color: antiquewhite;
}

.button {
  position: fixed;
  top: 30px;
  left: 20px;
  width: 40px;
  height: 40px;
  background-color: orange;
  border-radius: 50%;
  text-align: center;
  line-height: 40px;
  font-size: 20px;
  color: white;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
  backdrop-filter: blur(10px);
  z-index: 9999;
}

.main {
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center center;
  /* background-color: #E9EEF3; */
  background-image: url("../assets/blue2.png");
  color: #333;
  line-height: 20px;
  padding-left: 8%;
  padding-top: 30px;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
</style>