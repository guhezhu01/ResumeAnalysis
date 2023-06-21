<template>
  <div class="show">
    <el-button @click="resetDateFilter">清除日期过滤器</el-button>
    <el-button @click="clearFilter">清除所有过滤器</el-button>
    <el-table
      ref="filterTable"
      :data="tableData"
      height="740"
      border   
      style="width: 100%; height: 80%;">
      <el-table-column
        prop="date"
        label="日期"
        sortable
        width="180"
        column-key="date"
        :filters="[{text: '2016-05-01', value: '2016-05-01'}, {text: '2016-05-02', value: '2016-05-02'}, {text: '2016-05-03', value: '2016-05-03'}, {text: '2016-05-04', value: '2016-05-04'}]"
        :filter-method="filterHandler"
      >
      </el-table-column>
      <el-table-column
        prop="name"
        label="姓名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="age"
        label="年龄"
        width="180"
        >
      </el-table-column>
      <el-table-column
        prop="edu"
        label="最高学历"
        width="180">
      </el-table-column>
      <el-table-column
        prop="school"
        label="毕业院校"
        
        :formatter="formatter">
      </el-table-column>
      <el-table-column
        prop="wordingyears"
        label="工作年限"
        width="180">
      </el-table-column>
      <!-- <el-table-column
        prop="tag"
        label="标签"
        width="100"
        :filters="[{ text: '家', value: '家' }, { text: '公司', value: '公司' }]"
        :filter-method="filterTag"
        filter-placement="bottom-end">
        <template slot-scope="scope">
          <el-tag
            :type="scope.row.tag === '家' ? 'primary' : 'success'"
            disable-transitions>{{scope.row.tag}}</el-tag>
        </template>
      </el-table-column> -->
      <el-table-column label="操作" width="200">
      <template slot-scope="scope">
        <el-button
          size="mini"
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },{
          date: '2016-05-02',
          name: '王小虎',
          age: '22',
          edu: '本科',
          school: '北京师范大学',
          wordingyears: '6',
        },]
      }
    },
    methods: {
      resetDateFilter() {
        this.$refs.filterTable.clearFilter('date');
      },
      clearFilter() {
        this.$refs.filterTable.clearFilter();
      },
      formatter(row, column) {
        return row.school;
      },
      // filterTag(value, row) {
      //   return row.tag === value;
      // },
      filterHandler(value, row, column) {
        const property = column['property'];
        return row[property] === value;
      },
      handleEdit(index, row) {
        console.log(index, row);
      },
      handleDelete(index, row) {
        console.log(index, row);
      },
      fetchResumes(){
        // 这边就是获取数据，然后存放到tableDate中 
      }
    },
    mounted() {
      // 在组件挂载后，可以通过异步请求获取后端的简历数据
      // 这里只是一个示例，你需要根据实际情况修改
      this.fetchResumes();
    }
  }
</script>

<style>
.show{
  width: 90%;  
  height: 90%;  
  background-color:rgba(240, 240, 240, 0.8);
  padding: 10px;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.4); 
  border: 1px solid rgba(0, 0, 0, 0.1); 
}
</style>