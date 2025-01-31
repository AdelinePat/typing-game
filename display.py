import pygame
import time
import random, secrets
import string
from display.display_models.Screen import Screen
from game.element_models.Fruits import Fruits
from game.element_models.Fruit_slices import Fruit_slices
from __settings__ import FPS_EASY, FPS_HARD, FRUIT_DICT
# from display.display_menu import display_hearts, display_score_in_game

KEYDOWN = pygame.KEYDOWN
screen = Screen(1080, 720)

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

    fruit = Fruits(random_x_position, (screen.height+random_size), random_size, image, random_rotation, random_letter, color, fruits_list[index])
    # fruit = Fruits(random_x_position, screen.height//2, random_size, image, random_rotation, "A", color, screen.height, screen.screen)
    return fruit
 

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []
fruits_slices = []

run = True
is_create_fruit = True  

actual_background = screen.background()
# screen.screen.blit(actual_background, (0, 0))


counter = 0
while run:

    timer = clock.tick(60)
    counter += 1    
    screen.screen.blit(actual_background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == KEYDOWN:
            letter = pygame.key.name(event.key)
            for fruit in fruits:
                if event.key == pygame.key.key_code(letter):
                    if len(fruits) > 0:
                        if fruit.letter.lower() == letter:
                            index = fruits.index(fruit)
                            fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name)
                            fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name)
                            fruits_slices.append(fruit_slices_1)
                            fruits_slices.append(fruit_slices_2)
                            fruits.pop(index)
 
    if is_create_fruit and counter % 30 == 0: 
        fruit = create_fruits()
        fruits.append(fruit)
        if len(fruits) > 20:
            fruits.pop(0)
    
    for fruit in fruits:
        if len(fruits) > 0:
            fruit.draw()
            mode = 0
            fruit.fall()

    for fruit_slices in fruits_slices:
        if len(fruits_slices) > 0:
            fruit_slices.draw()
            fruit_slices.fall()

    score = 123
    life = 9
    strike = 0
    display_hearts(life, strike)
    display_score_in_game(score)

    pygame.display.update() 
    