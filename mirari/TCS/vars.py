APP = 'TCS'

MENU = {
    'TCS': {
        'title': 'ORDENES DE SERVICIO',
        'modules': [
			{
				'title': 'Ordenes de servicio',
				'icon': 'flaticon-edit-1',
				'text': 'Lista y altas de servicios',
				'subtext': 'Administra ordenes de servicio en el sistemas',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.OrderService',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Empresas',
				'icon': 'flaticon-bag',
				'text': 'Administración de empresas',
				'subtext': 'Configura empresas en el sistema',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Company',
				'url': 'Generic__ListView',
			},
            {
				'title': 'Tiendas',
				'icon': 'flaticon-map-location',
				'text': 'Administración de tiendas',
				'subtext': 'Configura tiendas en el sistema',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Store',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Marcas',
				'icon': 'flaticon-interface-9',
				'text': 'Administración de marcas',
				'subtext': 'Configura tiendas en el sistema',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Brand',
				'url': 'Generic__ListView',
			},
			{
				'title': 'Modelos',
				'icon': 'flaticon-notes',
				'text': 'Administración de modelos',
				'subtext': 'Administra modelos de caminadoras y gimnasios',
				'apps': [APP, ],
				'permission': 'Can_View',
				'model': APP + '.Modelo',
				'url': 'Generic__ListView',
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