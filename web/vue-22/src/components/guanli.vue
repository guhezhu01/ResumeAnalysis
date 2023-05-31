<template>
  <div>
    <h2>提交表单</h2>
    <div>
      <label>文字内容：</label>
      <textarea v-model="text"></textarea>
    </div>
    <div>
      <label>上传图片：</label>
      <input type="file" @change="uploadImage" accept="image/*">
    </div>
    <div>
      <label>上传PDF：</label>
      <input type="file" @change="uploadPDF" accept=".pdf">
    </div>
    <div>
      <label>上传文档表格：</label>
      <input type="file" @change="uploadDocument" accept=".doc, .docx, .xls, .xlsx">
    </div>
    <button @click="submitForm">提交</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      text: '',
      image: null,
      pdf: null,
      document: null
    };
  },
  methods: {
    uploadImage(event) {
      const file = event.target.files[0];
      // 使用Axios或其他方法将文件上传至服务器
      this.image = file;
    },
    uploadPDF(event) {
      const file = event.target.files[0];
      // 使用Axios或其他方法将文件上传至服务器
      this.pdf = file;
    },
    uploadDocument(event) {
      const file = event.target.files[0];
      // 使用Axios或其他方法将文件上传至服务器
      this.document = file;
    },
    submitForm() {
      // 在这里处理提交表单的逻辑，可以使用Axios发送表单数据至服务器
      const formData = new FormData();
      formData.append('text', this.text);
      formData.append('image', this.image);
      formData.append('pdf', this.pdf);
      formData.append('document', this.document);

      // 发送表单数据至服务器
      axios.post('/api/submit', formData)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>
