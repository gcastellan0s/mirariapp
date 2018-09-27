APP = 'INT'

MENU = {
    'INT': {
        'title': 'INTRANET',
        'modules': [
            {
                'title': 'CATÁLOGO DE DOCUMENTOS',
                'icon': 'flaticon-book',
                'text': 'LISTADO DE CÓDIGOS',
                'subtext': 'Listado de los códigos de documentos.',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Catalogue',
                'url': 'Generic__ListView',
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
        ]
    }
}