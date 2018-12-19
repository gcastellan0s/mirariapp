APP = 'PHOTO'

MENU = {
	'PHOTO': {
		'title': 'GALERIA',
		'modules': [
			{
				'title': 'GALERIA PÁGINA PRINCIPAL',
				'icon': 'fa fa-camera-retro',
				'text': 'GALERIA DE FOTOS',
				'subtext': 'Administra la galeria de tu página principal',
				'apps': ['PHOTO',],
				'permission': 'Can_View',
				'model': APP + '.Photo',
				'url': 'Generic__ListView',
			},
		]
	},
}