import pygame, random, secrets, string
from class_folder.Fruits import Fruits
from class_folder.Fruit_slices import Fruit_slices
from game.menues.game_functions import clock_tick
from __settings__ import FRUIT_DICT, BACKGROUND_IMAGE, PROPS_DICT
from game.scores.Player_attributes import Player_attributes
from game.scores.Scores import Scores
from display.display_menu_assets import display_hearts, display_score_in_game

def run_new_game(screen, clock,fps, game_mode, player):
    current_player = Player_attributes(player)
    game_scores = Scores()
    game_mode = game_mode
    if game_mode == 'normal_mode' or game_mode == 'easy_mode':
        life = 5
        spawn_delay = 40
        devel = 9
        letters = []
        for letter in range(0,7):
            letters.append(random.choice(string.ascii_uppercase))
    elif game_mode == 'nightmare_mode':
        life = 50
        spawn_delay = 30
        devel = 5
        letters = string.ascii_uppercase
    frame = 0
    fruits = []
    props = []
    current_background = screen.background(BACKGROUND_IMAGE, "Fruit Slicer")
    frozen_effect = screen.frozen()
    fruits_slices = []
    while True:
        if not current_player.alive(life):
            game_scores.update_scores(current_player)
            return "menu_game_over"
        screen.screen.blit(current_background, (0, 0))
    
        fruits_slices_on_screen = fruits_slices.copy()
        for fruit_slice in fruits_slices_on_screen:
            fruit_slice.draw()
            if not current_player.frozen():
                if fruit_slice.fall(frame) == 'dropped':
                    index = fruits_slices.index(fruit_slice)
                    fruits_slices.pop(index)
        
        fruits_on_screen = fruits.copy()
        for fruit in fruits_on_screen:
            fruit.draw()
            if not current_player.frozen():
                if fruit.fall(frame, devel) == 'dropped':
                    index = fruits.index(fruit)
                    fruits.pop(index)
                    current_player.life_down(life, 'dropped', frame)

        props_on_screen = props.copy()
        for prop in props_on_screen:
            prop.draw()
            if not current_player.frozen():
                if prop.fall(frame, devel) == 'dropped':
                    index = props.index(prop)
                    props.pop(index)

        display_score_in_game(current_player.score)
        display_hearts(life, current_player.strike)
        if current_player.frozen():
            screen.screen.blit(frozen_effect, (0, 0))
            current_player.frozen_up()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "game_off"
            if event.type == pygame.KEYDOWN:
                if not current_player.frozen():
                    try:
                        current_player.played_key = str(event.unicode).upper()
                        for fruit in fruits:
                            if fruit.letter == current_player.played_key:
                                index = fruits.index(fruit)
                                fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen, screen, 'half_1')
                                fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen, screen, 'half_2')
                                fruits_slices.append(fruit_slices_1)
                                fruits_slices.append(fruit_slices_2)
                                fruits.pop(index)
                                current_player.add_score()
                    except Exception:
                        pass
        if frame % 900 == 0:
            if spawn_delay <= 2:
                pass
            else:
                spawn_delay -=1
                devel -= 0.25
        if frame % spawn_delay == 0:
            if not current_player.frozen() and current_player.alive(life):
                if secrets.randbelow(100) > spawn_delay:
                    fruit = create_fruits(screen, letters, devel)
                    fruits.append(fruit)
                if secrets.randbelow(100) > spawn_delay: # + 40:
                    prop = create_props(screen, devel)
                    props.append(prop)
                
        frame = clock_tick(clock, fps, frame)

def create_fruits(screen, letters, devel):
    fruits_list= list(FRUIT_DICT.keys())
    index = secrets.randbelow(len(fruits_list))
    
    image = FRUIT_DICT[fruits_list[index]]["image"]
    color = FRUIT_DICT[fruits_list[index]]["color"]

    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-60, 60)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))

    random_letter = random.choice(letters).upper()

    fruit = Fruits(random_x_position, (screen.height+1), random_size, image, random_rotation, devel, random_letter, color, screen.height, screen.screen, screen.width, fruits_list[index])

    return fruit

def create_props(screen, devel):
    props_list= list(PROPS_DICT.keys())
    index = secrets.randbelow(len(props_list))
    
    image = PROPS_DICT[props_list[index]]["image"]
    color = PROPS_DICT[props_list[index]]["color"]

    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-60, 60)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))

    string.ascii_letters
    random_letter = random.choice(string.ascii_letters).upper()

    prop = Fruits(random_x_position, (screen.height+1), random_size, image, random_rotation, devel, random_letter, color, screen.height, screen.screen, screen.width, props_list[index])

    return prop