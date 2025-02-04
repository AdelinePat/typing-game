import pygame

class Sounds:
    def __init__(self):
        pygame.mixer.init()

        # Chargement des effets sonores
        self.slice_sound = pygame.mixer.Sound("./assets/sounds/slice_01.wav")
        self.slice_sound.set_volume(0.5)
        self.bomb_sound = pygame.mixer.Sound("./assets/sounds/explosion-2.wav")
        self.bomb_sound.set_volume(0.5)
        self.freeze_sound = pygame.mixer.Sound("./assets/sounds/freeze.wav")
        self.freeze_sound.set_volume(0.5)
        self.game_over_sound = pygame.mixer.Sound("./assets/sounds/game_over.wav")

        # Chargement de la musique de fond
        self.background_music = "./assets/sounds/ninja.mp3"  # Chemin vers votre fichier MP3

        # Initialisation des canaux
        self.music_channel = pygame.mixer.Channel(0)  # Canal dédié à la musique de fond
        self.effect_channel = pygame.mixer.Channel(1)  # Canal dédié aux effets sonores généraux
        self.bomb_channel = pygame.mixer.Channel(2)  # Canal dédié au son de la bombe

    # Effets sonores
    def play_slice_sound(self):
        self.effect_channel.play(self.slice_sound)

    def play_bomb_sound(self):
        self.bomb_channel.play(self.bomb_sound)

    def play_freeze_sound(self):
        self.effect_channel.play(self.freeze_sound)

    def play_game_over_sound(self):
        self.effect_channel.play(self.game_over_sound)

    # Musique de fond
    def play_background_music(self, volume=0.1):
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(volume)  # Ajuste le volume (0.0 à 1.0)
        pygame.mixer.music.play(-1)  # Joue la musique en boucle

    def stop_background_music(self):
        pygame.mixer.music.stop()
