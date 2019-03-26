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
                'title': 'COBRANZA',
                'icon': 'flaticon-coins',
                'text': 'Clientes de cartera',
                'subtext': 'Lista de cartera',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.WalletCredit',
                'url': 'Generic__ListView',
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
CLASIFICACION_CONTABLE = (
	('GARANTIZADOS CON LOS BIENES QUE DAN ORIG', 'GARANTIZADOS CON LOS BIENES QUE DAN ORIG'),
	('CRÉDITO SIMPLE', 'CRÉDITO SIMPLE'),
    ('GARANTIZADOS CON INMUEBLES URBANOS', 'GARANTIZADOS CON INMUEBLES URBANOS'),
    ('QUIROGRAFARIOS', 'QUIROGRAFARIOS'),
)
WALLETCREDIT_TIPO = {
    ('CREDITO', 'CREDITO'),
	('ARRENDAMIENTO', 'ARRENDAMIENTO'),
}