<template lang="pug">
    .authentication-wrapper.authentication-1.px-4
        .authentication-inner.py-5
            // Logo
            .d-flex.justify-content-center.align-items-center
            .ui-w-60
                .w-100.position-relative(style='padding-bottom: 54%')
                img(:src='M.LOGOBG',  style='max-width: 300px;')
            // / Logo
            // Form
            form.my-5
                b-form-group(label='Usuario o Email')
                    b-input(v-model='credentials.username')
                b-form-group
                    .d-flex.justify-content-between.align-items-end(slot='label')
                        div Contraseña
                        a.d-block.small(href='javascript:void(0)') Olvidaste tu contraseña?
                    b-input(type='password' v-model='credentials.password')
                .d-flex.justify-content-between.align-items-center.m-0
                    b-check.m-0(v-model='credentials.rememberMe') Recuerdame
                    b-btn(variant='primary' @click="login(credentials)") ENTRAR
            // / Form
            .text-center.text-muted
                | {{M.TITLE}} :: {{M.SLOGAN}}
</template>

<style src="@/vendor/styles/pages/authentication.scss" lang="scss"></style>

<script>
    export default {
        name: 'login',
        metaInfo: {
            title: require('@/../../package.json').title,
        },
        data() {
            return {
                credentials:{
                    username: 'gcastellan0s',
                    password: 'H1dr4Gu51*',
                    rememberMe: false
                },
            };
        },
        methods: {
            login({ username, password }) {
                username = this.M.CODE + '__' + username
                this.$store.dispatch('auth/login', {username, password})
                .then(() => this.$router.push('/'));
            },
        },
        mounted: function () {
        },
    }
</script>