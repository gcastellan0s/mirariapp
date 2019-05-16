$('#id_{{key}}').multiSelect({
	selectableHeader: '<input type="text" class="form-control form-control-sm kt-input search-input" autocomplete="off" placeholder="Filtrar...">',
	selectionHeader: '<input type="text" class="form-control form-control-sm kt-input search-input" autocomplete="off" placeholder="Filtrar...">',
	selectableFooter: '<button type="button" class="btn btn-secondary btn-block kt--margin-top-5 btn-sm" style="background-color: #f7f7f7;border:1px solid #b9b9b9;">QUITAR TODOS</button>',
	selectionFooter: '<button type="button" class="btn btn-secondary btn-block kt--margin-top-5 btn-sm" style="background-color: #f7f7f7;border:1px solid #b9b9b9;">AGREGAR TODOS</button>',
	afterInit: function(ms){
		var that = this,
		$selectableSearch = that.$selectableUl.prev(),
		$deselectall = that.$selectableUl.next(),
		$selectionSearch = that.$selectionUl.prev(),
		$selectall = that.$selectionUl.next(),
		selectableSearchString = '#'+that.$container.attr('id')+' .ms-elem-selectable:not(.ms-selected)',
		selectionSearchString = '#'+that.$container.attr('id')+' .ms-elem-selection.ms-selected';
		that.qs1 = $selectableSearch.quicksearch(selectableSearchString).on('keydown', function(e){
			if (e.which === 40){
				that.$selectableUl.focus();
				return false;
			}
		});
		$deselectall.on('click', function(e){
			that.$element.multiSelect('deselect_all');
		});
		that.$selectableUl.prev().wrap( '<div class="kt-input-icon kt-input-icon--left kt--margin-bottom-5"></div>' ).after('<span class="kt-input-icon__icon kt-input-icon__icon--left"><span><i class="la la-search"></i></span></span>');
		that.qs2 = $selectionSearch.quicksearch(selectionSearchString).on('keydown', function(e){
			if (e.which == 40){
				that.$selectionUl.focus();
				return false;
			}
		});
		$selectall.on('click', function(e){
			that.$element.multiSelect('select_all');
		});
		that.$selectionUl.prev().wrap( '<div class="kt-input-icon kt-input-icon--left kt--margin-bottom-5"></div>' ).after('<span class="kt-input-icon__icon kt-input-icon__icon--left"><span><i class="la la-search"></i></span></span>');
	},
	afterSelect: function(){
		this.qs1.cache();
		this.qs2.cache();
	},
	afterDeselect: function(){
		this.qs1.cache();
		this.qs2.cache();
	}
});