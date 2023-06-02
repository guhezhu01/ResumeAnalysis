<template>
  <div class="resume-form">
    <div class="grid-container">
      <div v-for="resume in resumes" :key="resume.id" class="grid-item">
        <div class="item-label">姓名:{{ resume.name }}</div>
        <!-- <div class="item-value">{{ resume.name }}</div> -->
        <div class="item-label">年龄:{{ resume.age }}</div>
        <!-- <div class="item-value">{{ resume.age }}</div> -->
        <div class="item-label">最高学历:{{ resume.education }}</div>
        <!-- <div class="item-value">{{ resume.education }}</div> -->
        <div class="item-label">工作年限:{{ resume.workExperience }}</div>
        <!-- <div class="item-value">{{ resume.workExperience }}</div> -->
        <div class="item-label">毕业院校:{{ resume.graduatedSchool }}</div>
        <!-- <div class="item-value">{{ resume.workHistory }}</div> -->
      </div>
    </div>
  </div>
</template>

  
  <script>
  export default {
    name: 'ResumeForm',
    data() {
      return {
        resumes: [] // 用于存储后端返回的简历数据
      };
    },
    mounted() {
      // 在组件挂载后，可以通过异步请求获取后端的简历数据
      // 这里只是一个示例，你需要根据实际情况修改
      this.fetchResumes();
    },
    methods: {
      fetchResumes() {
        // 执行异步请求，获取后端的简历数据
        // 这里只是一个示例，你需要根据实际情况修改
        // 可以使用axios等库发送请求到后端API
        // 示例代码：
        // axios.get('/api/resumes')
        //   .then(response => {
        //     this.resumes = response.data;
        //   })
        //   .catch(error => {
        //     console.error(error);
        //   });
        
        // 这里使用静态数据作为示例
        this.resumes = [
          {
            id: 1,
            name: '张三',
            age: 30,
            education: '本科',
            workExperience: '5 年',
            graduatedSchool: '北大'
          },
          {
            id: 2,
            name: '李四',
            age: 25,
            education: '大专',
            workExperience: '3 年',
            graduatedSchool: '机电'
          },
          {
            id: 3,
            name: '王五',
            age: 22,
            education: '硕士',
            workExperience: '3 年',
            graduatedSchool: '武大'
          },
          {
            id: 4,
            name: '3fs',
            age: 25,
            education: '本科',
            workExperience: '3 年',
            graduatedSchool: '华科'
          },
          {
            id: 5,
            name: 'fwse',
            age: 25,
            education: '博士',
            workExperience: '3 年',
            graduatedSchool: '上海交大'
          },
          {
            id: 6,
            name: 'fdsfd',
            age: 25,
            education: '本科',
            workExperience: '3 年',
            graduatedSchool: '杭电'
          },
          {
            id: 7,
            name: 'dfsfe',
            age: 25,
            education: '大专',
            workExperience: '3 年',
            graduatedSchool: '粮专'
          }
        ];
      }
    }
  };
  </script>
  
  <style>
  .resume-form {
    overflow-y: auto;
    padding: 20px;
    margin-top: -10px; /* 增加顶部的空间，具体数值可以根据需要进行调整 */
    /* background-image: url('~@/assets/background.jpg'); */
    background-size: cover;
    background-repeat: no-repeat;
  }
  
  .resume-form form {
    margin-bottom: 20px;
  }
  
  .resume-form label {
    display: block;
    margin-bottom: 5px;
  }
  
  .resume-form input[type="text"],
  .resume-form textarea {
    width: 100%;
    padding: 5px;
    margin-bottom: 10px;
  }
  .resume-form {
  padding: 20px;
}

.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 设置横向比例为3:1 */
  gap: 20px; /* 方块之间的间隔 */
}

.grid-item {
  background-color:rgba(240, 240, 240, 0.8);
  padding: 10px;
  border-radius: 10px; /* 添加圆角属性 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); /* 阴影效果 */
  border: 1px solid rgba(0, 0, 0, 0.1); /* 边框样式 */
}

.item-label {
  background-color: #E9EEF3;
    color: #333;
    text-align: center;
    line-height: 16px;
}

.item-value {
  margin-top: 5px;
}

  </style>
