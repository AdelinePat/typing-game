import pygame, random, secrets, string
from game.element_models.Fruits import Fruits
from game.element_models.Fruit_slices import Fruit_slices
from game.game_functions import clock_tick
from display.display_menu import game_over_screen
from __settings__ import FRUIT_DICT, PROPS_DICT
from display.display_models.__settings__ import BACKGROUND_IMAGE
from game.scores.Player_attributes import Player_attributes
from game.scores.Scores import Scores
from display.display_game_elements import display_hearts, display_score_in_game
from display.display_models.Sounds import Sounds

# Initialisation de pygame et du mixer




def run_new_game(screen, clock, fps, game_mode, player, translator):
    sounds = Sounds()
    sounds.play_slice_sound()
    pygame.mixer.init()
    pygame.mixer.set_num_channels(16)
    current_player = Player_attributes(player)

    game_scores = Scores()

    all_letters = list(string.ascii_uppercase)
    if game_mode == 'easy_mode':
        life = 7
        spawn_delay = 40
        devel = 9
        letters = []
        for letter in range(0,5):
            letters.append(random.choice(all_letters))
            all_letters.remove(letters[-1])

    elif game_mode == 'normal_mode':
        life = 5
        spawn_delay = 35
        devel = 7
        letters = []
        for letter in range(0,7):
            letters.append(random.choice(all_letters))
            all_letters.remove(letters[-1])

    elif game_mode == 'nightmare_mode':
        life = 3
        spawn_delay = 30
        devel = 5
        letters = all_letters.copy()

    frame = 1
    fruits = []
    props = []
    fruits_slices = []

    title = translator.translate("fruit_slicer")
    location = translator.translate("in_game")
    caption = f"{title} - {location}"

    current_background = screen.background(BACKGROUND_IMAGE, caption)
    frozen_effect = screen.frozen()
    
    while True:
        
        prop_pop_list = []
        fruit_pop_list = []
        slice_pop_list = []

        screen.screen.blit(current_background, (0, 0))

        if not current_player.is_alive(life):
            game_scores.update_scores(current_player)
            sounds.play_game_over_sound()
            game_menu = "menu_game_over"
            return game_menu, current_player.score
        
        for fruit in fruits:
            fruit.draw()
            if not current_player.is_frozen():
                if fruit.fall(frame, devel) == 'dropped':
                    index = fruits.index(fruit)
                    fruit_pop_list.append(index)
                    current_player.life_down(life, 'dropped', frame)
  
        for prop in props:
            prop.draw()
            if not current_player.is_frozen():
                if prop.fall(frame, devel) == 'dropped':
                    index = props.index(prop)
                    prop_pop_list.append(index)
        

        display_score_in_game(current_player.score)
        display_hearts(life, current_player.strike)

        if current_player.is_frozen():
            screen.screen.blit(frozen_effect, (0, 0))
            current_player.frozen_up()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "game_off"

            if event.type == pygame.KEYDOWN:
                try:
                    current_player.played_key = str(event.unicode).upper()
                except Exception:
                    current_player.played_key = ''

                for fruit in fruits:
                    if fruit.letter == current_player.played_key:
                        index = fruits.index(fruit)
                        fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.vel_x, fruit.vel_y, fruit.width, fruit.name, 'half_1')
                        fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.vel_x, fruit.vel_y, fruit.width, fruit.name, 'half_2')
                        fruits_slices.append(fruit_slices_1)
                        fruits_slices.append(fruit_slices_2)
                        fruit_pop_list.append(index)
                        sounds.play_slice_sound()
                        current_player.add_score()

                for prop in props:
                    if prop.letter == current_player.played_key:
                        if prop.name == 'bomb':
                            sounds.play_bomb_sound()
                            current_player.life_down(life,'bomb')
                            index = props.index(prop)
                            prop_pop_list.append(index)
                        elif prop.name in ('icecube1', 'icecube2', 'icecube3', 'icecube4'):
                            sounds.play_freeze_sound()
                            current_player.frozen_up()
                            index = props.index(prop)
                            prop_pop_list.append(index)

        for fruit_slice in fruits_slices:
            fruit_slice.draw()
            if not current_player.is_frozen():
                if fruit_slice.fall(frame) == 'dropped':
                    index = fruits_slices.index(fruit_slice)
                    slice_pop_list.append(index)

        
        
        if frame % spawn_delay == 0:
            if not current_player.is_frozen() and current_player.is_alive(life):
                if secrets.randbelow(100) > spawn_delay:
                    fruit = create_element(screen, devel, FRUIT_DICT, letters)
                    fruits.append(fruit)
                if secrets.randbelow(100) > spawn_delay + 50:
                    prop = create_element(screen, devel, PROPS_DICT)
                    props.append(prop)
        
        if frame % 900 == 0:
            if game_mode == 'normal_mode':
                letters.append(random.choice(all_letters))
                all_letters.remove(letters[-1])
            if spawn_delay <= 2:
                pass
            else:
                spawn_delay -=1
                devel -= 0.25
        
        if bool(fruit_pop_list):
            fruit_pop_list.sort(reverse= True)
            for a_fruit in fruit_pop_list:
                # print(f"l'index à pop : {a_fruit}")
                # print(f"longueur fruits list : {len(fruits)}")
                fruits.pop(a_fruit)

        if bool(slice_pop_list):
            slice_pop_list.sort(reverse= True)
            for a_slice in slice_pop_list:
                fruits_slices.pop(a_slice)
                
        if bool(prop_pop_list):
            prop_pop_list.sort(reverse= True)
            for a_prop in prop_pop_list:
                props.pop(a_prop)

        frame = clock_tick(clock, fps, frame)


def create_element(screen, devel, dictionary, letters=None):
    element_list= list(dictionary.keys())
    index = secrets.randbelow(len(element_list))
    
    image = dictionary[element_list[index]]["image"]
    color = dictionary[element_list[index]]["color"]

    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-60, 60)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))

    if not letters:
        random_letter = random.choice(string.ascii_letters).upper()
    else:
        random_letter = random.choice(letters).upper()
    element = Fruits(random_x_position, (screen.height+1), random_size, image, random_rotation, devel, random_letter, color, element_list[index])

    return element