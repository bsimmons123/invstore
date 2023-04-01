module.exports = {
  outputDir: '../dist',

  // relative to outputDir
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
    },
  },
};
