<template>
  <div class="statistics">
    <h2>年龄统计</h2>
    <div v-for="(count, age) in ageCounts" :key="age" class="count" :class="age">
      年龄 {{ age }}: {{ count }}
    </div>
    <h2>工作年限统计</h2>
    <div v-for="(count, workExperience) in yearCounts" :key="workExperience" class="count">
      工作年限 {{ workExperience }}: {{ count }}
    </div>

  </div>
</template>

<script>
export default {
  name: 'ResumeAll',
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
  },
  computed: {
    // 主要就是实现的一些函数，就是实现年龄工作年限的一些统计
    ageCounts() {
      const counts = {};
      for (const resume of this.resumes) {
        const age = resume.age;
        if (age in counts) {
          counts[age]++;
        } else {
          counts[age] = 1;
        }
      }
      return counts;
    },
    yearCounts() {
      const counts = {};
      for (const resume of this.resumes) {
        const year = resume.workExperience;
        if (year in counts) {
          counts[year]++;
        } else {
          counts[year] = 1;
        }
      }
      return counts;
    }
  }
};
</script>

<style>
.el-main{
  line-height: 16px;
}
.age{
  line-height: 16px;
}
.statistics.compact {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  line-height: 16px;
}

.statistics.compact h2 {
  margin: 0;
}

.statistics.compact .count {
  margin: 4px 0;
}

</style>