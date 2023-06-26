
``` js
var chartDom = document.getElementById('main');
var myChart = echarts.init(chartDom);
var option;

// prettier-ignore
const femaleData = [
  [23, 0],[27, 0],[22, 0],[23, 0],[24, 1],[23, 0],[25, 1],[27, 2],
  [29, 5],[22, 0],[35, 11],[26, 2],[23, 1],[22, 0],[23, 0],[21, 0],
  [20, 0],[21, 1],[22, 0],[23, 1],[25, 2],[27, 4],[29, 2],[32, 9],
  [28, 3],[29, 6],[22, 1],[23, 0],[18, 13],[18, 12],[20, 1],[21,0 ],
  [22, 9],[23, 8],[25, 7],[20, 0],[29, 5],[27, 4],[27, 3],[18,0],
  [25, 2],[27, 6],[29, 5],[31, 7],[33, 3],[36, 12],[22, 1],[18,0],
  [18,0],[18,0],[18,0],[18,0],[18,0],[18,0],[18,0],[18,0],[18,0]
];
// prettier-ignore
const maleDeta = [
  [18, 0],[18, 0],[20, 1],[21, 0],[22, 0],[23, 0],[24, 0],
  [26, 2],[28, 5],[32, 10],[35, 11],[39, 16],[42, 18],[24, 0],[18, 0],
  [18, 0],[18, 0],[20, 0],[21, 0],[22, 0],[23, 1],[24, 1],[26, 2],
  [28, 5],[32, 8],[27, 3],[26, 2],[23, 1],[22, 0],[26, 3],[18, 0],
  [18, 0],[18, 0],[20, 1],[21, 0],[22, 0],[23, 0],[24, 0],
  [26, 2],[28, 5],[32, 10],[35, 11],[39, 16],[42, 18],[24, 0],[18, 0],
  [18, 0],[18, 0],[20, 0],[21, 0],[22, 0],[23, 1],[24, 1],[26, 2],
  [28, 5],[32, 8],[27, 3],[26, 2],[23, 1],[22, 0],[26, 3],[18, 0],
  [18, 0],[18, 0],[20, 0],[21, 0],[22, 0],[23, 1],[24, 1],[26, 2],
  [28, 5],[32, 8],[27, 3],[26, 2],[23, 1],[22, 0],[26, 3],[18, 0],
  [18, 0],[18, 0],[20, 1],[21, 0],[22, 0],[23, 0],[24, 0],
  [26, 2],[28, 5],[32, 10],[35, 11],[39, 16],[42, 30],[24, 0],[18, 0],
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

option && myChart.setOption(option);

下面是单独的js代码：
// prettier-ignore
const femaleData = [
  [23, 0],[27, 0],[22, 0],[23, 0],[24, 1],[23, 0],[25, 1],[27, 2],
  [29, 5],[22, 0],[35, 11],[26, 2],[23, 1],[22, 0],[23, 0],[21, 0],
  [20, 0],[21, 1],[22, 0],[23, 1],[25, 2],[27, 4],[29, 2],[32, 9],
  [28, 3],[29, 6],[22, 1],[23, 0],[18, 13],[18, 12],[20, 1],[21,0 ],
  [22, 9],[23, 8],[25, 7],[20, 0],[29, 5],[27, 4],[27, 3],[18,0],
  [25, 2],[27, 6],[29, 5],[31, 7],[33, 3],[36, 12],[22, 1],[18,0],
  [18,0],[18,0],[18,0],[18,0],[18,0],[18,0],[18,0],[18,0],[18,0]
];
// prettier-ignore
const maleDeta = [
  [18, 0],[18, 0],[20, 1],[21, 0],[22, 0],[23, 0],[24, 0],
  [26, 2],[28, 5],[32, 10],[35, 11],[39, 16],[42, 18],[24, 0],[18, 0],
  [18, 0],[18, 0],[20, 0],[21, 0],[22, 0],[23, 1],[24, 1],[26, 2],
  [28, 5],[32, 8],[27, 3],[26, 2],[23, 1],[22, 0],[26, 3],[18, 0],
  [18, 0],[18, 0],[20, 1],[21, 0],[22, 0],[23, 0],[24, 0],
  [26, 2],[28, 5],[32, 10],[35, 11],[39, 16],[42, 18],[24, 0],[18, 0],
  [18, 0],[18, 0],[20, 0],[21, 0],[22, 0],[23, 1],[24, 1],[26, 2],
  [28, 5],[32, 8],[27, 3],[26, 2],[23, 1],[22, 0],[26, 3],[18, 0],
  [18, 0],[18, 0],[20, 0],[21, 0],[22, 0],[23, 1],[24, 1],[26, 2],
  [28, 5],[32, 8],[27, 3],[26, 2],[23, 1],[22, 0],[26, 3],[18, 0],
  [18, 0],[18, 0],[20, 1],[21, 0],[22, 0],[23, 0],[24, 0],
  [26, 2],[28, 5],[32, 10],[35, 11],[39, 16],[42, 30],[24, 0],[18, 0],
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
    name : '年龄/岁',
    scale: true
  },
  yAxis: {
    type: 'value',
    name : '工作经验/年',
    scale: true
  },
  series: [
    {
      type: 'scatter',
      id: 'female',
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
```