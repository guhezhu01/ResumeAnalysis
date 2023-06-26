const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  // chainWebpack: (config) => {
  //   config.externals({
  //     echarts: 'echarts',
  //   });
  // },
  // configureWebpack: {
  //   resolve: {
  //     alias: {
  //       // 'echarts$': 'echarts/dist/echarts.js'
  //     }
  //   }
  // }
});
