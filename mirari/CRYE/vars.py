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
                'title': 'SIEBEL DESBLOQUEO 2',
                'icon': 'flaticon-lifebuoy',
                'text': 'Desbloquea trenes de crédito',
                'subtext': 'Desbloqueo de tren de credito del sistema SIEBEL',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.SiebelUnblock',
                'href': 'CRYE:TablaAmortizacion2__TemplateView',
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
    'TASAS': {
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
    'COBRANZA': {
        'title': 'COBRANZA',
        'modules': [
            {
                'title': 'CARTERA',
                'icon': 'flaticon-folder-1',
                'text': 'Clientes de cartera',
                'subtext': 'Lista de cartera',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.WalletCredit',
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
}

TIPO_TASA = (
	('FIJA', 'FIJA'),
	('TIIE', 'TIIE'),
)

FORMA_PAGO = (
	('INTERESES MENSUALES Y CAPITAL AL VENCIMIENTO', 'INTERESES MENSUALES Y CAPITAL AL VENCIMIENTO'),
	('INTERES Y CAPITAL MENSUALMENTE', 'INTERES Y CAPITAL MENSUALMENTE'),
    ('INTERESES Y CAPITAL AL VENCIMIENTO', 'INTERESES Y CAPITAL AL VENCIMIENTO'),
)

CLASIFICACION_CONTABLE = (
	('GARANTIZADOS CON LOS BIENES QUE DAN ORIG', 'GARANTIZADOS CON LOS BIENES QUE DAN ORIG'),
	('CRÉDITO SIMPLE', 'CRÉDITO SIMPLE'),
    ('GARANTIZADOS CON INMUEBLES URBANOS', 'GARANTIZADOS CON INMUEBLES URBANOS'),
    ('QUIROGRAFARIOS', 'QUIROGRAFARIOS'),
)