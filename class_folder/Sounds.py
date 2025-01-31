import pygame

class Sounds:
    def __init__(self):
        pygame.mixer.init()
        self.slice_sound = pygame.mixer.Sound("./assets/sounds/slice_01.wav")
        self.slice_sound.set_volume(0.5)
        self.bomb_sound = pygame.mixer.Sound("./assets/sounds/explosion-2.wav")
        self.bomb_sound.set_volume(0.5)
        self.freeze_sound = pygame.mixer.Sound("./assets/sounds/freeze.wav")
        self.bomb_sound.set_volume(0.5)

    def play_slice_sound(self):
        self.slice_sound.play()

    def play_bomb_sound(self):
        self.bomb_sound.play()

    def play_freeze_sound(self):
        self.freeze_sound.play()
