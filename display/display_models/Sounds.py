import pygame

class Sounds:
    def __init__(self):
        """loading sound effects"""
        pygame.mixer.init()
        self.slice_sound = pygame.mixer.Sound("./assets/sounds/slice_01.wav")
        self.slice_sound.set_volume(0.5)
        self.bomb_sound = pygame.mixer.Sound("./assets/sounds/explosion-2.wav")
        self.bomb_sound.set_volume(0.5)
        self.freeze_sound = pygame.mixer.Sound("./assets/sounds/freeze.wav")
        self.freeze_sound.set_volume(0.5)
        self.game_over_sound = pygame.mixer.Sound("./assets/sounds/game_over.wav")
        # loading background music
        self.background_music = "./assets/sounds/ninja.mp3"

        # Init canals
        self.music_channel = pygame.mixer.Channel(0)  # canal dedicated to background music
        self.effect_channel = pygame.mixer.Channel(1)  # canal dedicated to other sound effects

    # Sound effects
    def play_slice_sound(self):
        self.effect_channel.play(self.slice_sound)

    def play_bomb_sound(self):
        self.effect_channel.play(self.bomb_sound)

    def play_freeze_sound(self):
        self.effect_channel.play(self.freeze_sound)

    def play_game_over_sound(self):
        self.effect_channel.play(self.game_over_sound)

    # Background music
    def play_background_music(self, volume=0.1):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(volume)  # Adjust volume (0.0 to 1.0)
        pygame.mixer.music.play(-1)  # Music loop

    def stop_background_music(self):
        pygame.mixer.music.stop()
