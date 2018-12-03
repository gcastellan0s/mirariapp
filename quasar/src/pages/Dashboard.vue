<template lang="pug">
    .authentication-wrapper.authentication-1.px-4
        .authentication-inner.py-5
            // Logo
            .d-flex.justify-content-center.align-items-center
            .ui-w-60
                .w-100.position-relative(style='padding-bottom: 54%')
                img(:src='M.LOGOBG',  style='max-width: 300px;')
</template>

<style src="@appwork/vendor/styles/pages/authentication.scss" lang="scss"></style>

<script>
	import M from '@mirari/variables/M' 
	export default {
		name: 'login',
		metaInfo: {
			title: M.TITLE,
		},
		data() {
			return {
				credentials:{
					username: 'credipyme__gcastellan0s',
					password: 'H1dr4Gu51*',
					rememberMe: false
				},
			};
		},
		methods: {
			
		},
		mounted: function () {
			console.log(M().M.TITLE)
		},
	}
</script>