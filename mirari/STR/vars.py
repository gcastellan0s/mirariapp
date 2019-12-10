APP = 'STR'

MENU = {
	'STR': {
		'title': 'PRODUCTOS DE INVENTARIO',
		'modules': [
			{
				'title': 'Categoria de Productos',
				'icon': 'fas fa-box',
				'text': 'Categorias de los productos',
				'subtext': 'Asocia productos a una categoría',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.CategoryProduct',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Productos',
				'icon': 'fas fa-box',
				'text': 'Productos en el almacén',
				'subtext': 'Administra todos los productos que deseas administrar',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.InventoryProduct',
				'url': 'Generic__ListView',
			},
		]
	},
}