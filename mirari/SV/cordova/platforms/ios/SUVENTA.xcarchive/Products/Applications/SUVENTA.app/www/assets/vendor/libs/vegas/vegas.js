
(function(r,f) {
	var a=f();
	if(typeof a!=='object')return;
	var e=[typeof module==='object'&&typeof module.exports==='object'?module.exports:null,typeof window!=='undefined'?window:null,r&&r!==window?r:null];
	for(var i in a){e[0]&&(e[0][i]=a[i]);e[1]&&i!=='__esModule'&&(e[1][i] = a[i]);e[2]&&(e[2][i]=a[i]);}
})(this,function(){
	return /******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId]) {
/******/ 			return installedModules[moduleId].exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			i: moduleId,
/******/ 			l: false,
/******/ 			exports: {}
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.l = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// define getter function for harmony exports
/******/ 	__webpack_require__.d = function(exports, name, getter) {
/******/ 		if(!__webpack_require__.o(exports, name)) {
/******/ 			Object.defineProperty(exports, name, { enumerable: true, get: getter });
/******/ 		}
/******/ 	};
/******/
/******/ 	// define __esModule on exports
/******/ 	__webpack_require__.r = function(exports) {
/******/ 		if(typeof Symbol !== 'undefined' && Symbol.toStringTag) {
/******/ 			Object.defineProperty(exports, Symbol.toStringTag, { value: 'Module' });
/******/ 		}
/******/ 		Object.defineProperty(exports, '__esModule', { value: true });
/******/ 	};
/******/
/******/ 	// create a fake namespace object
/******/ 	// mode & 1: value is a module id, require it
/******/ 	// mode & 2: merge all properties of value into the ns
/******/ 	// mode & 4: return value when already ns object
/******/ 	// mode & 8|1: behave like require
/******/ 	__webpack_require__.t = function(value, mode) {
/******/ 		if(mode & 1) value = __webpack_require__(value);
/******/ 		if(mode & 8) return value;
/******/ 		if((mode & 4) && typeof value === 'object' && value && value.__esModule) return value;
/******/ 		var ns = Object.create(null);
/******/ 		__webpack_require__.r(ns);
/******/ 		Object.defineProperty(ns, 'default', { enumerable: true, value: value });
/******/ 		if(mode & 2 && typeof value != 'string') for(var key in value) __webpack_require__.d(ns, key, function(key) { return value[key]; }.bind(null, key));
/******/ 		return ns;
/******/ 	};
/******/
/******/ 	// getDefaultExport function for compatibility with non-harmony modules
/******/ 	__webpack_require__.n = function(module) {
/******/ 		var getter = module && module.__esModule ?
/******/ 			function getDefault() { return module['default']; } :
/******/ 			function getModuleExports() { return module; };
/******/ 		__webpack_require__.d(getter, 'a', getter);
/******/ 		return getter;
/******/ 	};
/******/
/******/ 	// Object.prototype.hasOwnProperty.call
/******/ 	__webpack_require__.o = function(object, property) { return Object.prototype.hasOwnProperty.call(object, property); };
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(__webpack_require__.s = "./libs/vegas/vegas.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./libs/vegas/_extension.es6":
/*!***********************************!*\
  !*** ./libs/vegas/_extension.es6 ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("function _typeof(obj) { if (typeof Symbol === \"function\" && typeof Symbol.iterator === \"symbol\") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === \"function\" && obj.constructor === Symbol && obj !== Symbol.prototype ? \"symbol\" : typeof obj; }; } return _typeof(obj); }\n\n// Make vegas responsive\n//\nvar fnVegas = $.fn.vegas;\n\n$.fn.vegas = function () {\n  for (var _len = arguments.length, args = new Array(_len), _key = 0; _key < _len; _key++) {\n    args[_key] = arguments[_key];\n  }\n\n  var result = fnVegas.apply(this, args);\n\n  if (args[0] === undefined || _typeof(args[0]) === 'object') {\n    this.each(function () {\n      if (this.tagName.toUpperCase() === 'BODY' || !this._vegas) {\n        return;\n      }\n\n      $(this).css('height', '');\n    });\n  }\n\n  return result;\n};\n\n//# sourceURL=webpack:///./libs/vegas/_extension.es6?");

/***/ }),

/***/ "./libs/vegas/vegas.js":
/*!*****************************!*\
  !*** ./libs/vegas/vegas.js ***!
  \*****************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! ../../node_modules/vegas/src/vegas.js */ \"./node_modules/vegas/src/vegas.js\");\n__webpack_require__(/*! ./_extension.es6 */ \"./libs/vegas/_extension.es6\");\n\n\n//# sourceURL=webpack:///./libs/vegas/vegas.js?");

