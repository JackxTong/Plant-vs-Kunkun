data = {
    0: { # bullet
        'PATH': 'pic/other/peabullet.png',
        'IMAGE_INDEX_MAX': 0,
        'IMAGE_INDEX_CD': 0.0,
        'POSITION_CD': 0.008,
        'SIZE': (30, 30),
        'SPEED': (4, 0),
        'PRICE': 0

    },

    "basketball": {
        'PATH': 'pic/other/bball.png',
        'IMAGE_INDEX_MAX': 0,
        'IMAGE_INDEX_CD': 0.0,
        'POSITION_CD': 0.008,
        'SIZE': (30, 30),
        'SPEED': (4, 0),
        'PRICE': 0

    },

    1: { # zombie
        'PATH': 'pic/zombies/Zombie_%d copy.png',
        'IMAGE_INDEX_MAX': 21,
        'IMAGE_INDEX_CD': 0.05,  # zombie frame rate
        'POSITION_CD': 0.05,  # zombie speed (small means fast)
        'SIZE': (150, 150),
        'SPEED': (-2.5, 0),
        'PRICE': 0
    },

    "kun": {
        'PATH': 'pic/cxks/CXK_%d.png',
        'IMAGE_INDEX_MAX': 17,
        'IMAGE_INDEX_CD': 0.05,
        'POSITION_CD': 0.05,
        'SIZE': (150, 150),
        'SPEED': (-2.5, 0),
        'PRICE': 0
    },

    2: { # sunlight
        'PATH': 'pic/other/sunlight/%d.png',
        'IMAGE_INDEX_MAX': 30,
        'IMAGE_INDEX_CD': 0.03,
        'POSITION_CD': 0.05,
        'SIZE': (80, 80),
        'SPEED': (0, 2),
        'PRICE': 5 # picks sunlight earns 5 gold
    },

    3: { # sunflower
        'PATH': 'pic/plants/SunFlower/SunFlower_%d.png',
        'IMAGE_INDEX_MAX': 17,
        'IMAGE_INDEX_CD': 0.03,
        'POSITION_CD': 0.05,
        'SIZE': (80, 80),
        'SPEED': (0, 0),
        'PRICE': 30 # costs 30 gold
    },
    4: { # peashooter
        'PATH': 'pic/plants/Peashooter/Peashooter_%d.png',
        'IMAGE_INDEX_MAX': 12,
        'IMAGE_INDEX_CD': 0.03,
        'POSITION_CD': 0.05,
        'SIZE': (80, 80),
        'SPEED': (0, 0),
        'PRICE': 20 # costs 20 gold
    }
}