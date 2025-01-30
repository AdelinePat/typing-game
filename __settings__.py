import pygame
pygame.display.init()

BACKGROUND_IMAGE = "assets/backgrounds/background_name_v2.jpg"
FROZEN_EFFECT = "assets/props/frozen_effect.webp"
MAIN_FONT = "assets/fonts/Coolvetica Rg.otf"
STYLE_FONT = "assets/fonts/slice n dice.ttf"
TEXT_COLOR = (218, 133, 51)

BUTTON_IMAGE = "assets/plank/plank1.png"
PLANK_SCORE = "assets/plank/plank2.png"

ICECUBE_IMAGE = "assets/bonus_malus/ice_cube1.png"
ICE_CUBE1 = "assets/bonus_malus/ice_cube1.png"
ICE_CUBE2 = "assets/bonus_malus/ice_cube2.png"
ICE_CUBE3 = "assets/bonus_malus/ice_cube3.png"
ICE_CUBE4 = "assets/bonus_malus/ice_cube4.png"
HEART = "assets/bonus_malus/heart_v3.png"
BOMB_IMAGE = "assets/bonus_malus/bomb.png"
BOMB = "assets/bonus_malus/bomb.png"
EFFECT1 = "assets/bonus_malus/explosion1.png"
EFFECT2 = "assets/bonus_malus/explosion2.png"
EFFECT3 = "assets/bonus_malus/explosion3.png"

ICECUBE_COLOR = (255,255,255)
BOMB_COLOR = (0,0,0)

FPS = 60
FPS_EASY = 20
FPS_HARD = 40

APPLE_IMAGE = "assets/fruits/apple_full.png"
APPLE_SLICE = "assets/fruits/apple_slice.png"

COCONUT_IMAGE = "assets/fruits/coconut_full.png"
COCONUT_SLICE = "assets/fruits/coconut_slice.png"

KIWI_IMAGE = "assets/fruits/kiwi_full.png"
KIWI_SLICE = "assets/fruits/kiwi_slice.png"

LIMON_IMAGE = "assets/fruits/limon_full.png"
LIMON_SLICE = "assets/fruits/limon_slice.png"

MELON_IMAGE = "assets/fruits/melon_full.png"
MELON_SLICE = "assets/fruits/melon_slice.png"

ORANGE_IMAGE = "assets/fruits/orange_full.png"
ORANGE_SLICE = "assets/fruits/orange_slice.png"

PEAR_IMAGE = "assets/fruits/pear_full.png"
PEAR_SLICE = "assets/fruits/pear_slice.png"

PINEAPPLE_IMAGE = "assets/fruits/pineapple_full_2.png"
PINEAPPLE_SLICE = "assets/fruits/pineapple_slice.png"

WATERMELON_IMAGE = "assets/fruits/watermelon_full.png"
WATERMELON_SLICE = "assets/fruits/watermelon_slice.png"

ASSETS_DICT = {
    "plank1" : BUTTON_IMAGE,
    "plank2": PLANK_SCORE,
    "heart" :  HEART,
    "ice_cube": {
        "1": ICE_CUBE1,
        "2": ICE_CUBE2,
        "3": ICE_CUBE3,
        "4": ICE_CUBE4
    },
    "bomb" : BOMB,
    "effets" : {
        "1": EFFECT1,
        "2": EFFECT2,
        "3": EFFECT3
    }
}

FRUIT_DICT = {
    "apple" : {"image" : APPLE_IMAGE,
               "slice" : APPLE_SLICE,
                "color": (183, 1, 1)
               },
    "coconut" : {"image" : COCONUT_IMAGE,
               "slice" : COCONUT_SLICE,
                "color" : (126,78,36),
                },
    "kiwi" : {"image" : KIWI_IMAGE,
               "slice" : KIWI_SLICE,
                # "color" : (151,100,61)
                "color": (130, 87, 53)
            },
    "limon" : {"image" : LIMON_IMAGE,
               "slice" : LIMON_SLICE,
                # "color" : (146,192,30)
                "color": (121, 159, 25)
            },
    "melon" :  {"image" : MELON_IMAGE,
               "slice" : MELON_SLICE,
                # "color" : (255,210,112),
                "color": (184, 125, 0)
            },
    "orange": {"image" : ORANGE_IMAGE,
               "slice" : ORANGE_SLICE,
                # "color" : (243,146,1),
                "color" : (183, 110, 0)
            },
    "pear": { "image" : PEAR_IMAGE,
               "slice" : PEAR_SLICE,
                # "color" : (254,156,3),
                "color": (172, 138, 45)
            },
    "pineapple" : { "image" : PINEAPPLE_IMAGE,
               "slice" : PINEAPPLE_SLICE,
                # "color" : (254,156,3),
                "color": (185, 113, 1)
            },
    "watermelon" : { "image" : WATERMELON_IMAGE,
               "slice" : WATERMELON_SLICE,
                "color" : (42,131,41)
            },
}

SCORE_PATH = "game/scores/scores.json"