/***/ }),

/***/ "./node_modules/vegas/src/vegas.js":
/*!*****************************************!*\
  !*** ./node_modules/vegas/src/vegas.js ***!
  \*****************************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("\n(function ($) {\n    'use strict';\n\n    var defaults = {\n        slide:                   0,\n        delay:                   5000,\n        loop:                    true,\n        preload:                 false,\n        preloadImage:            false,\n        preloadVideo:            false,\n        timer:                   true,\n        overlay:                 false,\n        autoplay:                true,\n        shuffle:                 false,\n        cover:                   true,\n        color:                   null,\n        align:                   'center',\n        valign:                  'center',\n        firstTransition:         null,\n        firstTransitionDuration: null,\n        transition:              'fade',\n        transitionDuration:      1000,\n        transitionRegister:      [],\n        animation:               null,\n        animationDuration:       'auto',\n        animationRegister:       [],\n        slidesToKeep:            1,\n        init:  function () {},\n        play:  function () {},\n        pause: function () {},\n        walk:  function () {},\n        slides: [\n            // {\n            //  src:                null,\n            //  color:              null,\n            //  delay:              null,\n            //  align:              null,\n            //  valign:             null,\n            //  transition:         null,\n            //  transitionDuration: null,\n            //  animation:          null,\n            //  animationDuration:  null,\n            //  cover:              true,\n            //  video: {\n            //      src: [],\n            //      mute: true,\n            //      loop: true\n            // }\n            // ...\n        ]\n    };\n\n    var videoCache = {};\n\n    var Vegas = function (elmt, options) {\n        this.elmt         = elmt;\n        this.settings     = $.extend({}, defaults, $.vegas.defaults, options);\n        this.slide        = this.settings.slide;\n        this.total        = this.settings.slides.length;\n        this.noshow       = this.total < 2;\n        this.paused       = !this.settings.autoplay || this.noshow;\n        this.ended        = false;\n        this.$elmt        = $(elmt);\n        this.$timer       = null;\n        this.$overlay     = null;\n        this.$slide       = null;\n        this.timeout      = null;\n        this.first        = true;\n\n        this.transitions = [\n            'fade', 'fade2',\n            'blur', 'blur2',\n            'flash', 'flash2',\n            'negative', 'negative2',\n            'burn', 'burn2',\n            'slideLeft', 'slideLeft2',\n            'slideRight', 'slideRight2',\n            'slideUp', 'slideUp2',\n            'slideDown', 'slideDown2',\n            'zoomIn', 'zoomIn2',\n            'zoomOut', 'zoomOut2',\n            'swirlLeft', 'swirlLeft2',\n            'swirlRight', 'swirlRight2'\n        ];\n\n        this.animations = [\n            'kenburns',\n            'kenburnsLeft', 'kenburnsRight',\n            'kenburnsUp', 'kenburnsUpLeft', 'kenburnsUpRight',\n            'kenburnsDown', 'kenburnsDownLeft', 'kenburnsDownRight'\n        ];\n\n        if (this.settings.transitionRegister instanceof Array === false) {\n            this.settings.transitionRegister = [ this.settings.transitionRegister ];\n        }\n\n        if (this.settings.animationRegister instanceof Array === false) {\n            this.settings.animationRegister = [ this.settings.animationRegister ];\n        }\n\n        this.transitions = this.transitions.concat(this.settings.transitionRegister);\n        this.animations  = this.animations.concat(this.settings.animationRegister);\n\n        this.support = {\n            objectFit:  'objectFit'  in document.body.style,\n            transition: 'transition' in document.body.style || 'WebkitTransition' in document.body.style,\n            video:      $.vegas.isVideoCompatible()\n        };\n\n        if (this.settings.shuffle === true) {\n            this.shuffle();\n        }\n\n        this._init();\n    };\n\n    Vegas.prototype = {\n        _init: function () {\n            var $wrapper,\n                $overlay,\n                $timer,\n                isBody  = this.elmt.tagName === 'BODY',\n                timer   = this.settings.timer,\n                overlay = this.settings.overlay,\n                self    = this;\n\n            // Preloading\n            this._preload();\n\n            // Wrapper with content\n            if (!isBody) {\n                this.$elmt.css('height', this.$elmt.css('height'));\n\n                $wrapper = $('<div class=\"vegas-wrapper\">')\n                    .css('overflow', this.$elmt.css('overflow'))\n                    .css('padding',  this.$elmt.css('padding'));\n\n                // Some browsers don't compute padding shorthand\n                if (!this.$elmt.css('padding')) {\n                    $wrapper\n                        .css('padding-top',    this.$elmt.css('padding-top'))\n                        .css('padding-bottom', this.$elmt.css('padding-bottom'))\n                        .css('padding-left',   this.$elmt.css('padding-left'))\n                        .css('padding-right',  this.$elmt.css('padding-right'));\n                }\n\n                this.$elmt.clone(true).children().appendTo($wrapper);\n                this.elmt.innerHTML = '';\n            }\n\n            // Timer\n            if (timer && this.support.transition) {\n                $timer = $('<div class=\"vegas-timer\"><div class=\"vegas-timer-progress\">');\n                this.$timer = $timer;\n                this.$elmt.prepend($timer);\n            }\n\n            // Overlay\n            if (overlay) {\n                $overlay = $('<div class=\"vegas-overlay\">');\n\n                if (typeof overlay === 'string') {\n                    $overlay.css('background-image', 'url(' + overlay + ')');\n                }\n\n                this.$overlay = $overlay;\n                this.$elmt.prepend($overlay);\n            }\n\n            // Container\n            this.$elmt.addClass('vegas-container');\n\n            if (!isBody) {\n                this.$elmt.append($wrapper);\n            }\n\n            setTimeout(function () {\n                self.trigger('init');\n                self._goto(self.slide);\n\n                if (self.settings.autoplay) {\n                    self.trigger('play');\n                }\n            }, 1);\n        },\n\n        _preload: function () {\n            var img, i;\n\n            for (i = 0; i < this.settings.slides.length; i++) {\n                if (this.settings.preload || this.settings.preloadImages) {\n                    if (this.settings.slides[i].src) {\n                        img = new Image();\n                        img.src = this.settings.slides[i].src;\n                    }\n                }\n\n                if (this.settings.preload || this.settings.preloadVideos) {\n                    if (this.support.video && this.settings.slides[i].video) {\n                        if (this.settings.slides[i].video instanceof Array) {\n                            this._video(this.settings.slides[i].video);\n                        } else {\n                            this._video(this.settings.slides[i].video.src);\n                        }\n                    }\n                }\n            }\n        },\n\n        _random: function (array) {\n            return array[Math.floor(Math.random() * array.length)];\n        },\n\n        _slideShow: function () {\n            var self = this;\n\n            if (this.total > 1 && !this.ended && !this.paused && !this.noshow) {\n                this.timeout = setTimeout(function () {\n                    self.next();\n                }, this._options('delay'));\n            }\n        },\n\n        _timer: function (state) {\n            var self = this;\n\n            clearTimeout(this.timeout);\n\n            if (!this.$timer) {\n                return;\n            }\n\n            this.$timer\n                .removeClass('vegas-timer-running')\n                    .find('div')\n                        .css('transition-duration', '0ms');\n\n            if (this.ended || this.paused || this.noshow) {\n                return;\n            }\n\n            if (state) {\n                setTimeout(function () {\n                    self.$timer\n                    .addClass('vegas-timer-running')\n                        .find('div')\n                            .css('transition-duration', self._options('delay') - 100 + 'ms');\n                }, 100);\n            }\n        },\n\n        _video: function (srcs) {\n            var video,\n                source,\n                cacheKey = srcs.toString();\n\n            if (videoCache[cacheKey]) {\n                return videoCache[cacheKey];\n            }\n\n            if (srcs instanceof Array === false) {\n                srcs = [ srcs ];\n            }\n\n            video = document.createElement('video');\n            video.preload = true;\n\n            srcs.forEach(function (src) {\n                source = document.createElement('source');\n                source.src = src;\n                video.appendChild(source);\n            });\n\n            videoCache[cacheKey] = video;\n\n            return video;\n        },\n\n        _fadeOutSound: function (video, duration) {\n            var self   = this,\n                delay  = duration / 10,\n                volume = video.volume - 0.09;\n\n            if (volume > 0) {\n                video.volume = volume;\n\n                setTimeout(function () {\n                    self._fadeOutSound(video, duration);\n                }, delay);\n            } else {\n                video.pause();\n            }\n        },\n\n        _fadeInSound: function (video, duration) {\n            var self   = this,\n                delay  = duration / 10,\n                volume = video.volume + 0.09;\n\n            if (volume < 1) {\n                video.volume = volume;\n\n                setTimeout(function () {\n                    self._fadeInSound(video, duration);\n                }, delay);\n            }\n        },\n\n        _options: function (key, i) {\n            if (i === undefined) {\n                i = this.slide;\n            }\n\n            if (this.settings.slides[i][key] !== undefined) {\n                return this.settings.slides[i][key];\n            }\n\n            return this.settings[key];\n        },\n\n        _goto: function (nb) {\n            if (typeof this.settings.slides[nb] === 'undefined') {\n                nb = 0;\n            }\n\n            this.slide = nb;\n\n            var $slide,\n                $inner,\n                $video,\n                $slides       = this.$elmt.children('.vegas-slide'),\n                src           = this.settings.slides[nb].src,\n                videoSettings = this.settings.slides[nb].video,\n                delay         = this._options('delay'),\n                align         = this._options('align'),\n                valign        = this._options('valign'),\n                cover         = this._options('cover'),\n                color         = this._options('color') || this.$elmt.css('background-color'),\n                self          = this,\n                total         = $slides.length,\n                video,\n                img;\n\n            var transition         = this._options('transition'),\n                transitionDuration = this._options('transitionDuration'),\n                animation          = this._options('animation'),\n                animationDuration  = this._options('animationDuration');\n\n            if (this.settings.firstTransition && this.first) {\n                transition = this.settings.firstTransition || transition;\n            }\n\n            if (this.settings.firstTransitionDuration && this.first) {\n                transitionDuration = this.settings.firstTransitionDuration || transitionDuration;\n            }\n\n            if (this.first) {\n                this.first = false;\n            }\n\n            if (cover !== 'repeat') {\n                if (cover === true) {\n                    cover = 'cover';\n                } else if (cover === false) {\n                    cover = 'contain';\n                }\n            }\n\n            if (transition === 'random' || transition instanceof Array) {\n                if (transition instanceof Array) {\n                    transition = this._random(transition);\n                } else {\n                    transition = this._random(this.transitions);\n                }\n            }\n\n            if (animation === 'random' || animation instanceof Array) {\n                if (animation instanceof Array) {\n                    animation = this._random(animation);\n                } else {\n                    animation = this._random(this.animations);\n                }\n            }\n\n            if (transitionDuration === 'auto' || transitionDuration > delay) {\n                transitionDuration = delay;\n            }\n\n            if (animationDuration === 'auto') {\n                animationDuration = delay;\n            }\n\n            $slide = $('<div class=\"vegas-slide\"></div>');\n\n            if (this.support.transition && transition) {\n                $slide.addClass('vegas-transition-' + transition);\n            }\n\n            // Video\n\n            if (this.support.video && videoSettings) {\n                if (videoSettings instanceof Array) {\n                    video = this._video(videoSettings);\n                } else {\n                    video = this._video(videoSettings.src);\n                }\n\n                video.loop  = videoSettings.loop !== undefined ? videoSettings.loop : true;\n                video.muted = videoSettings.mute !== undefined ? videoSettings.mute : true;\n\n                if (video.muted === false) {\n                    video.volume = 0;\n                    this._fadeInSound(video, transitionDuration);\n                } else {\n                    video.pause();\n                }\n\n                $video = $(video)\n                    .addClass('vegas-video')\n                    .css('background-color', color);\n\n                if (this.support.objectFit) {\n                    $video\n                        .css('object-position', align + ' ' + valign)\n                        .css('object-fit', cover)\n                        .css('width',  '100%')\n                        .css('height', '100%');\n                } else if (cover === 'contain') {\n                    $video\n                        .css('width',  '100%')\n                        .css('height', '100%');\n                }\n\n                $slide.append($video);\n\n            // Image\n\n            } else {\n                img = new Image();\n\n                $inner = $('<div class=\"vegas-slide-inner\"></div>')\n                    .css('background-image',    'url(\"' + src + '\")')\n                    .css('background-color',    color)\n                    .css('background-position', align + ' ' + valign);\n\n                if (cover === 'repeat') {\n                    $inner.css('background-repeat', 'repeat');\n                } else {\n                    $inner.css('background-size', cover);\n                }\n\n                if (this.support.transition && animation) {\n                    $inner\n                        .addClass('vegas-animation-' + animation)\n                        .css('animation-duration',  animationDuration + 'ms');\n                }\n\n                $slide.append($inner);\n            }\n\n            if (!this.support.transition) {\n                $slide.css('display', 'none');\n            }\n\n            if (total) {\n                $slides.eq(total - 1).after($slide);\n            } else {\n                this.$elmt.prepend($slide);\n            }\n\n            $slides\n                .css('transition', 'all 0ms')\n                .each(function () {\n                    this.className  = 'vegas-slide';\n\n                    if (this.tagName === 'VIDEO') {\n                        this.className += ' vegas-video';\n                    }\n\n                    if (transition) {\n                        this.className += ' vegas-transition-' + transition;\n                        this.className += ' vegas-transition-' + transition + '-in';\n                    }\n                }\n            );\n\n            self._timer(false);\n\n            function go () {\n                self._timer(true);\n\n                setTimeout(function () {\n                    if (transition) {\n                        if (self.support.transition) {\n                            $slides\n                                .css('transition', 'all ' + transitionDuration + 'ms')\n                                .addClass('vegas-transition-' + transition + '-out');\n\n                            $slides.each(function () {\n                                var video = $slides.find('video').get(0);\n\n                                if (video) {\n                                    video.volume = 1;\n                                    self._fadeOutSound(video, transitionDuration);\n                                }\n                            });\n\n                            $slide\n                                .css('transition', 'all ' + transitionDuration + 'ms')\n                                .addClass('vegas-transition-' + transition + '-in');\n                        } else {\n                            $slide.fadeIn(transitionDuration);\n                        }\n                    }\n\n                    for (var i = 0; i < $slides.length - self.settings.slidesToKeep; i++) {\n                        $slides.eq(i).remove();\n                    }\n\n                    self.trigger('walk');\n                    self._slideShow();\n                }, 100);\n            }\n            if (video) {\n                if (video.readyState === 4) {\n                    video.currentTime = 0;\n                }\n\n                video.play();\n                go();\n            } else {\n                img.src = src;\n\n                if (img.complete) {\n                    go();\n                } else {\n                    img.onload = go;\n                }\n            }\n        },\n\n        _end: function () {\n            if (this.settings.autoplay) {\n                this.ended = false;\n            } else {\n                this.ended = true;\n            }\n            this._timer(false);\n            this.trigger('end');\n        },\n\n        shuffle: function () {\n            var temp,\n                rand;\n\n            for (var i = this.total - 1; i > 0; i--) {\n                rand = Math.floor(Math.random() * (i + 1));\n                temp = this.settings.slides[i];\n\n                this.settings.slides[i] = this.settings.slides[rand];\n                this.settings.slides[rand] = temp;\n            }\n        },\n\n        play: function () {\n            if (this.paused) {\n                this.paused = false;\n                this.next();\n                this.trigger('play');\n            }\n        },\n\n        pause: function () {\n            this._timer(false);\n            this.paused = true;\n            this.trigger('pause');\n        },\n\n        toggle: function () {\n            if (this.paused) {\n                this.play();\n            } else {\n                this.pause();\n            }\n        },\n\n        playing: function () {\n            return !this.paused && !this.noshow;\n        },\n\n        current: function (advanced) {\n            if (advanced) {\n                return {\n                    slide: this.slide,\n                    data:  this.settings.slides[this.slide]\n                };\n            }\n            return this.slide;\n        },\n\n        jump: function (nb) {\n            if (nb < 0 || nb > this.total - 1 || nb === this.slide) {\n                return;\n            }\n\n            this.slide = nb;\n            this._goto(this.slide);\n        },\n\n        next: function () {\n            this.slide++;\n\n            if (this.slide >= this.total) {\n                if (!this.settings.loop) {\n                    return this._end();\n                }\n\n                this.slide = 0;\n            }\n\n            this._goto(this.slide);\n        },\n\n        previous: function () {\n            this.slide--;\n\n            if (this.slide < 0) {\n                if (!this.settings.loop) {\n                    this.slide++;\n                    return;\n                } else {\n                    this.slide = this.total - 1;\n                }\n            }\n\n            this._goto(this.slide);\n        },\n\n        trigger: function (fn) {\n            var params = [];\n\n            if (fn === 'init') {\n                params = [ this.settings ];\n            } else {\n                params = [\n                    this.slide,\n                    this.settings.slides[this.slide]\n                ];\n            }\n\n            this.$elmt.trigger('vegas' + fn, params);\n\n            if (typeof this.settings[fn] === 'function') {\n                this.settings[fn].apply(this.$elmt, params);\n            }\n        },\n\n        options: function (key, value) {\n            var oldSlides = this.settings.slides.slice();\n\n            if (typeof key === 'object') {\n                this.settings = $.extend({}, defaults, $.vegas.defaults, key);\n            } else if (typeof key === 'string') {\n                if (value === undefined) {\n                    return this.settings[key];\n                }\n                this.settings[key] = value;\n            } else {\n                return this.settings;\n            }\n\n            // In case slides have changed\n            if (this.settings.slides !== oldSlides) {\n                this.total  = this.settings.slides.length;\n                this.noshow = this.total < 2;\n                this._preload();\n            }\n        },\n\n        destroy: function () {\n            clearTimeout(this.timeout);\n\n            this.$elmt.removeClass('vegas-container');\n            this.$elmt.find('> .vegas-slide').remove();\n            this.$elmt.find('> .vegas-wrapper').clone(true).children().appendTo(this.$elmt);\n            this.$elmt.find('> .vegas-wrapper').remove();\n\n            if (this.settings.timer) {\n                this.$timer.remove();\n            }\n\n            if (this.settings.overlay) {\n                this.$overlay.remove();\n            }\n\n            this.elmt._vegas = null;\n        }\n    };\n\n    $.fn.vegas = function(options) {\n        var args = arguments,\n            error = false,\n            returns;\n\n        if (options === undefined || typeof options === 'object') {\n            return this.each(function () {\n                if (!this._vegas) {\n                    this._vegas = new Vegas(this, options);\n                }\n            });\n        } else if (typeof options === 'string') {\n            this.each(function () {\n                var instance = this._vegas;\n\n                if (!instance) {\n                    throw new Error('No Vegas applied to this element.');\n                }\n\n                if (typeof instance[options] === 'function' && options[0] !== '_') {\n                    returns = instance[options].apply(instance, [].slice.call(args, 1));\n                } else {\n                    error = true;\n                }\n            });\n\n            if (error) {\n                throw new Error('No method \"' + options + '\" in Vegas.');\n            }\n\n            return returns !== undefined ? returns : this;\n        }\n    };\n\n    $.vegas = {};\n    $.vegas.defaults = defaults;\n\n    $.vegas.isVideoCompatible = function () {\n        return !/(Android|webOS|Phone|iPad|iPod|BlackBerry|Windows Phone)/i.test(navigator.userAgent);\n    };\n\n})(window.jQuery || window.Zepto);\n\n\n//# sourceURL=webpack:///./node_modules/vegas/src/vegas.js?");

/***/ })

/******/ });
});;