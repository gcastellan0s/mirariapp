APP = 'INV'

MENU = {
    'INV': {
        'title': 'SU FACTURA',
        'modules': [
            {
                'title': 'DATOS FISCALES',
                'icon': 'flaticon-avatar',
                'text': 'LISTADO DE DATOS FISCALES',
                'subtext': 'Listado de tus empesas o personas físicas',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model':  APP + '.FiscalMX',
                'url': 'Generic__ListView',
            },
            {
                'title': 'MIS FACTURAS',
                'icon': 'flaticon-doc',
                'text': 'CONSULTA TUS FACTURAS',
                'subtext': 'Listado de tus facturas en el sistema',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model':  APP + '.Invoice',
                'url': 'Generic__ListView',
            },
        ],
    },
}