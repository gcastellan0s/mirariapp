webpackJsonp([0],{KX5y:function(t,a,e){"use strict";Object.defineProperty(a,"__esModule",{value:!0});e("9qAv"),e("mw3O");var s={name:"app-layout-navbar",props:{sidenavToggle:{type:Boolean,default:!0}},methods:{toggleSidenav:function(){this.layoutHelpers.toggleCollapsed()},getLayoutNavbarBg:function(){return this.layoutNavbarBg}},mounted:function(){}},n={render:function(){var t=this,a=t.$createElement,e=t._self._c||a;return e("b-navbar",{staticClass:"layout-navbar align-items-lg-center container-p-x",attrs:{toggleable:"lg",variant:t.getLayoutNavbarBg()}},[e("b-navbar-brand",{attrs:{to:"/"}},[t._v("CREDIPyME :: UNION DE CREDITO")]),t._v(" "),t.sidenavToggle?e("b-navbar-nav",{staticClass:"align-items-lg-center mr-auto mr-lg-4"},[e("a",{staticClass:"nav-item nav-link px-0 ml-2 ml-lg-0",attrs:{href:"javascript:void(0)"},on:{click:t.toggleSidenav}},[e("i",{staticClass:"ion ion-md-menu text-large align-middle"})])]):t._e(),t._v(" "),e("b-navbar-toggle",{attrs:{target:"app-layout-navbar"}}),t._v(" "),e("b-collapse",{attrs:{"is-nav":"",id:"app-layout-navbar"}},[e("b-navbar-nav",{staticClass:"align-items-lg-center ml-auto"},[e("div",{staticClass:"nav-item d-none d-lg-block text-big font-weight-light line-height-1 opacity-25 mr-3 ml-1"},[t._v("|")]),t._v(" "),e("b-nav-item-dropdown",{staticClass:"demo-navbar-user",attrs:{right:!t.isRTL}},[e("template",{slot:"button-content"},[e("span",{staticClass:"d-inline-flex flex-lg-row-reverse align-items-center align-middle"},[e("span",{staticClass:"px-1 mr-lg-2 ml-2 ml-lg-0"},[t._v("Mike Greene")])])]),t._v(" "),e("b-dd-item",[e("i",{staticClass:"ion ion-ios-person text-lightest"}),t._v("   My profile")]),t._v(" "),e("b-dd-item",[e("i",{staticClass:"ion ion-ios-mail text-lightest"}),t._v("   Messages")]),t._v(" "),e("b-dd-item",[e("i",{staticClass:"ion ion-md-settings text-lightest"}),t._v("   Account settings")]),t._v(" "),e("b-dd-divider"),t._v(" "),e("b-dd-item",{attrs:{to:"logout"}},[e("i",{staticClass:"ion ion-ios-log-out text-danger"}),t._v("   SALIR")])],2)],1)],1)],1)},staticRenderFns:[]},i={render:function(){var t=this.$createElement;return(this._self._c||t)("div")},staticRenderFns:[]},l={name:"app-layout-without-sidenav",components:{"app-layout-navbar":e("VU/8")(s,n,!1,null,null,null).exports,"app-layout-footer":e("VU/8")({name:"app-layout-footer",methods:{getLayoutFooterBg:function(){return"bg-"+this.layoutFooterBg}}},i,!1,null,null,null).exports},mounted:function(){this.layoutHelpers._removeClass("layout-expanded"),this.layoutHelpers.init(),this.layoutHelpers.update(),this.layoutHelpers.setAutoUpdate(!0)},beforeDestroy:function(){this.layoutHelpers.destroy()}},o={render:function(){var t=this.$createElement,a=this._self._c||t;return a("div",{staticClass:"layout-wrapper layout-1 layout-without-sidenav"},[a("div",{staticClass:"layout-inner"},[a("app-layout-navbar",{attrs:{sidenavToggle:!1}}),this._v(" "),a("div",{staticClass:"layout-container"},[a("div",{staticClass:"layout-content"},[a("div",{staticClass:"router-transitions container-fluid flex-grow-1 container-p-y"},[a("router-view")],1),this._v(" "),a("app-layout-footer")],1)])],1)])},staticRenderFns:[]},r=e("VU/8")(l,o,!1,null,null,null);a.default=r.exports}});
//# sourceMappingURL=0.fc0993e9535401e4ad3f.js.map