<template>
  <div class="view" ref="container">
    <div class="echarts-chart" :style="{ width: chartWidth, height: chartHeight }" ref="chart"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts';

export default {
  data() {
    return {
      chartWidth: '100%',
      chartHeight: '100%',
      chartInstance: null
    };
  },
  mounted() {
    this.chartInstance = echarts.init(this.$refs.chart);

    // 监听容器大小变化
    this.resizeObserver = new ResizeObserver(() => {
      this.resizeChart();
    });
    this.resizeObserver.observe(this.$refs.container);

    // 初始化echarts图表
    this.initChart();
  },
  beforeUnmount() {
    this.resizeObserver.unobserve(this.$refs.container);
    this.resizeObserver.disconnect();
    this.chartInstance.dispose();
  },
  methods: {
    initChart() {
      // 初始化echarts图表的配置
      const chartOptions = {
        // echarts图表配置项
      };

      // 渲染echarts图表
      this.chartInstance.setOption(chartOptions);
    },
    resizeChart() {
      // 获取容器大小并设置echarts图表大小
      const containerWidth = this.$refs.container.offsetWidth;
      const containerHeight = this.$refs.container.offsetHeight;

      this.chartWidth = containerWidth + 'px';
      this.chartHeight = containerHeight + 'px';

      // 调整echarts图表大小
      this.chartInstance.resize();
    }
  }
};
</script>

<style>
.view {
  position: relative;
}

.echarts-chart {
  width: 100%;
  height: 100%;
}
</style>
