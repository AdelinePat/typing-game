import pygame
import random, secrets
import string
from class_folder.Screen import Screen
from class_folder.Fruits import Fruits
from __settings__ import FPS_EASY, FPS_HARD, FRUIT_DICT

def create_fruits():
    fruits_list= list(FRUIT_DICT.keys())
    index = secrets.randbelow(len(fruits_list))
    image = FRUIT_DICT[fruits_list[index]]["image"]
    color = FRUIT_DICT[fruits_list[index]]["color"]

    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-25, 25)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))

    string.ascii_letters
    random_letter = random.choice(string.ascii_letters).upper()

    fruit = Fruits(random_x_position, (screen.height+random_size), random_size, image, random_rotation, random_letter, color, screen.height, screen.screen)
    return fruit
 
screen = Screen(1080, 720)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []

run = True
is_create_fruit = True  

actual_background = screen.background()
screen.screen.blit(actual_background, (0, 0))

while run:

    clock.tick(40)
    
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
    