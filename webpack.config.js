const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const webpack = require("webpack");
const BundleTracker = require("webpack-bundle-tracker");
// const BundleAnalyzerPlugin = require('webpack-bundle-analyzer').BundleAnalyzerPlugin;

module.exports = {
    mode: 'production',
    devtool: false,
    watch: false,
    context: __dirname,
    entry: './static/static_src/js/index.js',
    output: {
        // filename: 'bundle.js', // Output JS file
        path: path.resolve(__dirname, './static/static_build/'), // Output directory
        // publicPath: "auto",
        filename: "[name]-[contenthash].js",
        clean: true,  // Cleans old files
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: [
                    MiniCssExtractPlugin.loader,
                    'css-loader',
                    'postcss-loader', // Use PostCSS for Tailwind
                ],
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif|webp)$/i,
                type: 'asset/resource',
            },
            {
                test: /\.(woff|woff2|eot|ttf)$/i,
                type: 'asset/resource',
                generator: {
                    filename: 'fonts/[name][ext][query][contenthash:8]', // Add contenthash
                },
            },
        ],
    },
    plugins: [
        new MiniCssExtractPlugin({
            filename: 'styles.css', // Output CSS file
        }),
        new BundleTracker({ path: __dirname, filename: "webpack-stats.json" }),
        // new BundleAnalyzerPlugin({
        //     analyzerPort: 9999,  // Change this to an available port
        // }),
    ],
};