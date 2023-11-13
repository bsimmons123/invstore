module.exports = {
  publicPath: '/',
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
      '/api': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
      '/login': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
      '/callback': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
      '/logout': {
        target: 'http://127.0.0.1:5000/',
        changeOrigin: true,
        ws: false,
        webSocketTimeout: 60000,
      },
    },
  },
};
