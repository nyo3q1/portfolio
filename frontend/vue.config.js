module.exports = {
    assetsDir: 'static',
    devServer: {
        proxy: process.env.VUE_APP_BACKEND_ORIGIN
    }
}
