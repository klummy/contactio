var gulp            = require('gulp'),
    $               = require('gulp-load-plugins')(),
    browserSync     = require('browser-sync'),
    reload          = browserSync.reload;


gulp.task('browser-sync', function() {
  browserSync({
    open: false,
    notify: false,
    server: { baseDir: "./assets" }
  });
});

gulp.task('jade', function() {
  return gulp.src('src/*.jade')
    .pipe($.plumber())
    .pipe($.jade({ pretty: true }))
    .pipe(gulp.dest('assets/'))
});

gulp.task('sass', function() {
  return gulp.src('src/styles/*.scss')
    .pipe($.sourcemaps.init())
      .pipe($.sass().on('error', $.sass.logError))
    .pipe($.autoprefixer({
      browsers: ['> 3% in NG'],
    }))
    .pipe($.sourcemaps.write())
    .pipe(gulp.dest('assets/styles'))
});

gulp.task('scripts', function() {
  return gulp.src('src/scripts/bin/*.js')
    .pipe($.sourcemaps.init())
      .pipe($.concat('app.js'))
    .pipe($.uglify())
    .pipe(gulp.dest('assets/scripts/'))
});

gulp.task('images', function() {
  return gulp.src("src/images/**/*")
    .pipe($.imagemin({
      progressive: true
    }))
    .pipe(gulp.dest("assets/"))
});

gulp.task('build', ['jade', 'scripts', 'sass', 'images']);

gulp.task('serve', ['build', 'browser-sync'], function() {
  gulp.watch('src/**/*.jade',['jade', reload]);
  gulp.watch('src/scripts/*.js',['scripts', reload]);
  gulp.watch('src/styles/**/*.scss',['sass', reload]);
  gulp.watch('src/images/**/*',['images', reload]);
});
