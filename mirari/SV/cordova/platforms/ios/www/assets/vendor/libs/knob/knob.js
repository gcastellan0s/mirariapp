
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
/******/ 	return __webpack_require__(__webpack_require__.s = "./libs/knob/knob.js");
/******/ })
/************************************************************************/
/******/ ({

/***/ "./libs/knob/knob.js":
/*!***************************!*\
  !*** ./libs/knob/knob.js ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("__webpack_require__(/*! ../../node_modules/jquery-knob/js/jquery.knob.js */ \"./node_modules/jquery-knob/js/jquery.knob.js\");\n\n\n//# sourceURL=webpack:///./libs/knob/knob.js?");

/***/ }),

/***/ "./node_modules/jquery-knob/js/jquery.knob.js":
/*!****************************************************!*\
  !*** ./node_modules/jquery-knob/js/jquery.knob.js ***!
  \****************************************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

eval("/*!jQuery Knob*/\n/**\n * Downward compatible, touchable dial\n *\n * Version: 1.2.11\n * Requires: jQuery v1.7+\n *\n * Copyright (c) 2012 Anthony Terrien\n * Under MIT License (http://www.opensource.org/licenses/mit-license.php)\n *\n * Thanks to vor, eskimoblood, spiffistan, FabrizioC\n */\n(function (factory) {\n    if (true) {\n        // CommonJS\n        module.exports = factory(__webpack_require__(/*! jquery */ \"jquery\"));\n    } else {}\n}(function ($) {\n\n    /**\n     * Kontrol library\n     */\n    \"use strict\";\n\n    /**\n     * Definition of globals and core\n     */\n    var k = {}, // kontrol\n        max = Math.max,\n        min = Math.min;\n\n    k.c = {};\n    k.c.d = $(document);\n    k.c.t = function (e) {\n        return e.originalEvent.touches.length - 1;\n    };\n\n    /**\n     * Kontrol Object\n     *\n     * Definition of an abstract UI control\n     *\n     * Each concrete component must call this one.\n     * <code>\n     * k.o.call(this);\n     * </code>\n     */\n    k.o = function () {\n        var s = this;\n\n        this.o = null; // array of options\n        this.$ = null; // jQuery wrapped element\n        this.i = null; // mixed HTMLInputElement or array of HTMLInputElement\n        this.g = null; // deprecated 2D graphics context for 'pre-rendering'\n        this.v = null; // value ; mixed array or integer\n        this.cv = null; // change value ; not commited value\n        this.x = 0; // canvas x position\n        this.y = 0; // canvas y position\n        this.w = 0; // canvas width\n        this.h = 0; // canvas height\n        this.$c = null; // jQuery canvas element\n        this.c = null; // rendered canvas context\n        this.t = 0; // touches index\n        this.isInit = false;\n        this.fgColor = null; // main color\n        this.pColor = null; // previous color\n        this.dH = null; // draw hook\n        this.cH = null; // change hook\n        this.eH = null; // cancel hook\n        this.rH = null; // release hook\n        this.scale = 1; // scale factor\n        this.relative = false;\n        this.relativeWidth = false;\n        this.relativeHeight = false;\n        this.$div = null; // component div\n\n        this.run = function () {\n            var cf = function (e, conf) {\n                var k;\n                for (k in conf) {\n                    s.o[k] = conf[k];\n                }\n                s._carve().init();\n                s._configure()\n                 ._draw();\n            };\n\n            if (this.$.data('kontroled')) return;\n            this.$.data('kontroled', true);\n\n            this.extend();\n            this.o = $.extend({\n                    // Config\n                    min: this.$.data('min') !== undefined ? this.$.data('min') : 0,\n                    max: this.$.data('max') !== undefined ? this.$.data('max') : 100,\n                    stopper: true,\n                    readOnly: this.$.data('readonly') || (this.$.attr('readonly') === 'readonly'),\n\n                    // UI\n                    cursor: this.$.data('cursor') === true && 30\n                            || this.$.data('cursor') || 0,\n                    thickness: this.$.data('thickness')\n                               && Math.max(Math.min(this.$.data('thickness'), 1), 0.01)\n                               || 0.35,\n                    lineCap: this.$.data('linecap') || 'butt',\n                    width: this.$.data('width') || 200,\n                    height: this.$.data('height') || 200,\n                    displayInput: this.$.data('displayinput') == null || this.$.data('displayinput'),\n                    displayPrevious: this.$.data('displayprevious'),\n                    fgColor: this.$.data('fgcolor') || '#87CEEB',\n                    inputColor: this.$.data('inputcolor'),\n                    font: this.$.data('font') || 'Arial',\n                    fontWeight: this.$.data('font-weight') || 'bold',\n                    inline: false,\n                    step: this.$.data('step') || 1,\n                    rotation: this.$.data('rotation'),\n\n                    // Hooks\n                    draw: null, // function () {}\n                    change: null, // function (value) {}\n                    cancel: null, // function () {}\n                    release: null, // function (value) {}\n\n                    // Output formatting, allows to add unit: %, ms ...\n                    format: function(v) {\n                        return v;\n                    },\n                    parse: function (v) {\n                        return parseFloat(v);\n                    }\n                }, this.o\n            );\n\n            // finalize options\n            this.o.flip = this.o.rotation === 'anticlockwise' || this.o.rotation === 'acw';\n            if (!this.o.inputColor) {\n                this.o.inputColor = this.o.fgColor;\n            }\n\n            // routing value\n            if (this.$.is('fieldset')) {\n\n                // fieldset = array of integer\n                this.v = {};\n                this.i = this.$.find('input');\n                this.i.each(function(k) {\n                    var $this = $(this);\n                    s.i[k] = $this;\n                    s.v[k] = s.o.parse($this.val());\n\n                    $this.bind(\n                        'change blur',\n                        function () {\n                            var val = {};\n                            val[k] = $this.val();\n                            s.val(s._validate(val));\n                        }\n                    );\n                });\n                this.$.find('legend').remove();\n            } else {\n\n                // input = integer\n                this.i = this.$;\n                this.v = this.o.parse(this.$.val());\n                this.v === '' && (this.v = this.o.min);\n                this.$.bind(\n                    'change blur',\n                    function () {\n                        s.val(s._validate(s.o.parse(s.$.val())));\n                    }\n                );\n\n            }\n\n            !this.o.displayInput && this.$.hide();\n\n            // adds needed DOM elements (canvas, div)\n            this.$c = $(document.createElement('canvas')).attr({\n                width: this.o.width,\n                height: this.o.height\n            });\n\n            // wraps all elements in a div\n            // add to DOM before Canvas init is triggered\n            this.$div = $('<div style=\"'\n                + (this.o.inline ? 'display:inline;' : '')\n                + 'width:' + this.o.width + 'px;height:' + this.o.height + 'px;'\n                + '\"></div>');\n\n            this.$.wrap(this.$div).before(this.$c);\n            this.$div = this.$.parent();\n\n            if (typeof G_vmlCanvasManager !== 'undefined') {\n                G_vmlCanvasManager.initElement(this.$c[0]);\n            }\n\n            this.c = this.$c[0].getContext ? this.$c[0].getContext('2d') : null;\n\n            if (!this.c) {\n                throw {\n                    name:        \"CanvasNotSupportedException\",\n                    message:     \"Canvas not supported. Please use excanvas on IE8.0.\",\n                    toString:    function(){return this.name + \": \" + this.message}\n                }\n            }\n\n            // hdpi support\n            this.scale = (window.devicePixelRatio || 1) / (\n                            this.c.webkitBackingStorePixelRatio ||\n                            this.c.mozBackingStorePixelRatio ||\n                            this.c.msBackingStorePixelRatio ||\n                            this.c.oBackingStorePixelRatio ||\n                            this.c.backingStorePixelRatio || 1\n                         );\n\n            // detects relative width / height\n            this.relativeWidth =  this.o.width % 1 !== 0\n                                  && this.o.width.indexOf('%');\n            this.relativeHeight = this.o.height % 1 !== 0\n                                  && this.o.height.indexOf('%');\n            this.relative = this.relativeWidth || this.relativeHeight;\n\n            // computes size and carves the component\n            this._carve();\n\n            // prepares props for transaction\n            if (this.v instanceof Object) {\n                this.cv = {};\n                this.copy(this.v, this.cv);\n            } else {\n                this.cv = this.v;\n            }\n\n            // binds configure event\n            this.$\n                .bind(\"configure\", cf)\n                .parent()\n                .bind(\"configure\", cf);\n\n            // finalize init\n            this._listen()\n                ._configure()\n                ._xy()\n                .init();\n\n            this.isInit = true;\n\n            this.$.val(this.o.format(this.v));\n            this._draw();\n\n            return this;\n        };\n\n        this._carve = function() {\n            if (this.relative) {\n                var w = this.relativeWidth ?\n                        this.$div.parent().width() *\n                        parseInt(this.o.width) / 100\n                        : this.$div.parent().width(),\n                    h = this.relativeHeight ?\n                        this.$div.parent().height() *\n                        parseInt(this.o.height) / 100\n                        : this.$div.parent().height();\n\n                // apply relative\n                this.w = this.h = Math.min(w, h);\n            } else {\n                this.w = this.o.width;\n                this.h = this.o.height;\n            }\n\n            // finalize div\n            this.$div.css({\n                'width': this.w + 'px',\n                'height': this.h + 'px'\n            });\n\n            // finalize canvas with computed width\n            this.$c.attr({\n                width: this.w,\n                height: this.h\n            });\n\n            // scaling\n            if (this.scale !== 1) {\n                this.$c[0].width = this.$c[0].width * this.scale;\n                this.$c[0].height = this.$c[0].height * this.scale;\n                this.$c.width(this.w);\n                this.$c.height(this.h);\n            }\n\n            return this;\n        }\n\n        this._draw = function () {\n\n            // canvas pre-rendering\n            var d = true;\n\n            s.g = s.c;\n\n            s.clear();\n\n            s.dH && (d = s.dH());\n\n            d !== false && s.draw();\n        };\n\n        this._touch = function (e) {\n            var touchMove = function (e) {\n                var v = s.xy2val(\n                            e.originalEvent.touches[s.t].pageX,\n                            e.originalEvent.touches[s.t].pageY\n                        );\n\n                if (v == s.cv) return;\n\n                if (s.cH && s.cH(v) === false) return;\n\n                s.change(s._validate(v));\n                s._draw();\n            };\n\n            // get touches index\n            this.t = k.c.t(e);\n\n            // First touch\n            touchMove(e);\n\n            // Touch events listeners\n            k.c.d\n                .bind(\"touchmove.k\", touchMove)\n                .bind(\n                    \"touchend.k\",\n                    function () {\n                        k.c.d.unbind('touchmove.k touchend.k');\n                        s.val(s.cv);\n                    }\n                );\n\n            return this;\n        };\n\n        this._mouse = function (e) {\n            var mouseMove = function (e) {\n                var v = s.xy2val(e.pageX, e.pageY);\n\n                if (v == s.cv) return;\n\n                if (s.cH && (s.cH(v) === false)) return;\n\n                s.change(s._validate(v));\n                s._draw();\n            };\n\n            // First click\n            mouseMove(e);\n\n            // Mouse events listeners\n            k.c.d\n                .bind(\"mousemove.k\", mouseMove)\n                .bind(\n                    // Escape key cancel current change\n                    \"keyup.k\",\n                    function (e) {\n                        if (e.keyCode === 27) {\n                            k.c.d.unbind(\"mouseup.k mousemove.k keyup.k\");\n\n                            if (s.eH && s.eH() === false)\n                                return;\n\n                            s.cancel();\n                        }\n                    }\n                )\n                .bind(\n                    \"mouseup.k\",\n                    function (e) {\n                        k.c.d.unbind('mousemove.k mouseup.k keyup.k');\n                        s.val(s.cv);\n                    }\n                );\n\n            return this;\n        };\n\n        this._xy = function () {\n            var o = this.$c.offset();\n            this.x = o.left;\n            this.y = o.top;\n\n            return this;\n        };\n\n        this._listen = function () {\n            if (!this.o.readOnly) {\n                this.$c\n                    .bind(\n                        \"mousedown\",\n                        function (e) {\n                            e.preventDefault();\n                            s._xy()._mouse(e);\n                        }\n                    )\n                    .bind(\n                        \"touchstart\",\n                        function (e) {\n                            e.preventDefault();\n                            s._xy()._touch(e);\n                        }\n                    );\n\n                this.listen();\n            } else {\n                this.$.attr('readonly', 'readonly');\n            }\n\n            if (this.relative) {\n                $(window).resize(function() {\n                    s._carve().init();\n                    s._draw();\n                });\n            }\n\n            return this;\n        };\n\n        this._configure = function () {\n\n            // Hooks\n            if (this.o.draw) this.dH = this.o.draw;\n            if (this.o.change) this.cH = this.o.change;\n            if (this.o.cancel) this.eH = this.o.cancel;\n            if (this.o.release) this.rH = this.o.release;\n\n            if (this.o.displayPrevious) {\n                this.pColor = this.h2rgba(this.o.fgColor, \"0.4\");\n                this.fgColor = this.h2rgba(this.o.fgColor, \"0.6\");\n            } else {\n                this.fgColor = this.o.fgColor;\n            }\n\n            return this;\n        };\n\n        this._clear = function () {\n            this.$c[0].width = this.$c[0].width;\n        };\n\n        this._validate = function (v) {\n            var val = (~~ (((v < 0) ? -0.5 : 0.5) + (v/this.o.step))) * this.o.step;\n            return Math.round(val * 100) / 100;\n        };\n\n        // Abstract methods\n        this.listen = function () {}; // on start, one time\n        this.extend = function () {}; // each time configure triggered\n        this.init = function () {}; // each time configure triggered\n        this.change = function (v) {}; // on change\n        this.val = function (v) {}; // on release\n        this.xy2val = function (x, y) {}; //\n        this.draw = function () {}; // on change / on release\n        this.clear = function () { this._clear(); };\n\n        // Utils\n        this.h2rgba = function (h, a) {\n            var rgb;\n            h = h.substring(1,7)\n            rgb = [\n                parseInt(h.substring(0,2), 16),\n                parseInt(h.substring(2,4), 16),\n                parseInt(h.substring(4,6), 16)\n            ];\n\n            return \"rgba(\" + rgb[0] + \",\" + rgb[1] + \",\" + rgb[2] + \",\" + a + \")\";\n        };\n\n        this.copy = function (f, t) {\n            for (var i in f) {\n                t[i] = f[i];\n            }\n        };\n    };\n\n\n    /**\n     * k.Dial\n     */\n    k.Dial = function () {\n        k.o.call(this);\n\n        this.startAngle = null;\n        this.xy = null;\n        this.radius = null;\n        this.lineWidth = null;\n        this.cursorExt = null;\n        this.w2 = null;\n        this.PI2 = 2*Math.PI;\n\n        this.extend = function () {\n            this.o = $.extend({\n                bgColor: this.$.data('bgcolor') || '#EEEEEE',\n                angleOffset: this.$.data('angleoffset') || 0,\n                angleArc: this.$.data('anglearc') || 360,\n                inline: true\n            }, this.o);\n        };\n\n        this.val = function (v, triggerRelease) {\n            if (null != v) {\n\n                // reverse format\n                v = this.o.parse(v);\n\n                if (triggerRelease !== false\n                    && v != this.v\n                    && this.rH\n                    && this.rH(v) === false) { return; }\n\n                this.cv = this.o.stopper ? max(min(v, this.o.max), this.o.min) : v;\n                this.v = this.cv;\n                this.$.val(this.o.format(this.v));\n                this._draw();\n            } else {\n                return this.v;\n            }\n        };\n\n        this.xy2val = function (x, y) {\n            var a, ret;\n\n            a = Math.atan2(\n                        x - (this.x + this.w2),\n                        - (y - this.y - this.w2)\n                    ) - this.angleOffset;\n\n            if (this.o.flip) {\n                a = this.angleArc - a - this.PI2;\n            }\n\n            if (this.angleArc != this.PI2 && (a < 0) && (a > -0.5)) {\n\n                // if isset angleArc option, set to min if .5 under min\n                a = 0;\n            } else if (a < 0) {\n                a += this.PI2;\n            }\n\n            ret = (a * (this.o.max - this.o.min) / this.angleArc) + this.o.min;\n\n            this.o.stopper && (ret = max(min(ret, this.o.max), this.o.min));\n\n            return ret;\n        };\n\n        this.listen = function () {\n\n            // bind MouseWheel\n            var s = this, mwTimerStop,\n                mwTimerRelease,\n                mw = function (e) {\n                    e.preventDefault();\n\n                    var ori = e.originalEvent,\n                        deltaX = ori.detail || ori.wheelDeltaX,\n                        deltaY = ori.detail || ori.wheelDeltaY,\n                        v = s._validate(s.o.parse(s.$.val()))\n                            + (\n                                deltaX > 0 || deltaY > 0\n                                ? s.o.step\n                                : deltaX < 0 || deltaY < 0 ? -s.o.step : 0\n                              );\n\n                    v = max(min(v, s.o.max), s.o.min);\n\n                    s.val(v, false);\n\n                    if (s.rH) {\n                        // Handle mousewheel stop\n                        clearTimeout(mwTimerStop);\n                        mwTimerStop = setTimeout(function () {\n                            s.rH(v);\n                            mwTimerStop = null;\n                        }, 100);\n\n                        // Handle mousewheel releases\n                        if (!mwTimerRelease) {\n                            mwTimerRelease = setTimeout(function () {\n                                if (mwTimerStop)\n                                    s.rH(v);\n                                mwTimerRelease = null;\n                            }, 200);\n                        }\n                    }\n                },\n                kval,\n                to,\n                m = 1,\n                kv = {\n                    37: -s.o.step,\n                    38: s.o.step,\n                    39: s.o.step,\n                    40: -s.o.step\n                };\n\n            this.$\n                .bind(\n                    \"keydown\",\n                    function (e) {\n                        var kc = e.keyCode;\n\n                        // numpad support\n                        if (kc >= 96 && kc <= 105) {\n                            kc = e.keyCode = kc - 48;\n                        }\n\n                        kval = parseInt(String.fromCharCode(kc));\n\n                        if (isNaN(kval)) {\n                            (kc !== 13)                     // enter\n                            && kc !== 8                     // bs\n                            && kc !== 9                     // tab\n                            && kc !== 189                   // -\n                            && (kc !== 190\n                                || s.$.val().match(/\\./))   // . allowed once\n                            && e.preventDefault();\n\n                            // arrows\n                            if ($.inArray(kc,[37,38,39,40]) > -1) {\n                                e.preventDefault();\n\n                                var v = s.o.parse(s.$.val()) + kv[kc] * m;\n                                s.o.stopper && (v = max(min(v, s.o.max), s.o.min));\n\n                                s.change(s._validate(v));\n                                s._draw();\n\n                                // long time keydown speed-up\n                                to = window.setTimeout(function () {\n                                    m *= 2;\n                                }, 30);\n                            }\n                        }\n                    }\n                )\n                .bind(\n                    \"keyup\",\n                    function (e) {\n                        if (isNaN(kval)) {\n                            if (to) {\n                                window.clearTimeout(to);\n                                to = null;\n                                m = 1;\n                                s.val(s.$.val());\n                            }\n                        } else {\n                            // kval postcond\n                            (s.$.val() > s.o.max && s.$.val(s.o.max))\n                            || (s.$.val() < s.o.min && s.$.val(s.o.min));\n                        }\n                    }\n                );\n\n            this.$c.bind(\"mousewheel DOMMouseScroll\", mw);\n            this.$.bind(\"mousewheel DOMMouseScroll\", mw)\n        };\n\n        this.init = function () {\n            if (this.v < this.o.min\n                || this.v > this.o.max) { this.v = this.o.min; }\n\n            this.$.val(this.v);\n            this.w2 = this.w / 2;\n            this.cursorExt = this.o.cursor / 100;\n            this.xy = this.w2 * this.scale;\n            this.lineWidth = this.xy * this.o.thickness;\n            this.lineCap = this.o.lineCap;\n            this.radius = this.xy - this.lineWidth / 2;\n\n            this.o.angleOffset\n            && (this.o.angleOffset = isNaN(this.o.angleOffset) ? 0 : this.o.angleOffset);\n\n            this.o.angleArc\n            && (this.o.angleArc = isNaN(this.o.angleArc) ? this.PI2 : this.o.angleArc);\n\n            // deg to rad\n            this.angleOffset = this.o.angleOffset * Math.PI / 180;\n            this.angleArc = this.o.angleArc * Math.PI / 180;\n\n            // compute start and end angles\n            this.startAngle = 1.5 * Math.PI + this.angleOffset;\n            this.endAngle = 1.5 * Math.PI + this.angleOffset + this.angleArc;\n\n            var s = max(\n                String(Math.abs(this.o.max)).length,\n                String(Math.abs(this.o.min)).length,\n                2\n            ) + 2;\n\n            this.o.displayInput\n                && this.i.css({\n                        'width' : ((this.w / 2 + 4) >> 0) + 'px',\n                        'height' : ((this.w / 3) >> 0) + 'px',\n                        'position' : 'absolute',\n                        'vertical-align' : 'middle',\n                        'margin-top' : ((this.w / 3) >> 0) + 'px',\n                        'margin-left' : '-' + ((this.w * 3 / 4 + 2) >> 0) + 'px',\n                        'border' : 0,\n                        'background' : 'none',\n                        'font' : this.o.fontWeight + ' ' + ((this.w / s) >> 0) + 'px ' + this.o.font,\n                        'text-align' : 'center',\n                        'color' : this.o.inputColor || this.o.fgColor,\n                        'padding' : '0px',\n                        '-webkit-appearance': 'none'\n                        }) || this.i.css({\n                            'width': '0px',\n                            'visibility': 'hidden'\n                        });\n        };\n\n        this.change = function (v) {\n            this.cv = v;\n            this.$.val(this.o.format(v));\n        };\n\n        this.angle = function (v) {\n            return (v - this.o.min) * this.angleArc / (this.o.max - this.o.min);\n        };\n\n        this.arc = function (v) {\n          var sa, ea;\n          v = this.angle(v);\n          if (this.o.flip) {\n              sa = this.endAngle + 0.00001;\n              ea = sa - v - 0.00001;\n          } else {\n              sa = this.startAngle - 0.00001;\n              ea = sa + v + 0.00001;\n          }\n          this.o.cursor\n              && (sa = ea - this.cursorExt)\n              && (ea = ea + this.cursorExt);\n\n          return {\n              s: sa,\n              e: ea,\n              d: this.o.flip && !this.o.cursor\n          };\n        };\n\n        this.draw = function () {\n            var c = this.g,                 // context\n                a = this.arc(this.cv),      // Arc\n                pa,                         // Previous arc\n                r = 1;\n\n            c.lineWidth = this.lineWidth;\n            c.lineCap = this.lineCap;\n\n            if (this.o.bgColor !== \"none\") {\n                c.beginPath();\n                    c.strokeStyle = this.o.bgColor;\n                    c.arc(this.xy, this.xy, this.radius, this.endAngle - 0.00001, this.startAngle + 0.00001, true);\n                c.stroke();\n            }\n\n            if (this.o.displayPrevious) {\n                pa = this.arc(this.v);\n                c.beginPath();\n                c.strokeStyle = this.pColor;\n                c.arc(this.xy, this.xy, this.radius, pa.s, pa.e, pa.d);\n                c.stroke();\n                r = this.cv == this.v;\n            }\n\n            c.beginPath();\n            c.strokeStyle = r ? this.o.fgColor : this.fgColor ;\n            c.arc(this.xy, this.xy, this.radius, a.s, a.e, a.d);\n            c.stroke();\n        };\n\n        this.cancel = function () {\n            this.val(this.v);\n        };\n    };\n\n    $.fn.dial = $.fn.knob = function (o) {\n        return this.each(\n            function () {\n                var d = new k.Dial();\n                d.o = o;\n                d.$ = $(this);\n                d.run();\n            }\n        ).parent();\n    };\n\n}));\n\n\n//# sourceURL=webpack:///./node_modules/jquery-knob/js/jquery.knob.js?");

/***/ }),

/***/ "jquery":
/*!********************************!*\
  !*** external "window.jQuery" ***!
  \********************************/
/*! no static exports found */
/***/ (function(module, exports) {

eval("module.exports = window.jQuery;\n\n//# sourceURL=webpack:///external_%22window.jQuery%22?");

/***/ })

/******/ });
});;