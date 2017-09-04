// standard webpack configuration

var path = require('path');
var webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

process.traceDeprecation = true; 

module.exports = {
  entry: {
    bundle: __dirname + '/static/app.js'
  },
  
  output: {
    path: __dirname + '/static/build',
    filename: '[name].js'
  },
  module: {
    loaders: [ // tools webpack uses to load different file types
      {
        test: /\.js$/, // check if .js
        exclude: /(node_modules|bower_components)/,
        loader: 'babel-loader', // if so, use this loader
        query: {
          presets: ['es2016', 'es2015', 'react', 'stage-0']
        }
      },
      { test: /\.json/, loader: 'json-loader'},
      // { test: /\.css$/, loader: 'style-loader!css-loader' },
      { test: /\.png$/, loader: 'url-loader?limit=100000' },
      { test: /\.svg$/, loader: 'url-loader?limit=100000' },

      {
        test: /\.css$/,
        loader: ExtractTextPlugin.extract('css-loader')
      },

      {
        test: /\.scss$/,
        loader: ExtractTextPlugin.extract('css-loader!sass-loader')
      }
    ]
  },
  plugins: [
    new ExtractTextPlugin({ 
      filename: 'styles.css', 
      disable: false,
      allChunks: true
    }),
    new webpack.EnvironmentPlugin([ // gets environmental variables from shell
    ])
  ],

  resolve: {
    modules: ['bower_components', 'node_modules'],
    descriptionFiles: ["package.json", "bower.json"],
  // you can now require('file') instead of require('file.coffee')
    extensions: ['.js', '.jsx', '.json', '.coffee']
  },

  node: { // fixes some sort of bug
     fs: "empty"
  }
}