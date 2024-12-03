const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const rename = require('gulp-rename');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const cssnano = require('cssnano');
const autoprefixer = require('autoprefixer');
const eslint = require('gulp-eslint');
const sasslint = require('gulp-sass-lint');
const browserify = require('browserify');
const babelify = require('babelify');
const source = require('vinyl-source-stream');
const streamify = require('gulp-streamify');
const uglify = require('gulp-uglify');

const styles = () => {
    const plugins = [autoprefixer(), cssnano()];

    return gulp.src(['./src/scss/main.scss'])
        .pipe(sass().on('error', sass.logError))
        .pipe(rename({ basename: 'green-audio-player' }))
        .pipe(gulp.dest('./dist/css'))
        .pipe(postcss(plugins))
        .pipe(rename({ suffix: '.min' }))
        .pipe(gulp.dest('./dist/css'))
        .pipe(browserSync.stream());
};

const scripts = () => browserify({
    entries: './index.js',
    standalone: 'GreenAudioPlayer'
}).transform(babelify, { presets: ['@babel/preset-env'] })
    .bundle()
    .pipe(source('green-audio-player.js'))
    .pipe(gulp.dest('dist/js'))
    .pipe(streamify(uglify()))
    .pipe(rename({ suffix: '.min' }))
    .pipe(gulp.dest('dist/js'))
    .pipe(browserSync.stream());

const scriptsLint = () => gulp.src('./src/js/*.js')
    .pipe(eslint())
    .pipe(eslint.format())
    .pipe(eslint.failAfterError());

const stylesLint = () => gulp.src('./src/scss/**/*.scss')
    .pipe(sasslint())
    .pipe(sasslint.format())
    .pipe(sasslint.failOnError());

const startServer = () => browserSync.init({
    server: {
        baseDir: './'
    }
});

const watchHTML = () => gulp.watch('./*.html').on('change', browserSync.reload);
const watchScripts = () => gulp.watch('./src/js/*.js', gulp.series(scriptsLint, scripts));
const watchStyles = () => gulp.watch('./src/scss/**/*.scss', gulp.series(stylesLint, styles));

const compile = gulp.parallel(styles, scripts);
const lint = gulp.parallel(scriptsLint, stylesLint);
const serve = gulp.series(compile, startServer);
const watch = gulp.parallel(watchHTML, watchScripts, watchStyles);
const defaultTasks = gulp.parallel(serve, watch);

exports.styles = styles;
exports.scripts = scripts;
exports.scriptsLint = scriptsLint;
exports.stylesLint = stylesLint;
exports.watchHTML = watchHTML;
exports.watchScripts = watchScripts;
exports.watchStyles = watchStyles;
exports.startServer = startServer;
exports.serve = serve;
exports.watch = watch;
exports.compile = compile;
exports.lint = lint;
exports.default = defaultTasks;
