// Load Gulp
var gulp    = require('gulp'),
    rename   = require('gulp-rename'),
    gutil   = require('gulp-util'),
    plugins = require('gulp-load-plugins')();

// Start Watching: Run "gulp"
gulp.task('default', ['watch']);

// Less to CSS: Run manually with: "gulp build-css"
gulp.task('build-css', function() {
    return gulp.src('less/app.less')
        .pipe(plugins.plumber())
        .pipe(plugins.less())
        .on('error', function (err) {
            gutil.log(err);
            gutil.log('hello')
            this.emit('end');
        })
        .pipe(plugins.autoprefixer(
            {
                browsers: [
                    '> 1%',
                    'last 2 versions',
                    'firefox >= 4',
                    'safari 7',
                    'safari 8',
                    'IE 8',
                    'IE 9',
                    'IE 10',
                    'IE 11'
                ],
                cascade: false
            }
        ))
        .pipe(plugins.cssmin())
        .pipe(gulp.dest('./static/css/')).on('error', gutil.log)
        .pipe(plugins.livereload());
});

gulp.task('js-reload', function () {
    return gulp.src('site-static/frontend/js/**/*.js')
            .pipe(plugins.livereload());
});

gulp.task('html-reload', function () {
    return gulp.src('./**/*.html')
            .pipe(plugins.livereload());
});


// Default task
gulp.task('watch', function() {
    plugins.livereload.listen();
    gulp.watch('less/**/*.less', ['build-css']);
    gulp.watch('js/**/*.js', ['js-reload'])
    gulp.watch('./**/*.html', ['html-reload'])
});
