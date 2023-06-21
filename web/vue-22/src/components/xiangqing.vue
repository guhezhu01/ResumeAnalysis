<template>
  <div class="view">
    <!-- <v-chart class="chart" :option="option" />
    <div ref="main" style="width: 500px;height:400px;"></div>
    <div ref="first" style="width: 500px;height:400px;"></div> -->
    <div class="edub" ref="edub"></div>
    <div class="experience" ref="experience"></div>
    <div class="age" ref="age"></div>
    <div id="scatter" class="scatter" ref="scatter"></div>
    <div id="map" class="map" ref="map"></div>
  </div>
</template>

<script>
import '@/assets/china'
export default {
  name: "HelloWorld",
  components: {
    // VChart
  },
  provide: {
    // [THEME_KEY]: "dark"
  },
  // data() {
  // },
  mounted() {
    // 请求数据
    this.getDate() //获取数据并展示到页面上。
    const data = [5, 20, 36, 10, 10, 20]
    this.$nextTick(() => {
      // this.init(data)
      // this.firsttest()
      this.edub()
      this.experience()
      this.age()
      this.scatter()
      this.map()
    })
  },
  methods: {
    getDate(){
      // 这边获取的数据可以和单个统计一样直接先给我，我这边实现，或者你和张泽宇沟通下，就是图里面的数据是怎么呈现的，直接处理好传给我也行
    },
    // init(data) {
    // // this.fetchResumes();
    // //  // 第三步 初始化 echarts
    //   var myChart = this.$echarts.init(this.$refs['main'])
    //     // 这儿是一个折线图的小demo
    //   var option = {
    //         title: {
    //             text: 'ECharts 入门示例'
    //         },
    //         tooltip: {},
    //         legend: {
    //             data: ['销量']
    //         },
    //         xAxis: {
    //             data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    //         },
    //         yAxis: {},
    //         series: [{
    //             name: '销量',
    //             type: 'line',
    //             data: data
    //         }]
    //   }
    //   // 第五步 使用刚指定的配置项和数据显示图表。
    //   myChart.setOption(option)
    // },
    // firsttest(){
    //   //++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    //   var myChartf = this.$echarts.init(this.$refs['first'])
    //   // 第四步 准备数据和配置项
    //   // 这儿是一个圆角环形图的小demo
    //   var option = {
    //   tooltip: {
    //     trigger: 'item'
    //   },
    //   legend: {
    //     top: '5%',
    //     left: 'center'
    //   },
    //   series: [
    //     {
    //       name: 'Access From',
    //       type: 'pie',
    //       radius: ['40%', '70%'],
    //       avoidLabelOverlap: false,
    //       itemStyle: {
    //         borderRadius: 10,
    //         borderColor: '#fff',
    //         borderWidth: 2
    //       },
    //       label: {
    //         show: false,
    //         position: 'center'
    //       },
    //       emphasis: {
    //         label: {
    //           show: true,
    //           fontSize: 40,
    //           fontWeight: 'bold'
    //         }
    //       },
    //       labelLine: {
    //         show: false
    //       },
    //       data: [
    //         { value: 1048, name: 'Search Engine' },
    //         { value: 735, name: 'Direct' },
    //         { value: 580, name: 'Email' },
    //         { value: 484, name: 'Union Ads' },
    //         { value: 300, name: 'Video Ads' }
    //       ]
    //     }
    //   ]
    // };
    //   // 第五步 使用刚指定的配置项和数据显示图表。
    //   myChartf.setOption(option)
    // },

    edub() {
      var myChart = this.$echarts.init(this.$refs['edub'])

      var option = {
        title: {
          text: '求职者最高学历',
          x : 'center',
          y : 'bottom',
        },
        tooltip: {
          trigger: 'item',
          formatter: '{a} <br/>{b} : {c}%'
        },
        toolbox: {
          feature: {
            dataView: { readOnly: false },
            restore: {},
            saveAsImage: {}
          }
        },
        legend: {
          data: ['高中/中专', '专科', '本科', '硕士', '博士']
        },
        series: [
          {
            name: '最高学历',
            type: 'funnel',
            left: '10%',
            radius: ['0%', '60%'],
            top: 60,
            bottom: 60,
            width: '80%',
            min: 0,
            max: 100,
            minSize: '0%',
            maxSize: '100%',
            sort: 'descending',
            gap: 2,
            label: {
              show: true,
              position: 'inside'
            },
            labelLine: {
              length: 10,
              lineStyle: {
                width: 1,
                type: 'solid'
              }
            },
            itemStyle: {
              borderColor: '#fff',
              borderWidth: 1
            },
            emphasis: {
              label: {
                fontSize: 20
              }
            },
            data: [
              { value: 60, name: '本科' },
              { value: 40, name: '硕士' },
              { value: 20, name: '博士' },
              { value: 80, name: '专科' },
              { value: 100, name: '高中/中专' }
            ]
          }
        ]
      };
      myChart.setOption(option)
    },
    experience() {
      var myChart = this.$echarts.init(this.$refs['experience'])
      // 这儿是一个折线图的小demo
      var option = {
        title: {
          text: '求职者求职者工作经验'
        },
        legend: {
          top: 'bottom'
        },
        toolbox: {
          show: true,
          feature: {
            mark: { show: true },
            dataView: { show: true, readOnly: false },
            restore: { show: true },
            saveAsImage: { show: true }
          }
        },
        series: [
          {
            name: 'Nightingale Chart',
            type: 'pie',
            radius: ['0%', '80%'],
            center: ['50%', '50%'],
            roseType: 'area',
            itemStyle: {
              borderRadius: 8
            },
            data: [
              { value: 40, name: '无经验' },
              { value: 35, name: '3个月以内' },
              { value: 32, name: '6个月' },
              { value: 30, name: '1年' },
              { value: 25, name: '2年' },
              { value: 19, name: '3年' },
              { value: 13, name: '5年' },
              { value: 10, name: '10年' }
            ]
          }
        ]
      };
      // 第五步 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    age() {
      var myChart = this.$echarts.init(this.$refs['age'])
      // 这儿是一个折线图的小demo
      var option = {
        title: {
          text: '求职者求职者年龄分布'
        },
        tooltip: {
          trigger: 'item'
        },
        legend: {
          top: '5%',
          left: 'center'
        },
        series: [
          {
            name: '年龄',
            type: 'pie',
            radius: ['30%', '60%'],
            avoidLabelOverlap: false,
            itemStyle: {
              borderRadius: 10,
              borderColor: '#fff',
              borderWidth: 2
            },
            label: {
              show: false,
              position: 'center'
            },
            emphasis: {
              label: {
                show: true,
                fontSize: 40,
                fontWeight: 'bold'
              }
            },
            labelLine: {
              show: false
            },
            data: [
              { value: 672, name: '18-21岁' },
              { value: 436, name: '22-25岁' },
              { value: 298, name: '26-30岁' },
              { value: 124, name: '31-39岁' },
              { value: 50, name: '40岁及以上' }
            ]
          }
        ]
      };
      // 第五步 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option)
    },
    scatter() {
      var chartDom = document.getElementById('scatter');
      var myChart = this.$echarts.init(chartDom);
      var option;

      // prettier-ignore
      const femaleData = [
        [23, 0], [27, 0], [22, 0], [23, 0], [24, 1], [23, 0], [25, 1], [27, 2],
        [29, 5], [22, 0], [35, 11], [26, 2], [23, 1], [22, 0], [23, 0], [21, 0],
        [20, 0], [21, 1], [22, 0], [23, 1], [25, 2], [27, 4], [29, 2], [32, 9],
        [28, 3], [29, 6], [22, 1], [23, 0], [18, 13], [18, 12], [20, 1], [21, 0],
        [22, 9], [23, 8], [25, 7], [20, 0], [29, 5], [27, 4], [27, 3], [18, 0],
        [25, 2], [27, 6], [29, 5], [31, 7], [33, 3], [36, 12], [22, 1], [18, 0],
        [18, 0], [18, 0], [18, 0], [18, 0], [18, 0], [18, 0], [18, 0], [18, 0], [18, 0]
      ];
      // prettier-ignore
      const maleDeta = [
        [18, 0], [18, 0], [20, 1], [21, 0], [22, 0], [23, 0], [24, 0],
        [26, 2], [28, 5], [32, 10], [35, 11], [39, 16], [42, 18], [24, 0], [18, 0],
        [18, 0], [18, 0], [20, 0], [21, 0], [22, 0], [23, 1], [24, 1], [26, 2],
        [28, 5], [32, 8], [27, 3], [26, 2], [23, 1], [22, 0], [26, 3], [18, 0],
        [18, 0], [18, 0], [20, 1], [21, 0], [22, 0], [23, 0], [24, 0],
        [26, 2], [28, 5], [32, 10], [35, 11], [39, 16], [42, 18], [24, 0], [18, 0],
        [18, 0], [18, 0], [20, 0], [21, 0], [22, 0], [23, 1], [24, 1], [26, 2],
        [28, 5], [32, 8], [27, 3], [26, 2], [23, 1], [22, 0], [26, 3], [18, 0],
        [18, 0], [18, 0], [20, 0], [21, 0], [22, 0], [23, 1], [24, 1], [26, 2],
        [28, 5], [32, 8], [27, 3], [26, 2], [23, 1], [22, 0], [26, 3], [18, 0],
        [18, 0], [18, 0], [20, 1], [21, 0], [22, 0], [23, 0], [24, 0],
        [26, 2], [28, 5], [32, 10], [35, 11], [39, 16], [42, 30], [24, 0], [18, 0],
      ];
      function calculateAverage(data, dim) {
        let total = 0;
        for (var i = 0; i < data.length; i++) {
          total += data[i][dim];
        }
        return (total /= data.length);
      }
      const scatterOption = (option = {
        xAxis: {
          type: 'value',
          name: '年龄/岁',
          scale: true
        },
        yAxis: {
          type: 'value',
          name: '工作经验/年',
          scale: true
        },
        series: [
          {
            type: 'scatter',
            id: 'female',
            radius: ['0%', '80%'],
            dataGroupId: 'A',
            itemStyle: {
              color: '#ee6666'
            },
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: femaleData
          },
          {
            type: 'scatter',
            id: 'male',
            dataGroupId: 'B',
            itemStyle: {
              color: '#5470c6'
            },
            universalTransition: {
              enabled: true,
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            },
            data: maleDeta
          }
        ]
      });
      const barOption = {
        xAxis: {
          type: 'category',
          data: ['女', '男']
        },
        yAxis: {
          name: '平均年龄/岁'
        },
        series: [
          {
            type: 'bar',
            id: 'total',
            radius: ['0%', '80%'],

            data: [
              {
                value: calculateAverage(maleDeta, 0),
                groupId: 'A',
                itemStyle: {
                  color: '#ee6666'
                }
              },
              {
                value: calculateAverage(femaleData, 0),
                groupId: 'B',
                itemStyle: {
                  color: '#5470c6'
                }
              }
            ],
            universalTransition: {
              enabled: true,
              seriesKey: ['female', 'male'],
              delay: function (idx, count) {
                return Math.random() * 400;
              }
            }
          }
        ]
      };
      let currentOption = scatterOption;
      setInterval(function () {
        currentOption = currentOption === scatterOption ? barOption : scatterOption;
        myChart.setOption(currentOption, true);
      }, 2000);
      myChart.setOption(currentOption, true);

    },
    map() {
      var myChart = this.$echarts.init(document.getElementById("map"));
      //准备option对象
      var option = {
        title: {
          top: 40,
          text: '求职人员城市分布图',
          //副标题
          subtext: 'By:张泽宇',
          left: 'center'
        },
        tooltip: {
          trigger: 'item'
        },

        toolbox: {
          feature: {
            saveAsImage: {
              title: '保存图片'
            },
            dataView: {},
            dataZoom: {},
            restore: {}

          }
        },
        //视觉映射组件
        visualMap: {
          //
          calculable: true,
          min: 0,
          max: 1500,
          left: 30,
          bottom: 100,
          text: ['高', '低'], // 文本，默认为数值文本
          inRange: {
            color: ['#e0f3fc', '#1266D0'] // 视觉映射颜色范围
          }
        },
        series: [{
          name: '求职人数',
          type: 'map',
          mapType: 'china',
          roam: true,
          data: [{
            value: 1430,
            name: '江苏'
          }, {
            value: 940,
            name: '山东'
          },
          {
            value: 984,
            name: '河南'
          },
          {
            value: 912,
            name: '安徽'
          }, {
            value: 1112,
            name: '浙江'
          },
          {
            value: 612,
            name: '江西'
          },
          {
            value: 123,
            name: '上海'
          }, {
            value: 321,
            name: '武汉'
          }, {
            value: 200,
            name: '河北'
          }, {
            value: 300,
            name: '山西'
          }, {
            value: 435,
            name: '湖南'
          }, {
            value: 580,
            name: '湖北'
          }, {
            value: 2,
            name: '甘肃'
          }, {
            value: 35,
            name: '青海'
          }, {
            value: 80,
            name: '四川'
          }, {
            value: 24,
            name: '云南'
          }, {
            value: 60,
            name: '广西'
          }, {
            value: 48,
            name: '贵州'
          }, {
            value: 235,
            name: '重庆'
          }, {
            value: 2,
            name: '内蒙古'
          }, {
            value: 84,
            name: '陕西'
          }, {
            value: 80,
            name: '黑龙江'
          }, {
            value: 300,
            name: '福建'
          }

          ],

          emphasis: {
            label: {
              show: true,
              color: '#053E86', // 文字颜色
            },
            itemStyle: {
              areaColor: '#89F7FF', // 区域颜色
            }
          }

        }]
      };
      // 使用刚指定的配置项和数据显示图表。
      myChart.setOption(option);
    }
  }
};
</script>

