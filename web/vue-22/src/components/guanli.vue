<template>
  <div class="upload">
    <div class="upload-files">
      <div class="head">智能简历解析系统</div>
      <header>
        <p>
          <i class="fa fa-cloud-upload" aria-hidden="true"></i>
          <span class="up"></span>
          <span class="load">文件上传</span>
        </p>
      </header>
      <div class="body-container">
        <div class="body" id="drop" :class="{ active: isActive }" @dragleave="dragLeave" @dragover="dragOver" @drop="drop">
          <i class="fa fa-file-text-o pointer-none" aria-hidden="true"></i>
          <p class="pointer-none"><b>拖放文件到这里</b><br> 或 <a href="" @click.prevent="triggerFileSelect">点此选择文件</a></p>
          <input type="file" multiple="multiple" @change="handleFileSelect" ref="fileInput" />
        </div>
        <div class="leftsub">
          <footer v-if="hasFiles">
            <div class="divider">
              <span><AR>文件列表</AR></span>
            </div>
            <div class="list-files">
              <div v-for="(file, index) in files" :key="index">{{ file.name }}</div>
            </div>
            <button class="importar" @click="resetUpload">继续上传</button>
            <button class="importar" @click="submitUpload">点击上传</button>
          </footer>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      hasFiles: false,
      files: [],
      isActive: false
    };
  },
  methods: {
    triggerFileSelect() {
      this.$refs.fileInput.click();


    },
    dragLeave(event) {
      event.preventDefault();
      this.isActive = false;
    },
    dragOver(event) {
      event.preventDefault();
      this.isActive = true;
    },
    drop(event) {
      event.preventDefault();
      this.$refs.fileInput.files = event.dataTransfer.files;
      this.hasFiles = true;
      this.isActive = false;
    },

    // 将获取的文件存放到files中
    handleFileSelect(event) {
      this.files = Array.from(event.target.files);
      this.hasFiles = true;
    },
    
    // 清空上传中的文件列表
    resetUpload() {
      this.files = [];
      this.hasFiles = false;
    },

    //提交文件
    submitUpload() {
      // 在这里执行上传操作的逻辑
      // 可以使用this.files来访问已选择的文件列表

      // 清空文件列表和重置状态
      this.files = [];
      this.hasFiles = false;
    }

  }
};
</script>

<style>
.head{
  position: fixed;
  text-align-last: center;
  top: 10%;
  color: rgb(43, 120, 192);
  font-size: 46px; /* 调整字体大小为 24 像素 */
  font-family: "楷体", sans-serif; /* 更改字体样式为 Arial 或其他 sans-serif 字体 */
  font-weight: bold; /* 加粗字体 */
  text-transform: uppercase; /* 转换为大写字母 */
  letter-spacing: 10px; /* 字母间距增加为 2 像素 */
}

.upload{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: center; */
  /* flex-direction: column; */
  background-image: url("../assets/blue2.png");
  /* z-index: 0000; */
}

.upload-files {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  /* background-image: url("../assets/background2.png"); */

}

.upload-files header {
  text-align: center;
  margin-bottom: -10px;
  color: rgb(253, 178, 178);
}

.body-container {
  display: flex;
  padding-top: 2%;
  padding-left: 6%;
  padding-right: 6%;
  padding-bottom: 2%;
  width: 60%;
  height: 60%;
  /* background-color: rgba(255, 255, 255, 0.5); */
  /* background-image: url("../assets/background2.png"); */
  background-size: cover;
  background-repeat: no-repeat;
  /* margin-bottom: 10px; */
  /* backdrop-filter: blur(10px); */
  /* box-shadow: 0 0 10px rgba(0, 0, 0, 0.3); */
}


.body {
  flex: 1;
  display: flex;
  flex-direction:row;
  align-items: center;
  justify-content: center;
  /* border: 2px dashed #ccc; */
  padding: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
}

.leftsub{
  flex: 1;
  display: flex;
  flex-direction:row;
  align-items: center;
  justify-content: center;
  /* border: 2px dashed #ccc; */
  padding: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  background-color: rgba(255, 255, 255, 0.5);
  backdrop-filter: blur(10px);
}

/* .upload-files .body.active {
  background-color: #f9f9f9;
}

.upload-files .body i {
  font-size: 60px;
  margin-bottom: 10px;
}

.upload-files .body p {
  text-align: center;
}

.upload-files .body p b {
  font-weight: bold;
}

.upload-files .body p a {
  color: #3366cc;
}

.footer {
  margin-left: 20px;
  text-align: center;
}

.upload-files .divider {
  margin-bottom: 10px;
}

.upload-files .list-files {
  display: grid;
  gap: 10px;
}

.upload-files .list-files div {
  padding: 5px;
  background-color: #f9f9f9;
} */

.upload-files input[type="file"] {
  display: none;
}
</style>
