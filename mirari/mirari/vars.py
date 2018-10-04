APP = 'mirari'

GENDER = (
	('Hombre', 'Hombre'),
	('Mujer', 'Mujer'),
	('Otro', 'Otro'),
)

MENU = {
	'mirari': {
		'title': 'ORGANIZACIÓN',
		'modules': [
			{
				'title': 'ORGANIZACIóN',
				'icon': 'flaticon-map',
				'text': 'CONFIGURA TU ORGANIZACIÓN',
				'subtext': 'Administra tus organizaciones del sistema',
				'apps': ['mirari',],
				'permission': 'Can_View',
				'model': APP + '.Organization',
				'url': 'Generic__ListView',
			},
			{
				'title': 'PERFILES',
				'icon': 'flaticon-squares-3',
				'text': 'ADMINISTRACIÓN DE PERFILES Y PERMISOS',
				'subtext': 'Configura nuevos perfiles o permisos del sistema',
				'apps': ['mirari', ],
				'permission': 'Can_View',
				'model': APP + '.Profile',
				'url': 'Generic__ListView',
			},
			{
				'title': 'USUARIOS',
				'icon': 'flaticon-profile',
				'text': 'ADMINISTRACION DE USUARIOS',
				'subtext': 'Herramientas para la administracion de usuarios',
				'apps': ['mirari', ],
				'permission': 'Can_View',
				'model': APP + '.User',
				'url': 'User__ListView',
			},
		]
	},
}

MMENU = {}
MMENU.update(MENU)

from SV.vars import MENU as SVMENU
MMENU.update(SVMENU)

from INT.vars import MENU as INTMENU
MMENU.update(INTMENU)

from CRYE.vars import MENU as CRYEMENU
MMENU.update(CRYEMENU)