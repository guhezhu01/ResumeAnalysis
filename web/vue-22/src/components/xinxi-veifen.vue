<template>
    <div class="resume-form">
      <div class="search" >
        <label for="search-box" class="search-label">Search:</label>
        <input type="text" id="search-box" v-model="searchKeyword" @input="searchResumes" placeholder="Enter a name" />
        <button @click="clearSearch">Clear</button>
      </div>
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
          resumes: [] ,// 用于存储后端返回的简历数据
          searchKeyword: '', // 搜索关键字
        };
      },
      mounted() {
        // 在组件挂载后，可以通过异步请求获取后端的简历数据
        // 这里只是一个示例，你需要根据实际情况修改
        this.fetchResumes();
      },
      computed: {
      filteredResumes() {
        if (this.searchKeyword === '') {
          return this.resumes; // 如果搜索关键字为空，则返回所有简历数据
        } else {
          // 使用搜索关键字过滤简历数据
          return this.resumes.filter((resume) =>
            resume.name.toLowerCase().includes(this.searchKeyword.toLowerCase())
          );
        }
      },
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
        },
        searchResumes() {
          // 搜索简历数据
          // 执行搜索操作，可以使用过滤函数或发送请求到后端进行搜索
        },
        clearSearch() {
          this.searchKeyword = ''; // 清空搜索关键字
        },
      }
    };
    </script>
    
  <style>
  .resume-form {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    background-image: url("../assets/background2.png");
    z-index: 0000;
  }
  
  .search {
    margin: 30px; /* 调整搜索框与边缘的距离 */
  }
  
  .search-label {
    margin-right: 10px; /* 调整标签与输入框之间的距离 */
  }
    
    /* .resume-form form {
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
  } */
  
  .grid-container {
    display: grid;
    grid-template-columns: repeat(4, 1fr); /* 设置横向比例为3:1 */
    gap: 20px; /* 方块之间的间隔 */
  }
  
  .grid-item {
    background-color:rgba(240, 240, 240, 0.8);
    padding: 10px;
    border-radius: 10px; /* 添加圆角属性 */
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); /* 阴影效果 */
    border: 1px solid rgba(0, 0, 0, 0.1); /* 边框样式 */
  }
  
  /* .item-label {
    background-color: #E9EEF3;
      color: #333;
      text-align: center;
      line-height: 25px;
  }
  
  .item-value {
    margin-top: 5px;
  } */
  
    </style>
  