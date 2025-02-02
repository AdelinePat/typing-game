import pygame
from display.display_models.Screen import Screen
pygame.display.init()

SCREEN = Screen(1080, 720)

MAIN_FONT = "assets/fonts/Coolvetica Rg.otf"
STYLE_FONT = "assets/fonts/slice n dice.ttf"
TEXT_COLOR = (218, 133, 51)
TEXT_COLOR_LIGHT = (245, 189, 122)
TEXT_COLOR_DARK = (96, 57, 2)

BUTTON_IMAGE = pygame.image.load("assets/plank/plank1.1.png")

def flip_button_image(img, flip_horizontal, flip_vertical):
    img_copy = img.copy()
    img_flip = pygame.transform.flip(img_copy, flip_horizontal, flip_vertical)
    return img_flip

BUTTON_IMAGE2 = flip_button_image(BUTTON_IMAGE, True, False)
BUTTON_IMAGE3 = flip_button_image(BUTTON_IMAGE, False, True)
BUTTON_IMAGE4 = flip_button_image(BUTTON_IMAGE, True, True)

PLANK_SCORE = "assets/plank/plank2.png"
PLANK_ARROW_RIGHT = pygame.image.load("assets/plank/arrow_right_plank.png")

PLANK_ARROW_LEFT = flip_button_image(PLANK_ARROW_RIGHT, True, False)

ICECUBE_IMAGE = "assets/bonus_malus/ice_cube1.png"
ICE_CUBE1 = pygame.image.load("assets/bonus_malus/ice_cube1.png")
ICE_CUBE2 = pygame.image.load("assets/bonus_malus/ice_cube2.png")
ICE_CUBE3 = pygame.image.load("assets/bonus_malus/ice_cube3.png")
ICE_CUBE4 = pygame.image.load("assets/bonus_malus/ice_cube4.png")
HEART = pygame.image.load("assets/bonus_malus/heart_v3.png")
BOMB_IMAGE = pygame.image.load("assets/bonus_malus/bomb.png")
BOMB = pygame.image.load("assets/bonus_malus/bomb.png")
EFFECT1 = pygame.image.load("assets/bonus_malus/explosion1.png")
EFFECT2 = pygame.image.load("assets/bonus_malus/explosion2.png")
EFFECT3 = pygame.image.load("assets/bonus_malus/explosion3.png")

ICECUBE_COLOR = (255,255,255)
BOMB_COLOR = (0,0,0)

FPS = 60
FPS_EASY = 20
FPS_HARD = 40

APPLE_IMAGE = pygame.image.load("assets/fruits/apple_full.png")
APPLE_SLICE = pygame.image.load("assets/fruits/apple_slice.png")

COCONUT_IMAGE = pygame.image.load("assets/fruits/coconut_full.png")
COCONUT_SLICE = pygame.image.load("assets/fruits/coconut_slice.png")

KIWI_IMAGE = pygame.image.load("assets/fruits/kiwi_full.png")
KIWI_SLICE = pygame.image.load("assets/fruits/kiwi_slice.png")

LIMON_IMAGE = pygame.image.load("assets/fruits/limon_full.png")
LIMON_SLICE = pygame.image.load("assets/fruits/limon_slice.png")

MELON_IMAGE = pygame.image.load("assets/fruits/melon_full.png")
MELON_SLICE = pygame.image.load("assets/fruits/melon_slice.png")

ORANGE_IMAGE = pygame.image.load("assets/fruits/orange_full.png")
ORANGE_SLICE = pygame.image.load("assets/fruits/orange_slice.png")

PEAR_IMAGE = pygame.image.load("assets/fruits/pear_full.png")
PEAR_SLICE = pygame.image.load("assets/fruits/pear_slice.png")

PINEAPPLE_IMAGE = pygame.image.load("assets/fruits/pineapple_full_2.png")
PINEAPPLE_SLICE = pygame.image.load("assets/fruits/pineapple_slice.png")

WATERMELON_IMAGE = pygame.image.load("assets/fruits/watermelon_full.png")
WATERMELON_SLICE = pygame.image.load("assets/fruits/watermelon_slice.png")

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


PROPS_DICT = {
    "icecube1" : {
        "image": ICE_CUBE1,
        "color": (0,0,0)
        },
    "icecube2": {
        "image" : ICE_CUBE2,
        "color": (0,0,0)
        },
    "icecube3" : {
        "image" : ICE_CUBE3,
        "color": (0,0,0)
        },
    "icecube4": {
        "image" : ICE_CUBE4,
        "color": (0,0,0)},
    "bomb": {
        "image": BOMB,
        "color": (0,0,0)
        }
    }

SCORE_PATH = "game/scores/scores.json"