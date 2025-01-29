import pygame
import time
import random, secrets
import string
from class_folder.Screen import Screen
from class_folder.Fruits import Fruits
from __settings__ import FPS_EASY, FPS_HARD, FRUIT_DICT

KEYDOWN = pygame.KEYDOWN

def create_fruits():
    fruits_list= list(FRUIT_DICT.keys())
    index = secrets.randbelow(len(fruits_list))
    image = FRUIT_DICT[fruits_list[index]]["image"]
    color = FRUIT_DICT[fruits_list[index]]["color"]
    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-60, 60)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))

    string.ascii_letters
    random_letter = random.choice(string.ascii_letters).upper()


    fruit = Fruits(random_x_position, (screen.height+random_size), random_size, image, random_rotation, random_letter, color,screen.height, screen.screen)
    # fruit = Fruits(random_x_position, screen.height//2, random_size, image, random_rotation, "A", color, screen.height, screen.screen)
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

    timer = clock.tick(10)
    # timer = time.time()
    
    # TIMER_FRUIT = 1
    # last_fruit_spawn = time.time()
    
    # pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
        
        # if event == pygame.KEYDOWN:
        if event.type == KEYDOWN:
            letter = pygame.key.name(event.key)
            # print(f"letter init {letter}")
            for fruit in fruits:
                if event.key == pygame.key.key_code(letter):
                    if len(fruits) > 0:
                        if fruit.letter.lower() == letter:
                            index = fruits.index(fruit)
                            fruits.pop(index)
                            # print(f"letter pressed {letter}")
                        # print("blabla")

            # if event.key == pygame.K_b:
            #     if fruit.letter.lower() == "b":
            #         index = fruits.index(fruit)
            #         fruits.pop(index)
            #         print("blabla")
            # if event.key == pygame.K_c:
            #     if fruit.letter.lower() == "c":
            #         index = fruits.index(fruit)
            #         fruits.pop(index)
            #         print("blabla")
    # keys = pygame.key.get_pressed()
    
    # # if timer - last_fruit_spawn >= TIMER_FRUIT:
    if is_create_fruit and timer % 3 == 0: #secrets.randbelow(100) > 50:
        fruit = create_fruits()
        # last_fruit_spawn = timer
        fruits.append(fruit)
        
        if len(fruits) > 20:
            fruits.pop(0)
            
    screen.screen.blit(actual_background, (0, 0))
    
    
    for fruit in fruits:
        if len(fruits) > 0:
            fruit.draw()
            # if timer % 3 == 0:
            fruit.fall()
    
    pygame.display.update() 
    