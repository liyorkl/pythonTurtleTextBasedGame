zonemap = {
    'a1': {
        'ZONENAME': "City Area",
        'DESCRIPTION': "The upper left most City Area",
        'EXAMINATION': "citya1",
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b1',
        'LEFT': '',
        'RIGHT': 'a2'
    },
    'a2': {
        'ZONENAME': "Bush",
        'DESCRIPTION': "A place with a lot of bushes surrounding the area",
        'EXAMINATION': "busha2",
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b2',
        'LEFT': 'a1',
        'RIGHT': 'a3'
    },
    'a3': {
        'ZONENAME': "Stream",
        'DESCRIPTION': "The main Stream connected to the City Area",
        'EXAMINATION': "streama3",
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b3',
        'LEFT': 'a2',
        'RIGHT': 'a4'
    },
    'a4': {
        'ZONENAME': "City Area",
        'DESCRIPTION': "Your starting point",
        'EXAMINATION': "citya4",
        'SOLVED': False,
        'UP': "",
        'DOWN': 'b4',
        'LEFT': 'a3',
        'RIGHT': ''
    },
    'b1': {
        'ZONENAME': "Bush",
        'DESCRIPTION': "Very damp and very dark",
        'EXAMINATION': "bushb1",
        'SOLVED': False,
        'UP': "a1",
        'DOWN': 'c1',
        'LEFT': '',
        'RIGHT': 'b2'
    },
    'b2': {
        'ZONENAME': "Stream",
        'DESCRIPTION': "The centre of the stream",
        'EXAMINATION': "streamb2",
        'SOLVED': False,
        'UP': "a2",
        'DOWN': 'c2',
        'LEFT': 'b1',
        'RIGHT': 'b3'
    },
    'b3': {
        'ZONENAME': "Stream",
        'DESCRIPTION': "A large area with quick flowing water",
        'EXAMINATION': "streamb3",
        'SOLVED': False,
        'UP': "a3",
        'DOWN': 'c3',
        'LEFT': 'b2',
        'RIGHT': 'b4'
    },
    'b4': {
        'ZONENAME': "City Area",
        'DESCRIPTION': "A very urban place with lots of cars passing by",
        'EXAMINATION': "cityb4",
        'SOLVED': False,
        'UP': "a4",
        'DOWN': 'c4',
        'LEFT': 'b3',
        'RIGHT': ''
    },
    'c1': {
        'ZONENAME': "Stream",
        'DESCRIPTION': "An area with eels due to it's slow flowing water",
        'EXAMINATION': "streamc1",
        'SOLVED': False,
        'UP': "b1",
        'DOWN': 'd1',
        'LEFT': '',
        'RIGHT': 'c2'
    },
    'c2': {
        'ZONENAME': "Stream",
        'DESCRIPTION': "A small area with lots of overflowing water",
        'EXAMINATION': "streamc2",
        'SOLVED': False,
        'UP': "b2",
        'DOWN': 'd2',
        'LEFT': 'c1',
        'RIGHT': 'c3'
    },
    'c3': {
        'ZONENAME': "Bush",
        'DESCRIPTION': "Much of the area is covered by a layer of water",
        'EXAMINATION': "bushc3",
        'SOLVED': False,
        'UP': "b3",
        'DOWN': 'd3',
        'LEFT': 'c2',
        'RIGHT': 'c4'
    },
    'c4': {
        'ZONENAME': "City Area",
        'DESCRIPTION': "An area with lots of litter thrown around",
        'EXAMINATION': "cityc4",
        'SOLVED': False,
        'UP': "b4",
        'DOWN': 'd4',
        'LEFT': 'c3',
        'RIGHT': ''
    },
    'd1': {
        'ZONENAME': "City Area",
        'DESCRIPTION': "Very quiet, not a very active place",
        'EXAMINATION': "cityd1",
        'SOLVED': False,
        'UP': "c1",
        'DOWN': '',
        'LEFT': '',
        'RIGHT': 'd2'
    },
    'd2': {
        'ZONENAME': "Bush",
        'DESCRIPTION': "An area with damp long grass",
        'EXAMINATION': "bushd2",
        'SOLVED': False,
        'UP': "c2",
        'DOWN': '',
        'LEFT': 'd1',
        'RIGHT': 'd3'
    },
    'd3': {
        'ZONENAME': "Bush",
        'DESCRIPTION': "Much green",
        'EXAMINATION': "bushd3",
        'SOLVED': False,
        'UP': "c3",
        'DOWN': '',
        'LEFT': 'd2',
        'RIGHT': 'd4'
    },
    'd4': {
        'ZONENAME': "Shop",
        'DESCRIPTION': "Very rich",
        'EXAMINATION': "shop",
        'SOLVED': True,
        'UP': "c4",
        'DOWN': '',
        'LEFT': 'd3',
        'RIGHT': ''
    }
}
