module.exports = {
  publicPath: '/',
  outputDir: '../dist',
  // relative to outputDir
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
    },
  },
};
