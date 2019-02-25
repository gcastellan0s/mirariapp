APP = 'TCS'

MENU = {
	'TCS': {
		'title': 'ORDENES DE SERVICIO',
		'modules': [
			{
				'title': 'Ordenes de servicio',
				'icon': 'flaticon-list',
				'text': 'Lista y altas de servicios',
				'subtext': 'Administra ordenes de servicio en el sistemas',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.OrderService',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Calendario de ordenes',
				'icon': 'flaticon-event-calendar-symbol',
				'text': 'Calendario de ordenes de servicio',
				'subtext': 'Administra ordenes de servicio desde el calendario',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.OrderService',
				'href': 'TCS:calendar__OrderService__TemplateView',
			},
			{
				'title': 'Empresas',
				'icon': 'flaticon-customer',
				'text': 'Administración de empresas',
				'subtext': 'Configura empresas en el sistema',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Company',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Tiendas',
				'icon': 'flaticon-shopping-basket',
				'text': 'Administración de tiendas',
				'subtext': 'Configura tiendas en el sistema',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Store',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Marcas',
				'icon': 'flaticon-price-tag',
				'text': 'Administración de marcas',
				'subtext': 'Configura tiendas en el sistema',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Brand',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Modelos',
				'icon': 'flaticon-interface-9',
				'text': 'Administración de modelos',
				'subtext': 'Administra modelos de caminadoras y gimnasios',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Modelo',
				'url': 'Generic__ListView',
			},
		]
	},
	'TCS__utilidades': {
		'title': 'UTILIDADES',
		'modules': [
			{
				'title': 'Correo electrónico',
				'icon': 'flaticon-paper-plane',
				'text': 'Consulta tu correo',
				'subtext': 'Ingresa a tu buzón electrónico',
				'apps': [APP, ],
				'permission': '',
				'model': APP + '.OrderService',
				'link': 'https://mail.yandex.com/',
			},
			{
				'title': 'Manulaes Usuario',
				'icon': 'flaticon-users-1',
				'text': 'Manuales de usuario',
				'subtext': 'Consulta los manuales de usuario',
				'apps': [APP, ],
				'permission': '',
				'model': APP + '.OrderService',
				'href': 'TCS:manuales_usuario__OrderService__TemplateView',
			},
			{
				'title': 'Manuales IconField',
				'icon': 'flaticon-layer',
				'text': 'Consulta tu correo',
				'subtext': 'Ingresa a tu buzón electrónico',
				'apps': [APP, ],
				'permission': '',
				'model': APP + '.OrderService',
				'href': 'TCS:manuales_iconfield__OrderService__TemplateView',
			},
		]
	}
}

ESTATUS= (
	('Nueva', 'Nueva'),
	('Alerta', 'Alerta'),
	('Espera de refacciones', 'Espera de refacciones'),
	('Terminada', 'Terminada'),
	('Cancelada', 'Cancelada'),
	('Especial', 'Especial'),
)
SERVICIO = (
	('Icon', 'Icon'),
	('Tecnoservicio', 'Tecnoservicio'),
)
ZONAS = (
	('Local', 'Local'),
	('Foraneo', 'Foraneo'),
)
CONCEPTO = (
	('Armado', 'Armado'),
	('Revision', 'Revision'),
	('OrdenesIcon', 'OrdenesIcon'),
	('Mantenimiento', 'Mantenimiento'),
	('Servicio', 'Servicio'),
)