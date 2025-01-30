import pygame
import random, secrets, string
from game.class_folder.Fruits import Fruits
from game.__settings__ import FPS, FRUIT_DICT, ICECUBE_IMAGE, BOMB_IMAGE, ICECUBE_COLOR, BOMB_COLOR
from game.scores.Player_attributes import Player_attributes
from game.scores.Scores import Scores
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
    current_player = Player_attributes(player)
    game_scores = Scores()
    spawn_delay = 40
    frame = 0
    fruits = []
    slashed_fruits = []
    current_background = screen.background()
    screen.screen.blit(current_background, (0, 0))
    frozen_effect = screen.frozen()
    while True:
        screen.screen.blit(current_background, (0, 0))
        fruits_on_screen = fruits.copy()
        for fruit in fruits_on_screen:
            if not current_player.frozen():
                if fruit.fall() == 'dropped':
                    index = fruits.index(fruit)
                    fruits.pop(index)
                    current_player.life_down('dropped', frame, fruit)
            fruit.draw()
        if current_player.frozen():
            screen.screen.blit(frozen_effect, (0, 0))
            current_player.frozen_up()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "game_off"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not current_player.alive():
                    game_scores.update_scores(current_player)
                    return 'main_menu'
                if not current_player.frozen():
                    try:
                        current_player.played_key = str(event.unicode).upper()
                        for fruit in fruits:
                            if fruit.letter == current_player.played_key:
                                if fruit.type == 'fruit':
                                    slashed_fruits.append(fruit)
                                    index = fruits.index(fruit)
                                    fruits.pop(index)
                                    current_player.add_score()
                                elif fruit.type == 'icecube':
                                    index = fruits.index(fruit)
                                    fruits.pop(index)
                                    current_player.frozen_up()
                                elif fruit.type == 'bomb':
                                    index = fruits.index(fruit)
                                    fruits.pop(index)
                                    current_player.life_down('bomb')
                                break                
                        print(current_player.score)
                    except Exception:
                        pass
        if frame % 1300 == 0:
            if spawn_delay <= 2:
                pass
            else: spawn_delay -=2
        if frame % spawn_delay == 0:
            if not current_player.frozen() and current_player.alive():
                if secrets.randbelow(100) > spawn_delay:
                    fruit = create_fruits(screen, game_mode,'fruit')
                    fruits.append(fruit)
                if secrets.randbelow(100) > spawn_delay + 50:
                    fruit = create_fruits(screen,game_mode, 'icecube')
                    fruits.append(fruit)
                if secrets.randbelow(100) > spawn_delay + 60:
                    fruit = create_fruits(screen,game_mode, 'bomb')
                    fruits.append(fruit)
                
        frame = clock_tick(clock,FPS, frame)