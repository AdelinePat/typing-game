import pygame, random, secrets, string
from class_folder.Fruits import Fruits
from class_folder.Fruit_slices import Fruit_slices
# <<<<<<< HEAD
from __settings__ import FRUIT_DICT, ICECUBE_IMAGE, BOMB_IMAGE, ICECUBE_COLOR, BOMB_COLOR, BACKGROUND_IMAGE
# =======
from game.menues.game_functions import clock_tick
from __settings__ import FRUIT_DICT
# >>>>>>> 424c21e502b879d3f3c5d45216ceee4e08c7d7ed
from game.scores.Player_attributes import Player_attributes
from game.scores.Scores import Scores
from display.display_menu_assets import display_hearts, display_score_in_game

# <<<<<<< HEAD
class Game_round(Game_methods):
    def __init__(self):
        self.strike = 0
        self.current_player = Player_attributes(Game_methods.player)
        self.game_scores = Scores()
        self.game_mode = Game_methods.game_mode
        if self.game_mode == 'normal':
            self.life = 5
            self.spawn_delay = 40
            self.letters = []
            for letter in range(0,8):
                self.letters.append(random.choice(string.ascii_uppercase))
        elif self.game_mode == 'nightmare':
            self.life = 3
            self.spawn_delay = 30
            self.letters = string.ascii_uppercase
        self.frame = 0
        self.fruits = []
        self.slashed_fruits = []
        self.current_background = self.screen.background(BACKGROUND_IMAGE, "Fruits Slicer - Partie en cours")
        self.frozen_effect = self.screen.frozen()
        
# =======
def run_new_game(screen, clock,fps, game_mode, player):
    current_player = Player_attributes(player)
    game_scores = Scores()
    game_mode = game_mode
    if game_mode == 'normal':
        life = 5
        spawn_delay = 40
        letters = []
        for letter in range(0,8):
            letters.append(random.choice(string.ascii_uppercase))
    elif game_mode == 'nightmare':
        life = 3
        spawn_delay = 30
        letters = string.ascii_uppercase
    frame = 0
    fruits = []
    slashed_fruits = []
    current_background = screen.background()
    frozen_effect = screen.frozen()
    fruits_slices = []
    while True:
        if not current_player.alive(life):
            game_scores.update_scores(current_player)
            return "menu_game_over"
        screen.screen.blit(current_background, (0, 0))
        fruits_on_screen = fruits.copy()
        for fruit in fruits_on_screen:
            if not current_player.frozen():
                if fruit.fall() == 'dropped':
                    index = fruits.index(fruit)
                    fruits.pop(index)
                    current_player.life_down(life, 'dropped', frame)
            fruit.draw()
        for fruit_slice in fruits_slices:
                fruit_slice.draw()
                fruit_slice.fall()
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
                                slashed_fruits.append(fruit)
                                index = fruits.index(fruit)
                                fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen)
                                fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen)
                                fruits_slices.append(fruit_slices_1)
                                fruits_slices.append(fruit_slices_2)
                                fruits.pop(index)
                                current_player.add_score()                
                        print(current_player.score)
                    except Exception:
                        pass
        if frame % 1300 == 0:
            if spawn_delay <= 2:
                pass
            else: spawn_delay -=2
        if frame % spawn_delay == 0:
            if not current_player.frozen() and current_player.alive(life):
                if secrets.randbelow(100) > spawn_delay:
                    fruit = create_fruits(screen)
                    fruits.append(fruit)
                
        frame = clock_tick(clock, fps, frame)

def create_fruits(screen):
    fruits_list= list(FRUIT_DICT.keys())
    index = secrets.randbelow(len(fruits_list))
# >>>>>>> 424c21e502b879d3f3c5d45216ceee4e08c7d7ed
    
    image = FRUIT_DICT[fruits_list[index]]["image"]
    color = FRUIT_DICT[fruits_list[index]]["color"]

    random_size = random.randrange(100, 175)
    random_rotation = random.randrange(-60, 60)
    random_x_position = random.randrange(random_size//4, (screen.width - random_size))

    string.ascii_letters
    random_letter = random.choice(string.ascii_letters).upper()

    fruit = Fruits(random_x_position, (screen.height+1), random_size, image, random_rotation, random_letter, color, screen.height, screen.screen, screen.width, fruits_list[index])

    return fruit