<template>
    <el-container class="container">
      <el-container>
        <el-aside width="200px">
  
          <!-- 左侧导航 --><!-- default-active="/management/guanli" 默认加载页路由路径 -->
          <el-menu 
          default-active="/management/guanli/" 
          class="el-menu-vertical-demo" 
          @open="handleOpen" 
          @close="handleClose"
          background-color="#545c64" 
          text-color="#fff" 
          active-text-color="#ffd04b" 
          :router="true"><!-- :router="true"开启导航 -->
  
            <el-menu-item index="/management/guanli/">
              <i class="el-icon-menu"></i>
              <span slot="title">提交</span>
            </el-menu-item>
  
            <el-submenu index="2">
              <template slot="title">
                <i class="el-icon-location"></i>
                <span>显示</span>
              </template>
              <el-menu-item-group>
                <el-menu-item index="/management/xinxi">单个显示</el-menu-item>
                <el-menu-item index="/management/xiangqing">统计</el-menu-item>
              </el-menu-item-group>
            </el-submenu>
  
          </el-menu>
          <!-- 左侧导航 -->
  
  
        </el-aside>
        <el-main>
          <router-view :key="path"/>   <!--路由出口-->
        </el-main>
        
      </el-container>
  
    </el-container>
  </template>
  
  <script>
  export default {
    methods: {
      handleOpen(key, keyPath) {
        console.log(key, keyPath);
      },
      handleClose(key, keyPath) {
        console.log(key, keyPath);
      }
    }
  }
  </script>
  
  <style scoped>
  /* 去掉选项右侧边框 */
  .el-menu {
    border-right: none;
  } 
  /* 设置整体布局高度 */
  .container {
    height: 100vh;
  }
  
  
  .el-header,
  .el-footer {
    background-color: #B3C0D1;
    color: #333;
    text-align: center;
    line-height: 60px;
  }
  
  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
    position: fixed;
    top: 0;
    left: 0;
    bottom: 0;
  }
  
  .el-main {
    background-color: #E9EEF3;
    color: #333;
    text-align: left;
    line-height: 16px;
    /* padding: 0; */
    padding-left: 200px;
    /* padding-top: -100px; */
  }
  
  body>.el-container {
    margin-bottom: 40px;
  }
  
  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 260px;
  }
  
  .el-container:nth-child(7) .el-aside {
    line-height: 320px;
  }
  </style>