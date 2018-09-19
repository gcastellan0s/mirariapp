APP = 'SV'

MENU = {
    'SV': {
        'title': 'SUVENTA',
        'modules': [
            {
                'title': 'PUNTOS DE VENTA',
                'icon': 'flaticon-piggy-bank',
                'text': 'MIS PUNTOS DE VENTA',
                'subtext': 'Administra y organiza tus Puntos de Venta',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model':  APP + '.Sellpoint',
                'url': 'Generic__ListView',
            },
            {
                'title': 'MENUS',
                'icon': 'flaticon-list-1',
                'text': 'MENUS DEL PUNTO DE VENTA',
                'subtext': 'Organiza tus productos por medio de menús',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model':  APP + '.User',
                'url': 'Generic__ListView',
            },
            {
                'title': 'PRODUCTOS',
                'icon': 'flaticon-open-box',
                'text': 'LISTADO DE PRODUCTOS',
                'subtext': 'Listado de productos que se ofertan en el PV',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Product',
                'url': 'Generic__ListView',
            },
        ]
    }
}