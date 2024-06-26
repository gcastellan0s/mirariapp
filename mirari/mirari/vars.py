from .extra_vars import *

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
				'title': 'USUARIOS',
				'icon': 'flaticon-profile',
				'text': 'ADMINISTRACION DE USUARIOS',
				'subtext': 'Herramientas para la administracion de usuarios',
				'apps': ['mirari', ],
				'permission': 'Can_View',
				'model': APP + '.User',
				'url': 'User__ListView',
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
		]
	},
}

MMENU = {}
MMENU.update(MENU)

from mirari.INT.vars import MENU as INTMENU
MMENU.update(INTMENU)

from mirari.SV.vars import MENU as SVMENU
MMENU.update(SVMENU)

from mirari.INV.vars import MENU as INV
MMENU.update(INV)

from mirari.CRYE.vars import MENU as CRYEMENU
MMENU.update(CRYEMENU)

from mirari.TCS.vars import MENU as TCS
MMENU.update(TCS)

from mirari.SIEBEL.vars import MENU as SIEBEL
MMENU.update(SIEBEL)

from mirari.STR.vars import MENU as STR
MMENU.update(STR)

