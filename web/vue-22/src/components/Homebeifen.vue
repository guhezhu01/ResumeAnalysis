<template>
    <el-container class="container">
      <!-- <el-container> -->
        <video id="startVideo" autoplay loop muted @ended="videoEnded" v-if="!videoEnded">
          <source src="../assets/start2.mp4" type="video/mp4">
        </video>
        <el-aside class="aside" width="100px" :style="{ left: asideVisible ? '0' : '-200px' }">
          
          <!-- 左侧导航 --><!-- default-active="/management/guanli" 默认加载页路由路径 -->
          <el-menu 
          default-active="/management/guanli/" 
          class="el-menu-vertical-demo" 
          :router="true"><!-- :router="true"开启导航 -->
            <!-- 提交 -->
            <el-menu-item class="menufirst" index="/management/guanli/">提交</el-menu-item>
            <el-menu-item class="menusecond" index="/management/xinxi">显示</el-menu-item>
            <el-menu-item class="menuthird" index="/management/xiangqing">统计</el-menu-item>
            <!-- 显示 -->
          </el-menu>
          <!-- 左侧导航 -->  
        </el-aside>
        <!-- // button  -->
        <i class="button" @click="toggleAside">C</i>

        <el-main>
          <router-view :key="path"/>   <!--路由出口-->
        </el-main>
        
      <!-- </el-container> -->
  
    </el-container>
  </template>
  
<script>
  export default {
    methods: {
      // handleOpen(key, keyPath) {
      //   console.log(key, keyPath);
      // },
      // handleClose(key, keyPath) {
      //   console.log(key, keyPath);
      // },
      // 实现点击反转的逻辑，调入调出区域，不是按钮。 （note the space bar） 或者在页面加载时实现点击反转。
      toggleAside() {
      this.asideVisible = !this.asideVisible;
    },
    },
    data(){
      return{
        path: '',
        videoEnded: true,   //true关闭
        asideVisible: true, // true显示导航栏 
      }
    },
    mounted() {
    setTimeout(() => {
      this.videoEnded = true;
    }, 5000);
  }
  }
</script>
  
<style scoped>
  /* 按钮css */
  .button {
    position: fixed;
    top: 30px;
    left: 30px;
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

  /* 去掉选项右侧边框 */
  /* .el-menu {
    border-right: none;
  }  */


  /* 设置整体布局高度。整体都填充满 */
  .container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }
  
  /* 视频样式调节 */
  #startVideo {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  z-index: 9999;
  } 

  /* 左侧边实现 */
   .aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
    position: fixed;
    top: 100px;
    padding-left: 0px;
    bottom: 668px;
    /* width: 140px; */
    border-radius: 10px; /* 设置圆角矩形 */
    transition: width 1s ease;
    z-index: 9998;
  } 
  /* .menufirst{
    background-color: rgb(209, 153, 153);
    color:antiquewhite;
  } */
  .el-menu-vertical-demo{
    background-color:#cbdcec;
    /* text-color:#fff;
    active-text-color:#ffd04b; */
  }

  /* 主框实现 */
  .el-main {
    /* background-image: url("../assets/background.jpg"); 替换为你的图片路径 */
    background-size: cover; /* 将背景图片缩放到完全覆盖元素 */
    background-repeat: no-repeat; /* 禁止背景图片重复 */
    background-position: center center; /* 将背景图片居中显示 */
    background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 20px;
    padding-left: 150px;
    padding-top: 30px;
  }

</style>