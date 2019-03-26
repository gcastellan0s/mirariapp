APP = 'SIEBEL'

MENU = {
    #'SIEBEL': {
        #'title': 'SIEBEL',
        #'modules': [
            #{
                #'title': 'ACTOR DE CREDITO',
                #'icon': 'flaticon-avatar',
                #'text': 'Da de alta actores para un crédito',
                #'subtext': 'Administra a los actores que interactuan en los créditos',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.Actor',
                #'url': 'Generic__ListView',
            #},
            #{
                #'title': 'PERSONAS',
                #'icon': 'flaticon-network',
                #'text': 'Da de alta tu base de datos de clientes',
                #'subtext': 'Administra todos tus clientes en el sistema SIEBEL',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.Person',
                #'url': 'Generic__ListView',
            #},
            #{
                #'title': 'TIPOS DE CRÉDITO',
                #'icon': 'flaticon-coins',
                #'text': 'Lista de tipos de crédito',
                #'subtext': 'Administra los tipso de crédito que se corren en el sistema SIEBEL',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.CreditType',
                #'url': 'Generic__ListView',
            #},
            #{
                #'title': 'CRÉDITO',
                #'icon': 'flaticon-piggy-bank',
                #'text': 'Creditos de SIEBEL',
                #'subtext': 'Listado de todos los créditos en SIEBEL',
                #'apps': [APP, ],
                #'permission': 'Can_View',
                #'model': APP + '.SBCredit',
                #'url': 'Generic__ListView',
            #},
        #]
    #}
}

CREDIT_STAGE = (
	('Prospecto', 'Prospecto'),
)

PERSON_TYPE = (
	('Persona física', 'Persona física'),
    ('Persona física con actividad empresarial', 'Persona física con actividad empresarial'),
)

COMPANY_TYPE = (
	('Sector público de pasajeros', 'Sector público de pasajeros'),
    ('Turismo', 'Turismo'),
    ('Transporte de personal', 'Transporte de personal'),
    ('Servicio Público Federal', 'Servicio Público Federal'),
    ('Agropecuario', 'Agropecuario'),
    ('Materiales y residuos peligrosos', 'Materiales y residuos peligrosos'),
    ('Forestal', 'Forestal'),
    ('Pesquero', 'Pesquero'),
    ('Agricola', 'Agricola'),
)

COMPANY_ACTIVITY = (
	('Agricultura', 'Agricultura'),
    ('Cultivo de alpiste', 'Cultivo de alpiste'),
    ('Construccion de inmuebles', 'Construccion de inmuebles'),
    ('Cultivo de arroz', 'Cultivo de arroz'),
    ('Cultivo de avena', 'Cultivo de avena'),
    ('Cultivo de cebada', 'Cultivo de cebada'),
    ('Fabricación de guantes', 'Fabricación de guantes'),
    ('Distribucion de otros productos', 'Distribucion de otros productos'),
    ('Agencia aduanal', 'Agencia aduanal'),
    ('Cultivo de aguacate', 'Cultivo de aguacate'),
    ('Fabricación otros art de metal', 'Fabricación otros art de metal'),
    ('Construcción no residencial', 'Construcción no residencial'),
    ('Fabricacion de uniformes', 'Fabricacion de uniformes'),
)