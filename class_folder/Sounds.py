import pygame
from __settings__ import SOUND_BOMB, SOUND_FREEZE

class Sounds:
    def __init__(self):
        self.explose_sound = pygame.mixer.Sound("SOUND_BOMB")
        self.freeze_sound = pygame.mixer.Sound("SOUND_FREEZE")
        self.music_volume = pygame.mixer.set_voluem(0.25)
        self.volume()

    def sound_volume(self):
        self.explose_sound.set_volume(0.15)
        self.explose_sound.set_volume(0.05)



"""
faudra rajouter ça la liste slice_sound.pay() sous fruit.pop(index)
   for fruit in fruits:
        if event.key == pygame.key.key_code(letter):
            if len(fruits) > 0:
                if fruit.letter.lower() == letter:
                    index = fruits.index(fruit)
                
                    fruit_slices_1 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen)
                    fruit_slices_2 = Fruit_slices(fruit.x, fruit.y, fruit.width, fruit.name, screen.screen)
                    fruits_slices.append(fruit_slices_1)
                    fruits_slices.append(fruit_slices_2)
                    fruits.pop(index)

                
                    slice_sound.play()
"""
