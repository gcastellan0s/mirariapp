!function(e,t){var o=function(e){var t={};function o(n){if(t[n])return t[n].exports;var r=t[n]={i:n,l:!1,exports:{}};return e[n].call(r.exports,r,r.exports,o),r.l=!0,r.exports}return o.m=e,o.c=t,o.d=function(e,t,n){o.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},o.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.t=function(e,t){if(1&t&&(e=o(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(o.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)o.d(n,r,function(t){return e[t]}.bind(null,r));return n},o.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return o.d(t,"a",t),t},o.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},o.p="",o(o.s=220)}({1:function(e,t){e.exports=window.jQuery},220:function(e,t,o){o(221)},221:function(e,t,o){var n,r,i;!function(s){"use strict";r=[o(1),o(3)],void 0===(i="function"==typeof(n=function(e,t){e.extend(t.prototype.options,{videoContentClass:"video-content",videoLoadingClass:"video-loading",videoPlayingClass:"video-playing",videoPosterProperty:"poster",videoSourcesProperty:"sources"});var o=t.prototype.handleSlide;return e.extend(t.prototype,{handleSlide:function(e){o.call(this,e),this.playingVideo&&this.playingVideo.pause()},videoFactory:function(t,o,n){var r,i,s,l,a,p=this,d=this.options,u=this.elementPrototype.cloneNode(!1),c=e(u),y=[{type:"error",target:u}],f=n||document.createElement("video"),v=this.getItemProperty(t,d.urlProperty),g=this.getItemProperty(t,d.typeProperty),m=this.getItemProperty(t,d.titleProperty),P=this.getItemProperty(t,this.options.altTextProperty)||m,h=this.getItemProperty(t,d.videoPosterProperty),C=this.getItemProperty(t,d.videoSourcesProperty);if(c.addClass(d.videoContentClass),m&&(u.title=m),f.canPlayType)if(v&&g&&f.canPlayType(g))f.src=v;else if(C)for(;C.length;)if(i=C.shift(),v=this.getItemProperty(i,d.urlProperty),g=this.getItemProperty(i,d.typeProperty),v&&g&&f.canPlayType(g)){f.src=v;break}return h&&(f.poster=h,r=this.imagePrototype.cloneNode(!1),e(r).addClass(d.toggleClass),r.src=h,r.draggable=!1,r.alt=P,u.appendChild(r)),(s=document.createElement("a")).setAttribute("target","_blank"),n||s.setAttribute("download",m),s.href=v,f.src&&(f.controls=!0,(n||e(f)).on("error",function(){p.setTimeout(o,y)}).on("pause",function(){f.seeking||(l=!1,c.removeClass(p.options.videoLoadingClass).removeClass(p.options.videoPlayingClass),a&&p.container.addClass(p.options.controlsClass),delete p.playingVideo,p.interval&&p.play())}).on("playing",function(){l=!1,c.removeClass(p.options.videoLoadingClass).addClass(p.options.videoPlayingClass),p.container.hasClass(p.options.controlsClass)?(a=!0,p.container.removeClass(p.options.controlsClass)):a=!1}).on("play",function(){window.clearTimeout(p.timeout),l=!0,c.addClass(p.options.videoLoadingClass),p.playingVideo=f}),e(s).on("click",function(e){p.preventDefault(e),l?f.pause():f.play()}),u.appendChild(n&&n.element||f)),u.appendChild(s),this.setTimeout(o,[{type:"load",target:u}]),u}}),t})?n.apply(t,r):n)||(e.exports=i)}()},3:function(e,t){e.exports=window.blueimpGallery}});if("object"==typeof o){var n=["object"==typeof module&&"object"==typeof module.exports?module.exports:null,"undefined"!=typeof window?window:null,e&&e!==window?e:null];for(var r in o)n[0]&&(n[0][r]=o[r]),n[1]&&"__esModule"!==r&&(n[1][r]=o[r]),n[2]&&(n[2][r]=o[r])}}(this);