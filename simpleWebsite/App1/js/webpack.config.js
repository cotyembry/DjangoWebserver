const WebpackShellPlugin = require('webpack-shell-plugin');
//Current build path represents where the file needs to go to
var MOVE_FILE_TO = 'Y:/marsjs/js/build/distribute';
var RECOMPILE_ON_THIS_FILE = MOVE_FILE_TO + '/bundle.js';
var shellCommand2 = 'mv ./dist/bundle.js ' + MOVE_FILE_TO;
var _onBuildEnd = shellCommand2;

module.exports = {
  entry: './js/index.js',
  output: {
    path: __dirname,
    filename: './dist/bundle.js'
  },
  module: {
    loaders: [
        {
            test: /\.jsx?$/,
            exclude: /node_modules/,
            loader: 'babel-loader',
            query: {
              plugins: ['transform-runtime'],
              presets: ['es2015', 'stage-0', 'react'],
            }
        },
        {
            test: /\.css$/,
            loader: 'style-loader'
        },
        {
            test: /\.css$/,
            loader: 'css-loader',
            query: {
              modules: true,
              localIdentName: '[name]__[local]__[hash:base64:5]'
            }
        }
    ]
  },
  plugins: [
    // new WebpackShellPlugin({onBuildStart:['echo "Webpack Start"'], onBuildEnd:['echo "Webpack End"']})
    new WebpackShellPlugin({onBuildStart:['echo "Webpack Start"'], onBuildEnd:[_onBuildEnd]})
  ]
}
