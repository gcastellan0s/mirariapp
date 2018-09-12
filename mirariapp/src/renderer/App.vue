<template>
  <div id="app">
    <transition name="slide-right" mode="out-in">
      <router-view/>
    </transition>
  </div>
</template>

<style src="@/vendor/styles/bootstrap-material.scss" lang="scss"></style>
<style src="@/vendor/styles/appwork-material.scss" lang="scss"></style>
<style src="@/vendor/styles/theme-soft-material.scss" lang="scss"></style>
<style src="@/vendor/styles/colors-material.scss" lang="scss"></style>
<style src="@/vendor/styles/uikit.scss" lang="scss"></style>
<style src="@/vendor/style.scss" lang="scss"></style>

<script>
  import { mapGetters } from 'vuex';
  export default {
    name: 'app',
    metaInfo: {
      title: require('@/../../package.json').title,
      titleTemplate: '%s :: ' + require('@/../../package.json').slogan
    },
    updated () {
      setTimeout(() => document.body.classList.remove('app-loading'), 1)
    },
    computed: mapGetters('auth', ['isAuthenticated',]),
  }
</script>