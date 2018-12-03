<template lang="pug">
    .d-flex.justify-content-center.align-items-center
        .ui-w-60
            .w-100.position-relative(style='padding-bottom: 54%')
            img(:src='M.LOGOBG',  style='max-width: 300px;')
</template>

<script>
	export default {
		metaInfo: {
			title: 'Dashboard',
		},
		data() {
			return {
                dashboard:{
					rememberMe: false
				},
			};
		},
		methods: {

		},
		mounted: function () {
			//console.log(M().M.TITLE)
		},
	}
</script>