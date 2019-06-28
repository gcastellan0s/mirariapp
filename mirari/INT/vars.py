APP = 'INT'

MENU = {
    'INT': {
        'title': 'INTRANET',
        'modules': [
            #{
                #'title': 'CATÁLOGO DE DOCUMENTOS',
                #'icon': 'flaticon-book',
                #'text': 'LISTADO DE CÓDIGOS',
                #'subtext': 'Listado de los códigos de documentos.',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.Catalogue',
                #'url': 'Generic__ListView',
            #},
            {
                'title': 'Directorio',
                'icon': 'flaticon-users',
                'text': 'Directorio de empleados',
                'subtext': 'Empleados en la organización',
                'apps': [APP,],
                'permission': 'Can_View',
                'model': APP + '.Team',
                'href': 'INT:EmployeDirectory__ListView',
            },
            {
                'title': 'EQUIPOS',
                'icon': 'flaticon-network',
                'text': 'Equipos de trabajo',
                'subtext': 'Departamentos, Equipos y Grupos de trabajo.',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Team',
                'url': 'Generic__ListView',
            },
            {
                'title': 'MANUALES',
                'icon': 'flaticon-layers',
                'text': 'Colleción de manuales',
                'subtext': 'Manuales y procedimientos.',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Handbook',
                'url': 'Generic__ListView',
            },
            #{
                #'title': 'BUZÓN INTERNO',
                #'icon': 'flaticon-email-black-circular-button',
                #'text': 'Configuración de Buzones',
                #'subtext': 'Buzones internos disponibles en la organización',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.InternalMailBox',
                #'url': 'Generic__ListView',
            #},
            #{
                #'title': 'CANALES DE COMUNICACIÓN',
                #'icon': 'flaticon-speech-bubble-1',
                #'text': 'Lista de canales',
                #'subtext': 'Canales para avisos en la organización',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.Channel',
                #'url': 'Generic__ListView',
            #},
            {
                'title': 'ENVIO DE NOTIFICACIONES',
                'icon': 'flaticon-paper-plane',
                'text': 'Envía notificaciones por canal',
                'subtext': 'Envía notificaciones a los destinatarios de un canal',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Notification',
                'url': 'Generic__ListView',
            },
        ]
    }
}

NOTIFICATION_STATUS = (
	('Borrador', 'Borrador'),
	('Publicado', 'Publicado'),
)