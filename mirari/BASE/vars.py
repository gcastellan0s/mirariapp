APP = 'BASE'

MENU = {
    'BASE': {
        'title': 'BASE',
        'modules': [
            {
                'title': 'BASE',
                'icon': 'flaticon-lifebuoy',
                'text': 'Base text',
                'subtext': 'Base subtext subtext subtext',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.BASE',
                'href': 'BASE:FunctionName__TypeView',
            },
        ]
    }
}