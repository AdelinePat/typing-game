import pygame
import random, secrets
import string
from Screen import Screen
from Fruits import Fruits
from __settings__ import FPS_EASY, FPS_HARD, FRUIT_DICT

def create_fruits():
    # fruits_list = ["watermelon", "orange", "coconut", "melon", "limon", "kiwi", "apple", "pineapple"]

    fruits_list= list(FRUIT_DICT.keys())
    # fruits_list = ["limon", "strawberry", "apple"]
    index = secrets.randbelow(len(fruits_list))
    image = FRUIT_DICT[fruits_list[index]]["image"]
    color = FRUIT_DICT[fruits_list[index]]["color"]



    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-15, 15)
    # random_x_position = secrets.randbelow(screen.width - random_size*2) + random_size/
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))
    string.ascii_letters
    random_letter = random.choice(string.ascii_letters).upper()

    fruit = Fruits(random_x_position, (screen.height+random_size), random_size, image, random_rotation, random_letter, color, screen.height, screen.screen)

    # match fruits_list[index]:
    #     case "watermelon":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, WATERMELON_IMAGE, random_rotation, random_letter, screen.height, screen.screen)
    #     case "orange":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, ORANGE_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
    #     case "coconut":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, COCONUT_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
    #     case "melon":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, MELON_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
    #     case "limon":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, LIMON_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
    #     case "kiwi":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, KIWI_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
    #     case "apple":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, APPLE_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
    #     case "pineapple":
    #         fruit = Fruits(random_x_position, (screen.height+random_size), random_size, PINEAPPLE_IMAGE,random_rotation, random_letter, screen.height, screen.screen)
        # case "strawberry":
        #     fruit = Fruits(random_x_position, -(random_height), random_height, WATERMELON_IMAGE, "S")
        
    return fruit
 
screen = Screen(1080, 720)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []

fruits_surface = pygame.Surface(screen.size, pygame.SRCALPHA)
global_rotation = 1

run = True
is_create_fruit = True  

actual_background = screen.background()
screen.screen.blit(actual_background, (0, 0))

while run:

    clock.tick(60)
    # pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
    keys = pygame.key.get_pressed()

    if is_create_fruit and secrets.randbelow(100) > 50:
        fruit = create_fruits()
        fruits.append(fruit)
        
        if len(fruits) > 20:
            fruits.pop(0)

    screen.screen.blit(actual_background, (0, 0))

    for fruit in fruits:
        fruit.draw()    
        fruit.fall()
    
    pygame.display.update() 
    