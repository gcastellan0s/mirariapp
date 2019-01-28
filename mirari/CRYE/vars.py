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
            {
                'title': 'MESA DE CONTROL',
                'icon': 'flaticon-time-1',
                'text': 'PROXIMAMENTE',
                'subtext': '',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': 'INT' + '.Handbook',
                #'href': 'CRYE:SiebelUnblock__SiebelUnblock__TemplateView',
            },
            {
                'title': 'QUIEN ES QUIEN',
                'icon': 'flaticon-time-1',
                'text': 'PROXIMAMENTE',
                'subtext': '',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': 'INT' + '.Handbook',
                #'href': 'CRYE:SiebelUnblock__SiebelUnblock__TemplateView',
            },
            {
                'title': 'INCIDENCIA SISTEMAS',
                'icon': 'flaticon-time-1',
                'text': 'PROXIMAMENTE',
                'subtext': '',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': 'INT' + '.Handbook',
                #'href': 'CRYE:SiebelUnblock__SiebelUnblock__TemplateView',
            },
            {
                'title': 'REQUISICIÓN DE MATERIAL',
                'icon': 'flaticon-time-1',
                'text': 'PROXIMAMENTE',
                'subtext': '',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': 'INT' + '.Handbook',
                #'href': 'CRYE:SiebelUnblock__SiebelUnblock__TemplateView',
            },
        ]
    },
    'CRYE': {
        'title': 'COBRANZA',
        'modules': [
            {
                'title': 'CREDITO',
                'icon': 'flaticon-graphic',
                'text': 'Cartera de crédito',
                'subtext': 'Cobranza de la cartera de crédito',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.SiebelUnblock',
                'url': 'Generic__ListView',
            },
            #{
                #'title': 'MESA DE CONTROL',
                #'icon': 'flaticon-time-1',
                #'text': 'PROXIMAMENTE',
                #'subtext': '',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': 'INT' + '.Handbook',
                ##'href': 'CRYE:SiebelUnblock__SiebelUnblock__TemplateView',
            #},
        ]
    },
    'CRYE': {
        'title': 'TASAS',
        'modules': [
            {
                'title': 'TASAS',
                'icon': 'flaticon-presentation-1',
                'text': 'Consulta las tasas de interés',
                'subtext': 'Tasas de Interés en el Mercado de Dinero',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.TasasInteres',
                'html': 'Tasas_DashboardView.html',
            },
        ]
    },
}