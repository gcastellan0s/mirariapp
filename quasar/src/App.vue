<template>
  <div id="q-app">
    <transition name="slide-right" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<style src="@appwork/vendor/styles/bootstrap-material.scss" lang="scss"></style>
<style src="@appwork/vendor/styles/appwork-material.scss" lang="scss"></style>
<style src="@appwork/vendor/styles/theme-gradient-material.scss" lang="scss"></style>
<style src="@appwork/vendor/styles/colors-material.scss" lang="scss"></style>
<style src="@appwork/vendor/styles/uikit.scss" lang="scss"></style>
<style src="@appwork/style.scss" lang="scss"></style>

<script>
  import { mapGetters } from 'vuex';
  import M from '@mirari/variables/M' 
  export default {
    name: 'App',
    metaInfo: {
      title: M.TITLE,
      titleTemplate: '%s :: ' + M.SLOGAN
    },
    updated () {
      setTimeout(() => document.body.classList.remove('app-loading'), 1)
    },
    computed: mapGetters('auth', ['isAuthenticated',]),
  }
</script>

<style>
</style>