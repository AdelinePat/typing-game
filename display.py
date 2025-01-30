import pygame
import time
import random, secrets
import string
from class_folder.Screen import Screen
from class_folder.Fruits import Fruits
from class_folder.Fruit_slices import Fruit_slices
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

    fruit = Fruits(random_x_position, (screen.height+random_size), random_size, image, random_rotation, random_letter, color,screen.height, screen.screen, fruits_list[index])
    # fruit = Fruits(random_x_position, screen.height//2, random_size, image, random_rotation, "A", color, screen.height, screen.screen)
    return fruit
 
screen = Screen(1080, 720)
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []
fruits_slices = []

run = True
is_create_fruit = True  

actual_background = screen.background()
screen.screen.blit(actual_background, (0, 0))


counter = 0
while run:

    timer = clock.tick(10)
    counter += 1    
    # timer = time.time()
    screen.screen.blit(actual_background, (0, 0))
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
                            fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen)
                            fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen)
                            fruits_slices.append(fruit_slices_1)
                            fruits_slices.append(fruit_slices_2)
                            fruits.pop(index)
                            # fruit_slices.draw()
                            # fruit_slices.fall(fruit_slices.image_1)
                            # fruit_slices.fall(fruit_slices.image_2)
    
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
    # print(timer)
    if is_create_fruit and counter % 30 == 0: #secrets.randbelow(100) > 50:
        # print(f"dans le if : {timer}")
        fruit = create_fruits()
        # last_fruit_spawn = timer
        fruits.append(fruit)
        
        if len(fruits) > 20:
            fruits.pop(0)

    
    
    
    for fruit in fruits:
        if len(fruits) > 0:
            fruit.draw()
            # if timer % 3 == 0:
            mode = 0
            fruit.fall(timer, mode)
    for fruit_slices in fruits_slices:
        if len(fruits_slices) > 0:

    # if fruit_slices:
            fruit_slices.draw()
            # fruit_slices_2.draw()
            fruit_slices.fall()
            # fruit_slices_2.fall()
    
    pygame.display.update() 
    