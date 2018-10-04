APP = 'CRYE'

MENU = {
    'CRYE': {
        'title': 'CREDIPyME',
        'modules': [
            {
                'title': 'SIEBEL DESBLOQUEO',
                'icon': 'flaticon-lifebuoy',
                'text': 'Desbloquea trenes de crédito',
                'subtext': 'Desbloqueo de tren de credito del sistema SIEBEL',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.SiebelUnblock',
                'href': 'CRYE:SiebelUnblock__SiebelUnblock__TemplateView',
            },
        ]
    }
}