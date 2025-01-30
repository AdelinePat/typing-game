import pygame
import random, secrets, string
from game.class_folder.Fruits import Fruits
from game.__settings__ import FPS, FRUIT_DICT, ICECUBE_IMAGE, BOMB_IMAGE, ICECUBE_COLOR, BOMB_COLOR
from game.scores.manage_scores import combo_count, update_scores
from game.game_functions import clock_tick
 
def create_fruits(screen, game_mode, type):
    fruits_list= list(FRUIT_DICT.keys())
    index = secrets.randbelow(len(fruits_list))
    if type == 'fruit':
        image = FRUIT_DICT[fruits_list[index]]["image"]
        color = FRUIT_DICT[fruits_list[index]]["color"]
    elif type == 'icecube':
        image = ICECUBE_IMAGE
        color = ICECUBE_COLOR
    elif type == 'bomb':
        image = BOMB_IMAGE
        color = BOMB_COLOR

    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-25, 25)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))
    letters_normal = ['A','S','P','V','C','T','K','W','R']
    letters_nightmare = string.ascii_uppercase
    if game_mode == 'normal':
        random_letter = random.choice(letters_normal)
    elif game_mode == 'nightmare':
        random_letter = random.choice(letters_nightmare)

    fruit = Fruits(random_x_position, (screen.height+1), random_size, image, random_rotation, random_letter, color, screen, type)
    return fruit

def in_game(screen, clock, game_mode, player):
    invicibility = 0
    score = 0
    frame = 0
    spawn_delay = 40
    fruits = []
    slashed = 0
    slashed_fruits = []
    life = 3
    combo = 0
    last_key = ''
    frozen=0
    is_frozen = False
    current_background = screen.background()
    screen.screen.blit(current_background, (0, 0))
    frozen_effect = screen.frozen()
    while True:
        if frozen == 0:
            is_frozen = False
            screen.screen.blit(current_background, (0, 0))
            for fruit in fruits:
                fruit.draw()
                if fruit.fall() == 'dropped':
                    index = fruits.index(fruit)
                    fruits.pop(index)
                    if frame - invicibility > 60 and fruit.type == 'fruit':
                        life -= 1
                        invicibility = frame
        elif frozen > 0:
            screen.screen.blit(frozen_effect, (0, 0))
            is_frozen = True
            frozen -=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "game_off"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and life <=0:
                    update_scores(score, slashed, player)
                    return 'main_menu'
                if is_frozen == False:
                    try:
                        played_key = str(event.unicode).upper()
                        for fruit in fruits:
                            if fruit.letter == played_key:
                                if fruit.type == 'fruit':
                                    slashed+=1
                                    slashed_fruits.append(fruit)
                                    index = fruits.index(fruit)
                                    fruits.pop(index)
                                    score, combo = combo_count(played_key, last_key, score, combo)
                                    last_key = played_key
                                elif fruit.type == 'icecube':
                                    frozen = 180
                                    index = fruits.index(fruit)
                                    fruits.pop(index)
                                elif fruit.type == 'bomb':
                                    life = 0
                                    index = fruits.index(fruit)
                                    fruits.pop(index)
                                break                
                        print(score)
                    except Exception:
                        pass
        if frame % 1300 == 0:
            if spawn_delay <= 2:
                pass
            else: spawn_delay -=3
        if frame % spawn_delay == 0:
            if is_frozen == False and life > 0:
                if secrets.randbelow(100) > spawn_delay:
                    fruit = create_fruits(screen, game_mode,'fruit')
                    fruits.append(fruit)
                if secrets.randbelow(100) > spawn_delay + 50:
                    fruit = create_fruits(screen,game_mode, 'icecube')
                    fruits.append(fruit)
                if secrets.randbelow(100) > spawn_delay + 70:
                    fruit = create_fruits(screen,game_mode, 'bomb')
                    fruits.append(fruit)
                
        frame = clock_tick(clock,FPS, frame)