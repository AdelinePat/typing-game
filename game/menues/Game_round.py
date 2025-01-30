import pygame, random, secrets, string
from class_folder.Fruits import Fruits
from class_folder.Fruit_slices import Fruit_slices
from __settings__ import FRUIT_DICT, ICECUBE_IMAGE, BOMB_IMAGE, ICECUBE_COLOR, BOMB_COLOR, BACKGROUND_IMAGE
from game.scores.Player_attributes import Player_attributes
from game.scores.Scores import Scores
from game.menues.Game_methods import Game_methods
from display.display_menu_assets import display_hearts, display_score_in_game

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
        
    
    def run(self):
        fruits_slices = []
        while True:
            if not self.current_player.alive(self.life):
                return "menu_game_over"
            self.screen.screen.blit(self.current_background, (0, 0))
            fruits_on_screen = self.fruits.copy()
            for fruit in fruits_on_screen:
                if not self.current_player.frozen():
                    if fruit.fall() == 'dropped':
                        index = self.fruits.index(fruit)
                        self.fruits.pop(index)
                        self.current_player.life_down('dropped', self.frame, fruit)
                fruit.draw()
            for fruit_slice in fruits_slices:
                    fruit_slice.draw()
                    fruit_slice.fall()
            display_score_in_game(self.current_player.score)
            display_hearts(self.life, self.current_player.strike)
            if self.current_player.frozen():
                self.screen.screen.blit(self.frozen_effect, (0, 0))
                self.current_player.frozen_up()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "game_off"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and not self.current_player.alive(self.life):
                        self.game_scores.update_scores(self.current_player)
                        return 'main_menu'
                    if not self.current_player.frozen():
                        try:
                            self.current_player.played_key = str(event.unicode).upper()
                            for fruit in self.fruits:
                                if fruit.letter == self.current_player.played_key:
                                    # if fruit.type == 'fruit':
                                    self.slashed_fruits.append(fruit)
                                    index = self.fruits.index(fruit)
                                    fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, self.screen.screen)
                                    fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, self.screen.screen)
                                    fruits_slices.append(fruit_slices_1)
                                    fruits_slices.append(fruit_slices_2)
                                    self.fruits.pop(index)
                                    self.current_player.add_score()
                                    # elif fruit.type == 'icecube':
                                    #     index = self.fruits.index(fruit)
                                    #     self.fruits.pop(index)
                                    #     self.current_player.frozen_up()
                                    # elif fruit.type == 'bomb':
                                    #     index = self.fruits.index(fruit)
                                    #     self.fruits.pop(index)
                                    #     self.current_player.life_down('bomb')
                                    # break                
                            print(self.current_player.score)
                        except Exception:
                            pass
            if self.frame % 1300 == 0:
                if self.spawn_delay <= 2:
                    pass
                else: self.spawn_delay -=2
            if self.frame % self.spawn_delay == 0:
                if not self.current_player.frozen() and self.current_player.alive(self.life):
                    if secrets.randbelow(100) > self.spawn_delay:
                        fruit = self.create_fruits()
                        self.fruits.append(fruit)
                    # if secrets.randbelow(100) > self.spawn_delay + 50:
                    #     fruit = self.create_fruits()
                    #     self.fruits.append(fruit)
                    # if secrets.randbelow(100) > self.spawn_delay + 60:
                    #     fruit = self.create_fruits()
                    #     self.fruits.append(fruit)
                    
            self.frame = self.clock_tick(self.frame)

    def create_fruits(self):
        # fruits_list= list(FRUIT_DICT.keys())
        # index = secrets.randbelow(len(fruits_list))
        # if type == 'fruit':
        #     image = FRUIT_DICT[fruits_list[index]]["image"]
        #     color = FRUIT_DICT[fruits_list[index]]["color"]
        # elif type == 'icecube':
        #     image = ICECUBE_IMAGE
        #     color = ICECUBE_COLOR
        # elif type == 'bomb':
        #     image = BOMB_IMAGE
        #     color = BOMB_COLOR

        # random_size = random.randrange(100, 175)
        # random_rotation = random.randrange(-25, 25)
        # random_x_position = random.randrange(random_size//4, (self.screen.width - random_size))
        # random_letter = random.choice(self.letters)
        fruits_list= list(FRUIT_DICT.keys())
        index = secrets.randbelow(len(fruits_list))
        
        image = FRUIT_DICT[fruits_list[index]]["image"]
        color = FRUIT_DICT[fruits_list[index]]["color"]

        random_size = random.randrange(100, 175)
        random_rotation = random.randrange(-60, 60)
        random_x_position = random.randrange(random_size//4, (self.screen.width - random_size))

        string.ascii_letters
        random_letter = random.choice(string.ascii_letters).upper()

        fruit = Fruits(random_x_position, (self.screen.height+1), random_size, image, random_rotation, random_letter, color, self.screen.height, self.screen.screen, fruits_list[index])

        return fruit