var path = require('path')

module.exports = {
  node: {
    fs: 'empty'
  },
  entry: {
    app: './src/app.js'
  },
  output: {
    path: path.resolve(__dirname, '../dist/static'),
    publicPath: '/static/',
    filename: '[name].js'
  },
  externals: {
    'jquery': 'jQuery'
  },
  resolve: {
    alias: {
      'src': path.resolve(__dirname, '../src'),
//      'JQueryUI': path.resolve(__dirname, '../node_modules/jquery-ui/ui/core.js'),
//      'JQueryBaResize': path.resolve(__dirname, '../src/dependencies/jquery-resize/jquery.ba-resize.js'),
//      'Bootstrap': path.resolve(__dirname, '../node_modules/bootstrap/dist/js/bootstrap.js'),
//      'BootstrapTable': path.resolve(__dirname, '../node_modules/bootstrap-table/dist/bootstrap-table.js'),
//      'BootstrapTableLocale': path.resolve(__dirname, '../node_modules/bootstrap-table/dist/bootstrap-table-locale-all.js'),
//      'BootstrapTableExport': path.resolve(__dirname, '../node_modules/bootstrap-table/dist/extensions/export/bootstrap-table-export.js'),
//      'BootstrapTableEditable': path.resolve(__dirname, '../node_modules/bootstrap-table/dist/extensions/editable/bootstrap-table-editable.js'),
//      'BootstrapTableFilterControl': path.resolve(__dirname, '../node_modules/bootstrap-table/dist/extensions/filter-control/bootstrap-table-filter-control.js'),
//      'TableExport': path.resolve(__dirname, '../src/dependencies/TableExport/dist/TableExport.js'),
//      'JqueryValidation': path.resolve(__dirname, '../node_modules/jquery-validation/dist/jquery.validate.js'),
//      'JqueryValidationZH': path.resolve(__dirname, '../node_modules/jquery-validation/dist/localization/messages_zh.js'),
//      'BootstrapDialog': path.resolve(__dirname, '../node_modules/bootstrap-dialog/dist/js/bootstrap-dialog.js'),
//      'BootstrapDatepicker': path.resolve(__dirname, '../node_modules/bootstrap-datepicker/dist/js/bootstrap-datepicker.js'),
//      'BootstrapDatepickerCN': path.resolve(__dirname, '../node_modules/bootstrap-datepicker/dist/locales/bootstrap-datepicker.zh-CN.min.js'),
//      'Slimscroll': path.resolve(__dirname, '../node_modules/jquery-slimscroll/jquery.slimscroll.min.js'),
//      'BootstrapValidator': path.resolve(__dirname, '../src/dependencies/bootstrapvalidator/dist/js/bootstrapValidator.min.js'),
//      'BootstrapValidatorCN': path.resolve(__dirname, '../src/dependencies/bootstrapvalidator/dist/js/language/zh_CN.js'),
      'commonFunc': path.resolve(__dirname, '../src/assets/js/common.js'),
      'vuexStore': path.resolve(__dirname, '../src/vuex/store.js'),
      'vuexGetters': path.resolve(__dirname, '../src/vuex/getters.js'),
      'vuexActions': path.resolve(__dirname, '../src/vuex/actions.js'),
      'vuexActionsTypes': path.resolve(__dirname, '../src/vuex/mutation-types.js'),
      'lodopPrintFunc': path.resolve(__dirname, '../src/assets/js/LodopFuncs.js'),
      'billPrintFunc': path.resolve(__dirname, '../src/assets/js/billPrint.js')
    },
    extensions: ['', '.js', '.vue', '.less']
  },
  resolveLoader: {
    root: path.join(__dirname, 'node_modules')
  },
  module: {
    loaders: [
      {
        test: /\.vue$/,
        loader: 'vue'
      },
      {
        test: /\.js$/,
        exclude: /node_modules|vue\/dist|vue-router\/|vue-loader\/|vue-hot-reload-api\//,
        loader: 'babel',
        query: {compact: false}
      },
      {
        test: /\.json$/,
        loader: 'json'
      },
      {
        test: /\.less$/,
        loader: 'css!less'
      },
      {
        test: /\.scss$/,
        loader: "style!css!sass"
      },
      {
        test: /\.css$/,
        loader: 'css'

      },
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'url',
        query: {
          limit: 10000,
          name: '[name].[ext]?[hash]'
        }
      },
      {
        test: /\.(eot|woff|ttf|svg)\??.*$/,
        loader: 'url-loader?limit=30000&name=[name]-[hash].[ext]'
      },
      {
        test: /\.styl$/,
        loader: 'style-loader!css-loader!stylus-loader'
      }
    ]
  },
  vue: {
    loaders: {
      js: 'babel!eslint',
      less: 'vue-style!css!less',
      sass: 'vue-style!css!sass'
    }
  },
  eslint: {
    formatter: require('eslint-friendly-formatter')
  }
}
