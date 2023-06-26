<template>
    <div >
      <el-input
        type="textarea"
        :rows="6"
        placeholder="请输入内容"
        v-model="textarea">
      </el-input>
      <br><br><br> <br>
      <el-upload
        class="upload-demo"
        ref="upload"
        action="https://jsonplaceholder.typicode.com/posts/"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :file-list="fileList"
        :auto-upload="false">
        <el-button slot="trigger" size="small" type="primary">选取文件</el-button>
        <el-button style="margin-left: 10px;" size="small" type="success" @click="submitUpload">上传到服务器</el-button>
        <div slot="tip" class="el-upload__tip">上传文件的内容，默认为空。在上传成功后，文件列表应</div>
      </el-upload>
    </div>
  </template>
  <script>
    export default {
      data() {
        return {
          fileList: [],
          textarea: '', // 上传文件的内容，默认为空。在上传成功后，文件列表应
        };
      },
      methods: {
        submitUpload() {
          this.$refs.upload.submit();
        },
        handleRemove(file, fileList) {
          console.log(file, fileList);
        },
        handlePreview(file) {
          console.log(file);
        }
      }
    }
  </script>