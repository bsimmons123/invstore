module.exports = {
  outputDir: '../dist',

  // relative to outputDir
  assetsDir: 'static',
  devServer: {
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:5000/api/', // replace with your backend server URL
        changeOrigin: true,
        pathRewrite: {
          '^/api': '',
        },
      },
    },
  },
};
