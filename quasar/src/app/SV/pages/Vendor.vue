<template lang="pug">
  div
	.row
	  .col-4.pr-0.pl-2
		.d-flex.col-xl-12.align-items-stretch(style='padding-right:.5rem;padding-left:.5rem;')
		  // Stats + Links
		  .card.d-flex.w-100.mb-4
			.row.no-gutters.row-bordered.row-border-light.h-100
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('1')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 1
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('2')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 2
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('3')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 3
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('4')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 4
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('5')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 5
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('6')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 6
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('7')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 7
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('8')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 8
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('9')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 9
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('<')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder <
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('0')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder 0
			  .d-flex.col-sm-4.align-items-center
				button.btn.btn-default.card-body.align-items-center.text-dark.text-center.waves-effect(v-on:click="keyboard('.')")
				  span.media-body.d-block
					span.text-big.font-weight-bolder .
		  // / Stats + Links
	  .col-8.px-0
		  .d-flex.flex-md-column.flex-wrap.justify-content-md-center.align-items-center.px-3.px-md-0.pt-md-4.pb-4.masonry-item(v-masonry-tile='' v-for='productattribute in productattributes' v-if="productattribute.sellpoint === active_sellpoint.id")
			.text-big.m-2
			  strong {{ productattribute.price|currency }} | {{productattribute.sellpoint}} | {{active_sellpoint.id}}
			p
			  | {{ productattribute.product.name }} 
			//
			  .text-muted.small.m-2  7 items available
</template>
<style>
  .masonry-item {
	width: 145px;
	height: 130px;
	float: left;
	border-radius: 5px;
	border: 1px solid #7b7b7b;
  }
</style>

<script>
  import { mapMutations, mapState } from 'vuex';
  import moment from 'moment'
  export default {
	name: 'pages-help-center',
	metaInfo: {
	  title: 'Vendedor'
	},
	data: function () {
	  return {
		hoy: moment().format("DD/MM/YY"),
	  }
	},
	methods: {
	  ...mapMutations('SV', ['keyboard',]),
	},
	computed: {
	  ...mapState('SV', ['productattributes','active_sellpoint']),
		},
  }
</script>