<style>
.view {
  /* position: relative; */
  /* 设置父容器为相对定位 */
  /* background-image: url("../assets/background3.jpg"); */
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  /* display: flex; */
  /* justify-content: center; */
  /* align-items: center; */
  /* flex-direction: column; */
  background-image: url("../assets/blue3.png");
  /* z-index: 0000; */
}

.edub,
.experience,
.age,
.map,
.scatter {
  position: absolute;
  /* 设置子元素为绝对定位 */
}

.edub {
  top: 20px;
  /* 距离顶部的偏移量 */
  right: 10px;
  /* 距离左侧的偏移量 */
  width: 432px;
  height: 472px;
  /* 其他样式 */
  border-radius: 10px; /* 圆角半径 */
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */
  backdrop-filter: blur(5px); /* 磨砂玻璃效果 */
}

.experience {
  top: 20px;
  /* 距离顶部的偏移量 */
  left: 80px;
  /* 距离左侧的偏移量 */
  width: 400px;
  height: 360px;
  /* 其他样式 */
  border-radius: 10px; /* 圆角半径 */
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */
  backdrop-filter: blur(5px); /* 磨砂玻璃效果 */
}

.age {
  top: 500px;
  left: 80px;
  width: 500px;
  height: 400px;
  border-radius: 10px; /* 圆角半径 */
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */
  backdrop-filter: blur(5px); /* 磨砂玻璃效果 */
}

.map{
  top: 220px;
  /* 距离顶部的偏移量 */
  left: 635px;
  /* 距离左侧的偏移量 */
  width: 700px;
  height: 550px;
  /* 其他样式 */
}

.scatter {
  top: 530px;
  /* 距离顶部的偏移量 */
  right: 10px;
  /* 距离左侧的偏移量 */
  width: 500px;
  height: 350px;
  /* 其他样式 */
  border-radius: 10px; /* 圆角半径 */
  box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.5); /* 阴影效果 */
  backdrop-filter: blur(5px); /* 磨砂玻璃效果 */
}</style>
