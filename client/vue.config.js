module.exports = {
  outputDir: '../dist',
  pages: {
    index: {
      entry: 'src/defaultapp/main.js',
      template: 'public/index.html',
      filename: 'index.html',
      title: 'Index Page',
      chunks: ['chunk-vendors', 'chunk-common', 'index'],
    },
  },
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
      '/api': {
        target: 'http://127.0.0.1:5000/api',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
    },
  },
};
