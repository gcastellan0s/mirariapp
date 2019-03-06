!function(t,i){var e=function(t){var i={};function e(o){if(i[o])return i[o].exports;var n=i[o]={i:o,l:!1,exports:{}};return t[o].call(n.exports,n,n.exports,e),n.l=!0,n.exports}return e.m=t,e.c=i,e.d=function(t,i,o){e.o(t,i)||Object.defineProperty(t,i,{enumerable:!0,get:o})},e.r=function(t){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},e.t=function(t,i){if(1&i&&(t=e(t)),8&i)return t;if(4&i&&"object"==typeof t&&t&&t.__esModule)return t;var o=Object.create(null);if(e.r(o),Object.defineProperty(o,"default",{enumerable:!0,value:t}),2&i&&"string"!=typeof t)for(var n in t)e.d(o,n,function(i){return t[i]}.bind(null,n));return o},e.n=function(t){var i=t&&t.__esModule?function(){return t.default}:function(){return t};return e.d(i,"a",i),i},e.o=function(t,i){return Object.prototype.hasOwnProperty.call(t,i)},e.p="",e(e.s=414)}({414:function(t,i,e){e(415)},415:function(t,i){
/* @license
morris.js v0.5.0
Copyright 2014 Olly Smith All rights reserved.
Licensed under the BSD-2-Clause License.
*/
(function(){var t,i,e,o,n=[].slice,s=function(t,i){return function(){return t.apply(i,arguments)}},r={}.hasOwnProperty,h=function(t,i){for(var e in i)r.call(i,e)&&(t[e]=i[e]);function o(){this.constructor=t}return o.prototype=i.prototype,t.prototype=new o,t.__super__=i.prototype,t},a=[].indexOf||function(t){for(var i=0,e=this.length;i<e;i++)if(i in this&&this[i]===t)return i;return-1};i=window.Morris={},t=jQuery,i.EventEmitter=function(){function t(){}return t.prototype.on=function(t,i){return null==this.handlers&&(this.handlers={}),null==this.handlers[t]&&(this.handlers[t]=[]),this.handlers[t].push(i),this},t.prototype.fire=function(){var t,i,e,o,s,r,h;if(e=arguments[0],t=2<=arguments.length?n.call(arguments,1):[],null!=this.handlers&&null!=this.handlers[e]){for(r=this.handlers[e],h=[],o=0,s=r.length;o<s;o++)i=r[o],h.push(i.apply(null,t));return h}},t}(),i.commas=function(t){var i,e,o,n;return null!=t?(o=t<0?"-":"",i=Math.abs(t),e=Math.floor(i).toFixed(0),o+=e.replace(/(?=(?:\d{3})+$)(?!^)/g,","),(n=i.toString()).length>e.length&&(o+=n.slice(e.length)),o):"-"},i.pad2=function(t){return(t<10?"0":"")+t},i.Grid=function(e){function o(i){this.resizeHandler=s(this.resizeHandler,this);var e=this;if("string"==typeof i.element?this.el=t(document.getElementById(i.element)):this.el=t(i.element),null==this.el||0===this.el.length)throw new Error("Graph container element not found");"static"===this.el.css("position")&&this.el.css("position","relative"),this.options=t.extend({},this.gridDefaults,this.defaults||{},i),"string"==typeof this.options.units&&(this.options.postUnits=i.units),this.raphael=new Raphael(this.el[0]),this.elementWidth=null,this.elementHeight=null,this.dirty=!1,this.selectFrom=null,this.init&&this.init(),this.setData(this.options.data),this.el.bind("mousemove",function(t){var i,o,n,s,r;return o=e.el.offset(),r=t.pageX-o.left,e.selectFrom?(i=e.data[e.hitTest(Math.min(r,e.selectFrom))]._x,n=e.data[e.hitTest(Math.max(r,e.selectFrom))]._x,s=n-i,e.selectionRect.attr({x:i,width:s})):e.fire("hovermove",r,t.pageY-o.top)}),this.el.bind("mouseleave",function(t){return e.selectFrom&&(e.selectionRect.hide(),e.selectFrom=null),e.fire("hoverout")}),this.el.bind("touchstart touchmove touchend",function(t){var i,o;return o=t.originalEvent.touches[0]||t.originalEvent.changedTouches[0],i=e.el.offset(),e.fire("hovermove",o.pageX-i.left,o.pageY-i.top)}),this.el.bind("click",function(t){var i;return i=e.el.offset(),e.fire("gridclick",t.pageX-i.left,t.pageY-i.top)}),this.options.rangeSelect&&(this.selectionRect=this.raphael.rect(0,0,0,this.el.innerHeight()).attr({fill:this.options.rangeSelectColor,stroke:!1}).toBack().hide(),this.el.bind("mousedown",function(t){var i;return i=e.el.offset(),e.startRange(t.pageX-i.left)}),this.el.bind("mouseup",function(t){var i;return i=e.el.offset(),e.endRange(t.pageX-i.left),e.fire("hovermove",t.pageX-i.left,t.pageY-i.top)})),this.options.resize&&t(window).bind("resize",function(t){return null!=e.timeoutId&&window.clearTimeout(e.timeoutId),e.timeoutId=window.setTimeout(e.resizeHandler,100)}),this.el.css("-webkit-tap-highlight-color","rgba(0,0,0,0)"),this.postInit&&this.postInit()}return h(o,e),o.prototype.gridDefaults={dateFormat:null,axes:!0,grid:!0,gridLineColor:"#aaa",gridStrokeWidth:.5,gridTextColor:"#888",gridTextSize:12,gridTextFamily:"sans-serif",gridTextWeight:"normal",hideHover:!1,yLabelFormat:null,xLabelAngle:0,numLines:5,padding:25,parseTime:!0,postUnits:"",preUnits:"",ymax:"auto",ymin:"auto 0",goals:[],goalStrokeWidth:1,goalLineColors:["#666633","#999966","#cc6666","#663333"],events:[],eventStrokeWidth:1,eventLineColors:["#005a04","#ccffbb","#3a5f0b","#005502"],rangeSelect:null,rangeSelectColor:"#eef",resize:!1},o.prototype.setData=function(t,e){var o,n,s,r,h,a,l,p,u,c,d,f,g,m,y;return null==e&&(e=!0),this.options.data=t,null==t||0===t.length?(this.data=[],this.raphael.clear(),void(null!=this.hover&&this.hover.hide())):(f=this.cumulative?0:null,g=this.cumulative?0:null,this.options.goals.length>0&&(h=Math.min.apply(Math,this.options.goals),r=Math.max.apply(Math,this.options.goals),g=null!=g?Math.min(g,h):h,f=null!=f?Math.max(f,r):r),this.data=function(){var e,o,r;for(r=[],s=e=0,o=t.length;e<o;s=++e)l=t[s],(a={src:l}).label=l[this.options.xkey],this.options.parseTime?(a.x=i.parseDate(a.label),this.options.dateFormat?a.label=this.options.dateFormat(a.x):"number"==typeof a.label&&(a.label=new Date(a.label).toString())):(a.x=s,this.options.xLabelFormat&&(a.label=this.options.xLabelFormat(a))),u=0,a.y=function(){var t,i,e,o;for(e=this.options.ykeys,o=[],n=t=0,i=e.length;t<i;n=++t)d=e[n],"string"==typeof(m=l[d])&&(m=parseFloat(m)),null!=m&&"number"!=typeof m&&(m=null),null!=m&&(this.cumulative?u+=m:null!=f?(f=Math.max(m,f),g=Math.min(m,g)):f=g=m),this.cumulative&&null!=u&&(f=Math.max(u,f),g=Math.min(u,g)),o.push(m);return o}.call(this),r.push(a);return r}.call(this),this.options.parseTime&&(this.data=this.data.sort(function(t,i){return(t.x>i.x)-(i.x>t.x)})),this.xmin=this.data[0].x,this.xmax=this.data[this.data.length-1].x,this.events=[],this.options.events.length>0&&(this.options.parseTime?this.events=function(){var t,e,n,s;for(n=this.options.events,s=[],t=0,e=n.length;t<e;t++)o=n[t],s.push(i.parseDate(o));return s}.call(this):this.events=this.options.events,this.xmax=Math.max(this.xmax,Math.max.apply(Math,this.events)),this.xmin=Math.min(this.xmin,Math.min.apply(Math,this.events))),this.xmin===this.xmax&&(this.xmin-=1,this.xmax+=1),this.ymin=this.yboundary("min",g),this.ymax=this.yboundary("max",f),this.ymin===this.ymax&&(g&&(this.ymin-=1),this.ymax+=1),!0!==(y=this.options.axes)&&"both"!==y&&"y"!==y&&!0!==this.options.grid||(this.options.ymax===this.gridDefaults.ymax&&this.options.ymin===this.gridDefaults.ymin?(this.grid=this.autoGridLines(this.ymin,this.ymax,this.options.numLines),this.ymin=Math.min(this.ymin,this.grid[0]),this.ymax=Math.max(this.ymax,this.grid[this.grid.length-1])):(p=(this.ymax-this.ymin)/(this.options.numLines-1),this.grid=function(){var t,i,e;for(e=[],c=t=this.ymin,i=this.ymax;p>0?t<=i:t>=i;c=t+=p)e.push(c);return e}.call(this))),this.dirty=!0,e?this.redraw():void 0)},o.prototype.yboundary=function(t,i){var e,o;return"string"==typeof(e=this.options["y"+t])?"auto"===e.slice(0,4)?e.length>5?(o=parseInt(e.slice(5),10),null==i?o:Math[t](i,o)):null!=i?i:0:parseInt(e,10):e},o.prototype.autoGridLines=function(t,i,e){var o,n,s,r,h,a,l,p,u;return h=i-t,u=Math.floor(Math.log(h)/Math.log(10)),l=Math.pow(10,u),n=Math.floor(t/l)*l,o=Math.ceil(i/l)*l,a=(o-n)/(e-1),1===l&&a>1&&Math.ceil(a)!==a&&(a=Math.ceil(a),o=n+a*(e-1)),n<0&&o>0&&(n=Math.floor(t/a)*a,o=Math.ceil(i/a)*a),a<1?(r=Math.floor(Math.log(a)/Math.log(10)),s=function(){var t,i;for(i=[],p=t=n;a>0?t<=o:t>=o;p=t+=a)i.push(parseFloat(p.toFixed(1-r)));return i}()):s=function(){var t,i;for(i=[],p=t=n;a>0?t<=o:t>=o;p=t+=a)i.push(p);return i}(),s},o.prototype._calc=function(){var t,i,e,o,n,s,r,h;if(n=this.el.width(),e=this.el.height(),(this.elementWidth!==n||this.elementHeight!==e||this.dirty)&&(this.elementWidth=n,this.elementHeight=e,this.dirty=!1,this.left=this.options.padding,this.right=this.elementWidth-this.options.padding,this.top=this.options.padding,this.bottom=this.elementHeight-this.options.padding,!0!==(r=this.options.axes)&&"both"!==r&&"y"!==r||(s=function(){var t,e,o,n;for(o=this.grid,n=[],t=0,e=o.length;t<e;t++)i=o[t],n.push(this.measureText(this.yAxisFormat(i)).width);return n}.call(this),this.left+=Math.max.apply(Math,s)),!0!==(h=this.options.axes)&&"both"!==h&&"x"!==h||(t=function(){var t,i,e;for(e=[],o=t=0,i=this.data.length;0<=i?t<i:t>i;o=0<=i?++t:--t)e.push(this.measureText(this.data[o].text,-this.options.xLabelAngle).height);return e}.call(this),this.bottom-=Math.max.apply(Math,t)),this.width=Math.max(1,this.right-this.left),this.height=Math.max(1,this.bottom-this.top),this.dx=this.width/(this.xmax-this.xmin),this.dy=this.height/(this.ymax-this.ymin),this.calc))return this.calc()},o.prototype.transY=function(t){return this.bottom-(t-this.ymin)*this.dy},o.prototype.transX=function(t){return 1===this.data.length?(this.left+this.right)/2:this.left+(t-this.xmin)*this.dx},o.prototype.redraw=function(){if(this.raphael.clear(),this._calc(),this.drawGrid(),this.drawGoals(),this.drawEvents(),this.draw)return this.draw()},o.prototype.measureText=function(t,i){var e,o;return null==i&&(i=0),o=this.raphael.text(100,100,t).attr("font-size",this.options.gridTextSize).attr("font-family",this.options.gridTextFamily).attr("font-weight",this.options.gridTextWeight).rotate(i),e=o.getBBox(),o.remove(),e},o.prototype.yAxisFormat=function(t){return this.yLabelFormat(t)},o.prototype.yLabelFormat=function(t){return"function"==typeof this.options.yLabelFormat?this.options.yLabelFormat(t):""+this.options.preUnits+i.commas(t)+this.options.postUnits},o.prototype.drawGrid=function(){var t,i,e,o,n,s,r,h;if(!1!==this.options.grid||!0===(n=this.options.axes)||"both"===n||"y"===n){for(s=this.grid,h=[],e=0,o=s.length;e<o;e++)t=s[e],i=this.transY(t),!0!==(r=this.options.axes)&&"both"!==r&&"y"!==r||this.drawYAxisLabel(this.left-this.options.padding/2,i,this.yAxisFormat(t)),this.options.grid?h.push(this.drawGridLine("M"+this.left+","+i+"H"+(this.left+this.width))):h.push(void 0);return h}},o.prototype.drawGoals=function(){var t,i,e,o,n,s,r;for(s=this.options.goals,r=[],e=o=0,n=s.length;o<n;e=++o)i=s[e],t=this.options.goalLineColors[e%this.options.goalLineColors.length],r.push(this.drawGoal(i,t));return r},o.prototype.drawEvents=function(){var t,i,e,o,n,s,r;for(s=this.events,r=[],e=o=0,n=s.length;o<n;e=++o)i=s[e],t=this.options.eventLineColors[e%this.options.eventLineColors.length],r.push(this.drawEvent(i,t));return r},o.prototype.drawGoal=function(t,i){return this.raphael.path("M"+this.left+","+this.transY(t)+"H"+this.right).attr("stroke",i).attr("stroke-width",this.options.goalStrokeWidth)},o.prototype.drawEvent=function(t,i){return this.raphael.path("M"+this.transX(t)+","+this.bottom+"V"+this.top).attr("stroke",i).attr("stroke-width",this.options.eventStrokeWidth)},o.prototype.drawYAxisLabel=function(t,i,e){return this.raphael.text(t,i,e).attr("font-size",this.options.gridTextSize).attr("font-family",this.options.gridTextFamily).attr("font-weight",this.options.gridTextWeight).attr("fill",this.options.gridTextColor).attr("text-anchor","end")},o.prototype.drawGridLine=function(t){return this.raphael.path(t).attr("stroke",this.options.gridLineColor).attr("stroke-width",this.options.gridStrokeWidth)},o.prototype.startRange=function(t){return this.hover.hide(),this.selectFrom=t,this.selectionRect.attr({x:t,width:0}).show()},o.prototype.endRange=function(t){var i,e;if(this.selectFrom)return e=Math.min(this.selectFrom,t),i=Math.max(this.selectFrom,t),this.options.rangeSelect.call(this.el,{start:this.data[this.hitTest(e)].x,end:this.data[this.hitTest(i)].x}),this.selectFrom=null},o.prototype.resizeHandler=function(){return this.timeoutId=null,this.raphael.setSize(this.el.width(),this.el.height()),this.redraw()},o}(i.EventEmitter),i.parseDate=function(t){var i,e,o,n,s,r,h,a,l,p,u;return"number"==typeof t?t:(e=t.match(/^(\d+) Q(\d)$/),n=t.match(/^(\d+)-(\d+)$/),s=t.match(/^(\d+)-(\d+)-(\d+)$/),h=t.match(/^(\d+) W(\d+)$/),a=t.match(/^(\d+)-(\d+)-(\d+)[ T](\d+):(\d+)(Z|([+-])(\d\d):?(\d\d))?$/),l=t.match(/^(\d+)-(\d+)-(\d+)[ T](\d+):(\d+):(\d+(\.\d+)?)(Z|([+-])(\d\d):?(\d\d))?$/),e?new Date(parseInt(e[1],10),3*parseInt(e[2],10)-1,1).getTime():n?new Date(parseInt(n[1],10),parseInt(n[2],10)-1,1).getTime():s?new Date(parseInt(s[1],10),parseInt(s[2],10)-1,parseInt(s[3],10)).getTime():h?(4!==(p=new Date(parseInt(h[1],10),0,1)).getDay()&&p.setMonth(0,1+(4-p.getDay()+7)%7),p.getTime()+6048e5*parseInt(h[2],10)):a?a[6]?(r=0,"Z"!==a[6]&&(r=60*parseInt(a[8],10)+parseInt(a[9],10),"+"===a[7]&&(r=0-r)),Date.UTC(parseInt(a[1],10),parseInt(a[2],10)-1,parseInt(a[3],10),parseInt(a[4],10),parseInt(a[5],10)+r)):new Date(parseInt(a[1],10),parseInt(a[2],10)-1,parseInt(a[3],10),parseInt(a[4],10),parseInt(a[5],10)).getTime():l?(u=parseFloat(l[6]),i=Math.floor(u),o=Math.round(1e3*(u-i)),l[8]?(r=0,"Z"!==l[8]&&(r=60*parseInt(l[10],10)+parseInt(l[11],10),"+"===l[9]&&(r=0-r)),Date.UTC(parseInt(l[1],10),parseInt(l[2],10)-1,parseInt(l[3],10),parseInt(l[4],10),parseInt(l[5],10)+r,i,o)):new Date(parseInt(l[1],10),parseInt(l[2],10)-1,parseInt(l[3],10),parseInt(l[4],10),parseInt(l[5],10),i,o).getTime()):new Date(parseInt(t,10),0,1).getTime())},i.Hover=function(){function e(e){null==e&&(e={}),this.options=t.extend({},i.Hover.defaults,e),this.el=t("<div class='"+this.options.class+"'></div>"),this.el.hide(),this.options.parent.append(this.el)}return e.defaults={class:"morris-hover morris-default-style"},e.prototype.update=function(t,i,e){return t?(this.html(t),this.show(),this.moveTo(i,e)):this.hide()},e.prototype.html=function(t){return this.el.html(t)},e.prototype.moveTo=function(t,i){var e,o,n,s,r,h;return r=this.options.parent.innerWidth(),s=this.options.parent.innerHeight(),o=this.el.outerWidth(),e=this.el.outerHeight(),n=Math.min(Math.max(0,t-o/2),r-o),null!=i?(h=i-e-10)<0&&(h=i+10)+e>s&&(h=s/2-e/2):h=s/2-e/2,this.el.css({left:n+"px",top:parseInt(h)+"px"})},e.prototype.show=function(){return this.el.show()},e.prototype.hide=function(){return this.el.hide()},e}(),i.Line=function(t){function e(t){if(this.hilight=s(this.hilight,this),this.onHoverOut=s(this.onHoverOut,this),this.onHoverMove=s(this.onHoverMove,this),this.onGridClick=s(this.onGridClick,this),!(this instanceof i.Line))return new i.Line(t);e.__super__.constructor.call(this,t)}return h(e,t),e.prototype.init=function(){if("always"!==this.options.hideHover)return this.hover=new i.Hover({parent:this.el}),this.on("hovermove",this.onHoverMove),this.on("hoverout",this.onHoverOut),this.on("gridclick",this.onGridClick)},e.prototype.defaults={lineWidth:3,pointSize:4,lineColors:["#0b62a4","#7A92A3","#4da74d","#afd8f8","#edc240","#cb4b4b","#9440ed"],pointStrokeWidths:[1],pointStrokeColors:["#ffffff"],pointFillColors:[],smooth:!0,xLabels:"auto",xLabelFormat:null,xLabelMargin:24,hideHover:!1},e.prototype.calc=function(){return this.calcPoints(),this.generatePaths()},e.prototype.calcPoints=function(){var t,i,e,o,n,s;for(n=this.data,s=[],e=0,o=n.length;e<o;e++)(t=n[e])._x=this.transX(t.x),t._y=function(){var e,o,n,s;for(n=t.y,s=[],e=0,o=n.length;e<o;e++)null!=(i=n[e])?s.push(this.transY(i)):s.push(i);return s}.call(this),s.push(t._ymax=Math.min.apply(Math,[this.bottom].concat(function(){var e,o,n,s;for(n=t._y,s=[],e=0,o=n.length;e<o;e++)null!=(i=n[e])&&s.push(i);return s}())));return s},e.prototype.hitTest=function(t){var i,e,o,n,s;if(0===this.data.length)return null;for(s=this.data.slice(1),i=o=0,n=s.length;o<n&&(e=s[i],!(t<(e._x+this.data[i]._x)/2));i=++o);return i},e.prototype.onGridClick=function(t,i){var e;return e=this.hitTest(t),this.fire("click",e,this.data[e].src,t,i)},e.prototype.onHoverMove=function(t,i){var e;return e=this.hitTest(t),this.displayHoverForRow(e)},e.prototype.onHoverOut=function(){if(!1!==this.options.hideHover)return this.displayHoverForRow(null)},e.prototype.displayHoverForRow=function(t){var i;return null!=t?((i=this.hover).update.apply(i,this.hoverContentForRow(t)),this.hilight(t)):(this.hover.hide(),this.hilight())},e.prototype.hoverContentForRow=function(t){var i,e,o,n,s,r,h;for(o=this.data[t],i="<div class='morris-hover-row-label'>"+o.label+"</div>",h=o.y,e=s=0,r=h.length;s<r;e=++s)n=h[e],i+="<div class='morris-hover-point' style='color: "+this.colorFor(o,e,"label")+"'>\n  "+this.options.labels[e]+":\n  "+this.yLabelFormat(n)+"\n</div>";return"function"==typeof this.options.hoverCallback&&(i=this.options.hoverCallback(t,this.options,i,o.src)),[i,o._x,o._ymax]},e.prototype.generatePaths=function(){var t,e,o,n;return this.paths=function(){var s,r,h,l;for(l=[],e=s=0,r=this.options.ykeys.length;0<=r?s<r:s>r;e=0<=r?++s:--s)n="boolean"==typeof this.options.smooth?this.options.smooth:(h=this.options.ykeys[e],a.call(this.options.smooth,h)>=0),(t=function(){var t,i,n,s;for(n=this.data,s=[],t=0,i=n.length;t<i;t++)void 0!==(o=n[t])._y[e]&&s.push({x:o._x,y:o._y[e]});return s}.call(this)).length>1?l.push(i.Line.createPath(t,n,this.bottom)):l.push(null);return l}.call(this)},e.prototype.draw=function(){var t;if(!0!==(t=this.options.axes)&&"both"!==t&&"x"!==t||this.drawXAxis(),this.drawSeries(),!1===this.options.hideHover)return this.displayHoverForRow(this.data.length-1)},e.prototype.drawXAxis=function(){var t,e,o,n,s,r,h,a,l,p,u=this;for(h=this.bottom+this.options.padding/2,s=null,n=null,t=function(t,i){var e,o,r,a,l;return e=u.drawXAxisLabel(u.transX(i),h,t),l=e.getBBox(),e.transform("r"+-u.options.xLabelAngle),o=e.getBBox(),e.transform("t0,"+o.height/2+"..."),0!==u.options.xLabelAngle&&(a=-.5*l.width*Math.cos(u.options.xLabelAngle*Math.PI/180),e.transform("t"+a+",0...")),o=e.getBBox(),(null==s||s>=o.x+o.width||null!=n&&n>=o.x)&&o.x>=0&&o.x+o.width<u.el.width()?(0!==u.options.xLabelAngle&&(r=1.25*u.options.gridTextSize/Math.sin(u.options.xLabelAngle*Math.PI/180),n=o.x-r),s=o.x-u.options.xLabelMargin):e.remove()},(o=this.options.parseTime?1===this.data.length&&"auto"===this.options.xLabels?[[this.data[0].label,this.data[0].x]]:i.labelSeries(this.xmin,this.xmax,this.width,this.options.xLabels,this.options.xLabelFormat):function(){var t,i,e,o;for(e=this.data,o=[],t=0,i=e.length;t<i;t++)r=e[t],o.push([r.label,r.x]);return o}.call(this)).reverse(),p=[],a=0,l=o.length;a<l;a++)e=o[a],p.push(t(e[0],e[1]));return p},e.prototype.drawSeries=function(){var t,i,e,o,n,s;for(this.seriesPoints=[],t=i=o=this.options.ykeys.length-1;o<=0?i<=0:i>=0;t=o<=0?++i:--i)this._drawLineFor(t);for(s=[],t=e=n=this.options.ykeys.length-1;n<=0?e<=0:e>=0;t=n<=0?++e:--e)s.push(this._drawPointFor(t));return s},e.prototype._drawPointFor=function(t){var i,e,o,n,s,r;for(this.seriesPoints[t]=[],s=this.data,r=[],o=0,n=s.length;o<n;o++)e=s[o],i=null,null!=e._y[t]&&(i=this.drawLinePoint(e._x,e._y[t],this.colorFor(e,t,"point"),t)),r.push(this.seriesPoints[t].push(i));return r},e.prototype._drawLineFor=function(t){var i;if(null!==(i=this.paths[t]))return this.drawLinePath(i,this.colorFor(null,t,"line"),t)},e.createPath=function(t,e,o){var n,s,r,h,a,l,p,u,c,d,f,g,m,y;for(p="",e&&(r=i.Line.gradients(t)),u={y:null},h=m=0,y=t.length;m<y;h=++m)null!=(n=t[h]).y&&(null!=u.y?e?(s=r[h],l=r[h-1],a=(n.x-u.x)/4,c=u.x+a,f=Math.min(o,u.y+a*l),d=n.x-a,g=Math.min(o,n.y-a*s),p+="C"+c+","+f+","+d+","+g+","+n.x+","+n.y):p+="L"+n.x+","+n.y:e&&null==r[h]||(p+="M"+n.x+","+n.y)),u=n;return p},e.gradients=function(t){var i,e,o,n,s,r,h,a;for(e=function(t,i){return(t.y-i.y)/(t.x-i.x)},a=[],o=r=0,h=t.length;r<h;o=++r)null!=(i=t[o]).y?(n=t[o+1]||{y:null},null!=(s=t[o-1]||{y:null}).y&&null!=n.y?a.push(e(s,n)):null!=s.y?a.push(e(s,i)):null!=n.y?a.push(e(i,n)):a.push(null)):a.push(null);return a},e.prototype.hilight=function(t){var i,e,o,n,s;if(null!==this.prevHilight&&this.prevHilight!==t)for(i=e=0,n=this.seriesPoints.length-1;0<=n?e<=n:e>=n;i=0<=n?++e:--e)this.seriesPoints[i][this.prevHilight]&&this.seriesPoints[i][this.prevHilight].animate(this.pointShrinkSeries(i));if(null!==t&&this.prevHilight!==t)for(i=o=0,s=this.seriesPoints.length-1;0<=s?o<=s:o>=s;i=0<=s?++o:--o)this.seriesPoints[i][t]&&this.seriesPoints[i][t].animate(this.pointGrowSeries(i));return this.prevHilight=t},e.prototype.colorFor=function(t,i,e){return"function"==typeof this.options.lineColors?this.options.lineColors.call(this,t,i,e):"point"===e&&this.options.pointFillColors[i%this.options.pointFillColors.length]||this.options.lineColors[i%this.options.lineColors.length]},e.prototype.drawXAxisLabel=function(t,i,e){return this.raphael.text(t,i,e).attr("font-size",this.options.gridTextSize).attr("font-family",this.options.gridTextFamily).attr("font-weight",this.options.gridTextWeight).attr("fill",this.options.gridTextColor)},e.prototype.drawLinePath=function(t,i,e){return this.raphael.path(t).attr("stroke",i).attr("stroke-width",this.lineWidthForSeries(e))},e.prototype.drawLinePoint=function(t,i,e,o){return this.raphael.circle(t,i,this.pointSizeForSeries(o)).attr("fill",e).attr("stroke-width",this.pointStrokeWidthForSeries(o)).attr("stroke",this.pointStrokeColorForSeries(o))},e.prototype.pointStrokeWidthForSeries=function(t){return this.options.pointStrokeWidths[t%this.options.pointStrokeWidths.length]},e.prototype.pointStrokeColorForSeries=function(t){return this.options.pointStrokeColors[t%this.options.pointStrokeColors.length]},e.prototype.lineWidthForSeries=function(t){return this.options.lineWidth instanceof Array?this.options.lineWidth[t%this.options.lineWidth.length]:this.options.lineWidth},e.prototype.pointSizeForSeries=function(t){return this.options.pointSize instanceof Array?this.options.pointSize[t%this.options.pointSize.length]:this.options.pointSize},e.prototype.pointGrowSeries=function(t){return Raphael.animation({r:this.pointSizeForSeries(t)+3},25,"linear")},e.prototype.pointShrinkSeries=function(t){return Raphael.animation({r:this.pointSizeForSeries(t)},25,"linear")},e}(i.Grid),i.labelSeries=function(e,o,n,s,r){var h,a,l,p,u,c,d,f,g,m,y;if(l=200*(o-e)/n,a=new Date(e),void 0===(d=i.LABEL_SPECS[s]))for(y=i.AUTO_LABEL_ORDER,g=0,m=y.length;g<m;g++)if(p=y[g],c=i.LABEL_SPECS[p],l>=c.span){d=c;break}for(void 0===d&&(d=i.LABEL_SPECS.second),r&&(d=t.extend({},d,{fmt:r})),h=d.start(a),u=[];(f=h.getTime())<=o;)f>=e&&u.push([d.fmt(h),f]),d.incr(h);return u},e=function(t){return{span:60*t*1e3,start:function(t){return new Date(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours())},fmt:function(t){return i.pad2(t.getHours())+":"+i.pad2(t.getMinutes())},incr:function(i){return i.setUTCMinutes(i.getUTCMinutes()+t)}}},o=function(t){return{span:1e3*t,start:function(t){return new Date(t.getFullYear(),t.getMonth(),t.getDate(),t.getHours(),t.getMinutes())},fmt:function(t){return i.pad2(t.getHours())+":"+i.pad2(t.getMinutes())+":"+i.pad2(t.getSeconds())},incr:function(i){return i.setUTCSeconds(i.getUTCSeconds()+t)}}},i.LABEL_SPECS={decade:{span:1728e8,start:function(t){return new Date(t.getFullYear()-t.getFullYear()%10,0,1)},fmt:function(t){return""+t.getFullYear()},incr:function(t){return t.setFullYear(t.getFullYear()+10)}},year:{span:1728e7,start:function(t){return new Date(t.getFullYear(),0,1)},fmt:function(t){return""+t.getFullYear()},incr:function(t){return t.setFullYear(t.getFullYear()+1)}},month:{span:24192e5,start:function(t){return new Date(t.getFullYear(),t.getMonth(),1)},fmt:function(t){return t.getFullYear()+"-"+i.pad2(t.getMonth()+1)},incr:function(t){return t.setMonth(t.getMonth()+1)}},week:{span:6048e5,start:function(t){return new Date(t.getFullYear(),t.getMonth(),t.getDate())},fmt:function(t){return t.getFullYear()+"-"+i.pad2(t.getMonth()+1)+"-"+i.pad2(t.getDate())},incr:function(t){return t.setDate(t.getDate()+7)}},day:{span:864e5,start:function(t){return new Date(t.getFullYear(),t.getMonth(),t.getDate())},fmt:function(t){return t.getFullYear()+"-"+i.pad2(t.getMonth()+1)+"-"+i.pad2(t.getDate())},incr:function(t){return t.setDate(t.getDate()+1)}},hour:e(60),"30min":e(30),"15min":e(15),"10min":e(10),"5min":e(5),minute:e(1),"30sec":o(30),"15sec":o(15),"10sec":o(10),"5sec":o(5),second:o(1)},i.AUTO_LABEL_ORDER=["decade","year","month","week","day","hour","30min","15min","10min","5min","minute","30sec","15sec","10sec","5sec","second"],i.Area=function(e){var o;function n(e){var s;if(!(this instanceof i.Area))return new i.Area(e);s=t.extend({},o,e),this.cumulative=!s.behaveLikeLine,"auto"===s.fillOpacity&&(s.fillOpacity=s.behaveLikeLine?.8:1),n.__super__.constructor.call(this,s)}return h(n,e),o={fillOpacity:"auto",behaveLikeLine:!1},n.prototype.calcPoints=function(){var t,i,e,o,n,s,r;for(s=this.data,r=[],o=0,n=s.length;o<n;o++)(t=s[o])._x=this.transX(t.x),i=0,t._y=function(){var o,n,s,r;for(s=t.y,r=[],o=0,n=s.length;o<n;o++)e=s[o],this.options.behaveLikeLine?r.push(this.transY(e)):(i+=e||0,r.push(this.transY(i)));return r}.call(this),r.push(t._ymax=Math.max.apply(Math,t._y));return r},n.prototype.drawSeries=function(){var t,i,e,o,n,s,r,h;for(this.seriesPoints=[],i=this.options.behaveLikeLine?function(){s=[];for(var t=0,i=this.options.ykeys.length-1;0<=i?t<=i:t>=i;0<=i?t++:t--)s.push(t);return s}.apply(this):function(){r=[];for(var t=n=this.options.ykeys.length-1;n<=0?t<=0:t>=0;n<=0?t++:t--)r.push(t);return r}.apply(this),h=[],e=0,o=i.length;e<o;e++)t=i[e],this._drawFillFor(t),this._drawLineFor(t),h.push(this._drawPointFor(t));return h},n.prototype._drawFillFor=function(t){var i;if(null!==(i=this.paths[t]))return i=i+"L"+this.transX(this.xmax)+","+this.bottom+"L"+this.transX(this.xmin)+","+this.bottom+"Z",this.drawFilledPath(i,this.fillForSeries(t))},n.prototype.fillForSeries=function(t){var i;return i=Raphael.rgb2hsl(this.colorFor(this.data[t],t,"line")),Raphael.hsl(i.h,this.options.behaveLikeLine?.9*i.s:.75*i.s,Math.min(.98,this.options.behaveLikeLine?1.2*i.l:1.25*i.l))},n.prototype.drawFilledPath=function(t,i){return this.raphael.path(t).attr("fill",i).attr("fill-opacity",this.options.fillOpacity).attr("stroke","none")},n}(i.Line),i.Bar=function(e){function o(e){if(this.onHoverOut=s(this.onHoverOut,this),this.onHoverMove=s(this.onHoverMove,this),this.onGridClick=s(this.onGridClick,this),!(this instanceof i.Bar))return new i.Bar(e);o.__super__.constructor.call(this,t.extend({},e,{parseTime:!1}))}return h(o,e),o.prototype.init=function(){if(this.cumulative=this.options.stacked,"always"!==this.options.hideHover)return this.hover=new i.Hover({parent:this.el}),this.on("hovermove",this.onHoverMove),this.on("hoverout",this.onHoverOut),this.on("gridclick",this.onGridClick)},o.prototype.defaults={barSizeRatio:.75,barGap:3,barColors:["#0b62a4","#7a92a3","#4da74d","#afd8f8","#edc240","#cb4b4b","#9440ed"],barOpacity:1,barRadius:[0,0,0,0],xLabelMargin:50},o.prototype.calc=function(){var t;if(this.calcBars(),!1===this.options.hideHover)return(t=this.hover).update.apply(t,this.hoverContentForRow(this.data.length-1))},o.prototype.calcBars=function(){var t,i,e,o,n,s,r;for(s=this.data,r=[],t=o=0,n=s.length;o<n;t=++o)(i=s[t])._x=this.left+this.width*(t+.5)/this.data.length,r.push(i._y=function(){var t,o,n,s;for(n=i.y,s=[],t=0,o=n.length;t<o;t++)null!=(e=n[t])?s.push(this.transY(e)):s.push(null);return s}.call(this));return r},o.prototype.draw=function(){var t;return!0!==(t=this.options.axes)&&"both"!==t&&"x"!==t||this.drawXAxis(),this.drawSeries()},o.prototype.drawXAxis=function(){var t,i,e,o,n,s,r,h,a,l,p,u,c;for(l=this.bottom+(this.options.xAxisLabelTopPadding||this.options.padding/2),r=null,s=null,c=[],t=p=0,u=this.data.length;0<=u?p<u:p>u;t=0<=u?++p:--p)h=this.data[this.data.length-1-t],i=this.drawXAxisLabel(h._x,l,h.label),a=i.getBBox(),i.transform("r"+-this.options.xLabelAngle),e=i.getBBox(),i.transform("t0,"+e.height/2+"..."),0!==this.options.xLabelAngle&&(n=-.5*a.width*Math.cos(this.options.xLabelAngle*Math.PI/180),i.transform("t"+n+",0...")),(null==r||r>=e.x+e.width||null!=s&&s>=e.x)&&e.x>=0&&e.x+e.width<this.el.width()?(0!==this.options.xLabelAngle&&(o=1.25*this.options.gridTextSize/Math.sin(this.options.xLabelAngle*Math.PI/180),s=e.x-o),c.push(r=e.x-this.options.xLabelMargin)):c.push(i.remove());return c},o.prototype.drawSeries=function(){var t,i,e,o,n,s,r,h,a,l,p,u,c,d,f;return e=this.width/this.options.data.length,h=this.options.stacked?1:this.options.ykeys.length,t=(e*this.options.barSizeRatio-this.options.barGap*(h-1))/h,this.options.barSize&&(t=Math.min(t,this.options.barSize)),u=e-t*h-this.options.barGap*(h-1),r=u/2,f=this.ymin<=0&&this.ymax>=0?this.transY(0):null,this.bars=function(){var h,u,g,m;for(g=this.data,m=[],o=h=0,u=g.length;h<u;o=++h)a=g[o],n=0,m.push(function(){var h,u,g,m;for(g=a._y,m=[],l=h=0,u=g.length;h<u;l=++h)null!==(d=g[l])?(f?(c=Math.min(d,f),i=Math.max(d,f)):(c=d,i=this.bottom),s=this.left+o*e+r,this.options.stacked||(s+=l*(t+this.options.barGap)),p=i-c,this.options.verticalGridCondition&&this.options.verticalGridCondition(a.x)&&this.drawBar(this.left+o*e,this.top,e,Math.abs(this.top-this.bottom),this.options.verticalGridColor,this.options.verticalGridOpacity,this.options.barRadius),this.options.stacked&&(c-=n),this.drawBar(s,c,t,p,this.colorFor(a,l,"bar"),this.options.barOpacity,this.options.barRadius),m.push(n+=p)):m.push(null);return m}.call(this));return m}.call(this)},o.prototype.colorFor=function(t,i,e){var o,n;return"function"==typeof this.options.barColors?(o={x:t.x,y:t.y[i],label:t.label},n={index:i,key:this.options.ykeys[i],label:this.options.labels[i]},this.options.barColors.call(this,o,n,e)):this.options.barColors[i%this.options.barColors.length]},o.prototype.hitTest=function(t){return 0===this.data.length?null:(t=Math.max(Math.min(t,this.right),this.left),Math.min(this.data.length-1,Math.floor((t-this.left)/(this.width/this.data.length))))},o.prototype.onGridClick=function(t,i){var e;return e=this.hitTest(t),this.fire("click",e,this.data[e].src,t,i)},o.prototype.onHoverMove=function(t,i){var e,o;return e=this.hitTest(t),(o=this.hover).update.apply(o,this.hoverContentForRow(e))},o.prototype.onHoverOut=function(){if(!1!==this.options.hideHover)return this.hover.hide()},o.prototype.hoverContentForRow=function(t){var i,e,o,n,s,r,h,a;for(o=this.data[t],i="<div class='morris-hover-row-label'>"+o.label+"</div>",a=o.y,e=r=0,h=a.length;r<h;e=++r)s=a[e],i+="<div class='morris-hover-point' style='color: "+this.colorFor(o,e,"label")+"'>\n  "+this.options.labels[e]+":\n  "+this.yLabelFormat(s)+"\n</div>";return"function"==typeof this.options.hoverCallback&&(i=this.options.hoverCallback(t,this.options,i,o.src)),n=this.left+(t+.5)*this.width/this.data.length,[i,n]},o.prototype.drawXAxisLabel=function(t,i,e){return this.raphael.text(t,i,e).attr("font-size",this.options.gridTextSize).attr("font-family",this.options.gridTextFamily).attr("font-weight",this.options.gridTextWeight).attr("fill",this.options.gridTextColor)},o.prototype.drawBar=function(t,i,e,o,n,s,r){var h;return(0===(h=Math.max.apply(Math,r))||h>o?this.raphael.rect(t,i,e,o):this.raphael.path(this.roundedRect(t,i,e,o,r))).attr("fill",n).attr("fill-opacity",s).attr("stroke","none")},o.prototype.roundedRect=function(t,i,e,o,n){return null==n&&(n=[0,0,0,0]),["M",t,n[0]+i,"Q",t,i,t+n[0],i,"L",t+e-n[1],i,"Q",t+e,i,t+e,i+n[1],"L",t+e,i+o-n[2],"Q",t+e,i+o,t+e-n[2],i+o,"L",t+n[3],i+o,"Q",t,i+o,t,i+o-n[3],"Z"]},o}(i.Grid),i.Donut=function(e){function o(e){this.resizeHandler=s(this.resizeHandler,this),this.select=s(this.select,this),this.click=s(this.click,this);var o=this;if(!(this instanceof i.Donut))return new i.Donut(e);if(this.options=t.extend({},this.defaults,e),"string"==typeof e.element?this.el=t(document.getElementById(e.element)):this.el=t(e.element),null===this.el||0===this.el.length)throw new Error("Graph placeholder not found.");void 0!==e.data&&0!==e.data.length&&(this.raphael=new Raphael(this.el[0]),this.options.resize&&t(window).bind("resize",function(t){return null!=o.timeoutId&&window.clearTimeout(o.timeoutId),o.timeoutId=window.setTimeout(o.resizeHandler,100)}),this.setData(e.data))}return h(o,e),o.prototype.defaults={colors:["#0B62A4","#3980B5","#679DC6","#95BBD7","#B0CCE1","#095791","#095085","#083E67","#052C48","#042135"],backgroundColor:"#FFFFFF",labelColor:"#000000",formatter:i.commas,resize:!1},o.prototype.redraw=function(){var t,e,o,n,s,r,h,a,l,p,u,c,d,f,g,m,y,v,x,w,b,M,F;for(this.raphael.clear(),e=this.el.width()/2,o=this.el.height()/2,d=(Math.min(e,o)-10)/3,u=0,w=this.values,f=0,y=w.length;f<y;f++)c=w[f],u+=c;for(a=5/(2*d),t=1.9999*Math.PI-a*this.data.length,r=0,s=0,this.segments=[],b=this.values,n=g=0,v=b.length;g<v;n=++g)c=b[n],l=r+a+t*(c/u),(p=new i.DonutSegment(e,o,2*d,d,r,l,this.data[n].color||this.options.colors[s%this.options.colors.length],this.options.backgroundColor,s,this.raphael)).render(),this.segments.push(p),p.on("hover",this.select),p.on("click",this.click),r=l,s+=1;for(this.text1=this.drawEmptyDonutLabel(e,o-10,this.options.labelColor,15,800),this.text2=this.drawEmptyDonutLabel(e,o+10,this.options.labelColor,14),h=Math.max.apply(Math,this.values),s=0,M=this.values,F=[],m=0,x=M.length;m<x;m++){if((c=M[m])===h){this.select(s);break}F.push(s+=1)}return F},o.prototype.setData=function(t){var i;return this.data=t,this.values=function(){var t,e,o,n;for(o=this.data,n=[],t=0,e=o.length;t<e;t++)i=o[t],n.push(parseFloat(i.value));return n}.call(this),this.redraw()},o.prototype.click=function(t){return this.fire("click",t,this.data[t])},o.prototype.select=function(t){var i,e,o,n;for(n=this.segments,e=0,o=n.length;e<o;e++)n[e].deselect();return this.segments[t].select(),i=this.data[t],this.setLabels(i.label,this.options.formatter(i.value,i))},o.prototype.setLabels=function(t,i){var e,o,n,s,r,h,a,l;return e=2*(Math.min(this.el.width()/2,this.el.height()/2)-10)/3,s=1.8*e,n=e/2,o=e/3,this.text1.attr({text:t,transform:""}),r=this.text1.getBBox(),h=Math.min(s/r.width,n/r.height),this.text1.attr({transform:"S"+h+","+h+","+(r.x+r.width/2)+","+(r.y+r.height)}),this.text2.attr({text:i,transform:""}),a=this.text2.getBBox(),l=Math.min(s/a.width,o/a.height),this.text2.attr({transform:"S"+l+","+l+","+(a.x+a.width/2)+","+a.y})},o.prototype.drawEmptyDonutLabel=function(t,i,e,o,n){var s;return s=this.raphael.text(t,i,"").attr("font-size",o).attr("fill",e),null!=n&&s.attr("font-weight",n),s},o.prototype.resizeHandler=function(){return this.timeoutId=null,this.raphael.setSize(this.el.width(),this.el.height()),this.redraw()},o}(i.EventEmitter),i.DonutSegment=function(t){function i(t,i,e,o,n,r,h,a,l,p){this.cx=t,this.cy=i,this.inner=e,this.outer=o,this.color=h,this.backgroundColor=a,this.index=l,this.raphael=p,this.deselect=s(this.deselect,this),this.select=s(this.select,this),this.sin_p0=Math.sin(n),this.cos_p0=Math.cos(n),this.sin_p1=Math.sin(r),this.cos_p1=Math.cos(r),this.is_long=r-n>Math.PI?1:0,this.path=this.calcSegment(this.inner+3,this.inner+this.outer-5),this.selectedPath=this.calcSegment(this.inner+3,this.inner+this.outer),this.hilight=this.calcArc(this.inner)}return h(i,t),i.prototype.calcArcPoints=function(t){return[this.cx+t*this.sin_p0,this.cy+t*this.cos_p0,this.cx+t*this.sin_p1,this.cy+t*this.cos_p1]},i.prototype.calcSegment=function(t,i){var e,o,n,s,r,h,a,l,p,u;return p=this.calcArcPoints(t),e=p[0],n=p[1],o=p[2],s=p[3],u=this.calcArcPoints(i),r=u[0],a=u[1],h=u[2],l=u[3],"M"+e+","+n+"A"+t+","+t+",0,"+this.is_long+",0,"+o+","+s+"L"+h+","+l+"A"+i+","+i+",0,"+this.is_long+",1,"+r+","+a+"Z"},i.prototype.calcArc=function(t){var i,e,o,n,s;return s=this.calcArcPoints(t),i=s[0],o=s[1],e=s[2],n=s[3],"M"+i+","+o+"A"+t+","+t+",0,"+this.is_long+",0,"+e+","+n},i.prototype.render=function(){var t=this;return this.arc=this.drawDonutArc(this.hilight,this.color),this.seg=this.drawDonutSegment(this.path,this.color,this.backgroundColor,function(){return t.fire("hover",t.index)},function(){return t.fire("click",t.index)})},i.prototype.drawDonutArc=function(t,i){return this.raphael.path(t).attr({stroke:i,"stroke-width":2,opacity:0})},i.prototype.drawDonutSegment=function(t,i,e,o,n){return this.raphael.path(t).attr({fill:i,stroke:e,"stroke-width":3}).hover(o).click(n)},i.prototype.select=function(){if(!this.selected)return this.seg.animate({path:this.selectedPath},150,"<>"),this.arc.animate({opacity:1},150,"<>"),this.selected=!0},i.prototype.deselect=function(){if(this.selected)return this.seg.animate({path:this.path},150,"<>"),this.arc.animate({opacity:0},150,"<>"),this.selected=!1},i}(i.EventEmitter)}).call(this)}});if("object"==typeof e){var o=["object"==typeof module&&"object"==typeof module.exports?module.exports:null,"undefined"!=typeof window?window:null,t&&t!==window?t:null];for(var n in e)o[0]&&(o[0][n]=e[n]),o[1]&&"__esModule"!==n&&(o[1][n]=e[n]),o[2]&&(o[2][n]=e[n])}}(this);