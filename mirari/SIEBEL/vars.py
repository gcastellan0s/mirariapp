APP = 'SIEBEL'

MENU = {
    'SIEBEL': {
        'title': 'SIEBEL',
        'modules': [
            {
                'title': 'ACTOR DE CREDITO',
                'icon': 'flaticon-avatar',
                'text': 'Da de alta actores para un crédito',
                'subtext': 'Administra a los actores que interactuan en los créditos',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Actor',
                'url': 'Generic__ListView',
            },
            {
                'title': 'PERSONAS',
                'icon': 'flaticon-network',
                'text': 'Da de alta tu base de datos de clientes',
                'subtext': 'Administra todos tus clientes en el sistema SIEBEL',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.Person',
                'url': 'Generic__ListView',
            },
            {
                'title': 'TIPOS DE CRÉDITO',
                'icon': 'flaticon-coins',
                'text': 'Lista de tipos de crédito',
                'subtext': 'Administra los tipso de crédito que se corren en el sistema SIEBEL',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.CreditType',
                'url': 'Generic__ListView',
            },
            {
                'title': 'CRÉDITO',
                'icon': 'flaticon-piggy-bank',
                'text': 'Creditos de SIEBEL',
                'subtext': 'Listado de todos los créditos en SIEBEL',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.SIEBELCredit',
                'url': 'Generic__ListView',
            },
        ]
    }
}

CREDIT_STAGE = (
	('Prospecto', 'Prospecto'),
)