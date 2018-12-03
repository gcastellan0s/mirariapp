<template src="@/layouts/pug/Layout2.pug" lang="pug"></template>
<script>
  import LayoutNavbar from './LayoutNavbar'
  import LayoutSidenav from './LayoutSidenav'
  import LayoutFooter from './LayoutFooter'
  export default {
    name: 'app-layout-2',
    components: {
      'app-layout-navbar': LayoutNavbar,
      'app-layout-sidenav': LayoutSidenav,
      'app-layout-footer': LayoutFooter
    },
    mounted () {
      this.layoutHelpers.init()
      this.layoutHelpers.update()
      this.layoutHelpers.setAutoUpdate(true)
    },
    beforeDestroy () {
      this.layoutHelpers.destroy()
    },
    methods: {
      closeSidenav () {
        this.layoutHelpers.setCollapsed(true)
      }
    }
  }
</script>
