<template>
  <div class="submit">
    <input type="file" @change="handleFileUpload" accept=".jpg,.png,.pdf" />
    <!-- 这里的handleFileUpload是用来处理文件上传的方法 -->
    <button @click="submitForm">Submit</button>  
    <!-- 这个按钮是用来提交表单的 -->
  </div>
</template>

<script>
export default {
  name: 'HeaderSection',
  methods: {
    // 处理文件上传的逻辑
    handleFileUpload() {
      // const file = event.target.files[0]; // 移除未使用的变量 "event"
      // 执行上传操作，可以使用axios等库发送文件到后端
      // ...
    },
    //提交数据
    submitForm() {
      // // 在这里处理提交表单的逻辑，可以使用Axios发送表单数据至服务器
      // const formData = new FormData();
      // formData.append('text', this.text);
      // formData.append('image', this.image);
      // formData.append('pdf', this.pdf);
      // formData.append('document', this.document);

      // // 发送表单数据至服务器
      // axios.post('/api/submit', formData)
      //   .then(response => {
      //     console.log(response.data);
      //   })
      //   .catch(error => {
      //     console.error(error);
      //   });
    }
  }
};
</script>

<style>
.submit {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  background-image: url("../assets/background1.jpg");
  z-index: 0000;
}



.submit input[type="file"] {
  width: 200px;
  height: 40px;
  margin-bottom: 20px;
  padding: 10px;
  font-size: 16px;
  background-color: #e3b46d;
  border: none;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  color: #333;
  
}

.submit button {
  width: 160px;
  height: 40px;
  font-size: 16px;
  /* background-color: #7899ce; */
  color: #fff;
  border: none;
  border-radius: 4px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: background-color 0.3s ease;
  background-color: rgba(70, 120, 199, 0.7); /* 添加半透明背景颜色 */
  backdrop-filter: blur(5px); /* 添加磨砂效果 */
}

.submit button:hover {
  background-color: #3277d6;
}

.submit button:focus {
  outline: none;
}


</style>
