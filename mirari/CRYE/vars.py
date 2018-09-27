APP = 'CRYE'

MENU = {
    'CRYE': {
        'title': 'CREDIPyME',
        'modules': [
            {
                'title': 'NOTIFICACIONES PLD',
                'icon': 'flaticon-speech-bubble-1',
                'text': 'Avisos de PLD',
                'subtext': 'Es importante leer todos los avisos de PLD.',
                'apps': [APP, ],
                'permission': 'Can_View',
                'model': APP + '.PLDNotifications',
                'url': 'Generic__ListView',
            },
        ]
    }
}