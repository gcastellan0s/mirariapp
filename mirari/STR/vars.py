APP = 'STR'

MENU = {
	'STR': {
		'title': 'ALMACEN',
		'modules': [
			{
				'title': 'Almacenes',
				'icon': 'fas fa-box-open',
				'text': 'Administracion de almacenes',
				'subtext': 'Controla los datos de tus almacenes',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Storehouse',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Proveedores',
				'icon': 'fab fa-black-tie',
				'text': 'Administracion de proveedores',
				'subtext': 'Controla la mercancia de los proveedores',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Provider',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Categoria de Productos',
				'icon': 'fas fa-clone',
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
				'model': APP + '.Product',
				'url': 'Generic__ListView',
			},
		]
	},
}