'use strict';
 
var gulp = require('gulp');
var sass = require('gulp-sass');
var babel = require("gulp-babel");
var concat = require('gulp-concat');
const minify = require('gulp-minify');
 
const paths = {
	styles: [
		// './node_modules/bulma/bulma.sass', 
		'./node_modules/animate.css/animate.min.css', 
		'./src/css/app.sass',
	],
	js: [
		'./src/js/app.js',
	],
	jslib: [
		'./node_modules/jquery/dist/jquery.min.js', 
		// './src/js/blotter.min.js',
		// './src/js/materials/channelSplitMaterial.js',
		// './src/js/materials/fliesMaterial.js',
		// './src/js/materials/liquidDistortMaterial.js',
		// './src/js/materials/rollingDistortMaterial.js',
		// './src/js/materials/slidingDoorMaterial.js',
	]
}

sass.compiler = require('node-sass');
 
gulp.task('style', function () {
  return gulp.src( paths.styles )
    .pipe(sass.sync().on('error', sass.logError))
    .pipe(concat('styles.css'))
    .pipe(gulp.dest('./assets/css'));
});
 

// gulp.task("jslib", function () {
//   return gulp.src( paths.jslib )
//     .pipe(babel())
//     .pipe(concat('lib.js'))
//     .pipe(minify())
//     .pipe(gulp.dest("./assets/js/"));
// });
gulp.task("js", function () {
  return gulp.src( paths.js )
    .pipe(babel())
    .pipe(minify())
    .pipe(gulp.dest("./assets/js/"));
});

gulp.task('watch', 
	gulp.series(function(){
		gulp.watch( paths.js, gulp.series( ['js'], function( done ){ done(); } ) )
		gulp.watch( paths.styles, gulp.series( ['style'], function( done ){ done(); } ) )

	})
)