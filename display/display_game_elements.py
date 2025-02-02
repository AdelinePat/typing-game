import pygame
from __settings__ import SCREEN, HEART, PLANK_SCORE, STYLE_FONT

def display_hearts(life, strike):
    hearts = []
    life_count = life - strike
    if life_count > 0 : 
        life_rect = pygame.Rect(0, 0, 500, 70)
        heart = pygame.transform.smoothscale(HEART, (50, 50)).convert_alpha()
        for index in range(life_count):
            hearts.append(heart)

        spacing = 0
        # for index in range(life_count):
        for heart in hearts:
            heart_rect = heart.get_rect(center = (40 + spacing, life_rect.center[1]), top=20)
            SCREEN.screen.blit(heart, heart_rect)
            spacing += 60

def display_score_in_game(score):
    score_width = 200
    score_height = 100
    score_rect = pygame.Rect(0, 0, score_width, score_height)
    score_image = pygame.transform.smoothscale(PLANK_SCORE, (score_width, score_height)).convert_alpha()
    score_image_rect = score_image.get_rect(top= 10, right= SCREEN.width - 10)
    SCREEN.screen.blit(score_image, score_image_rect)

    font_size = round((score_height // 3)*2)
    font = pygame.font.Font(STYLE_FONT, font_size)
    dialog = font.render(str(score), True, (96, 57, 2))

    dialog_rect = dialog.get_rect(center = score_image_rect.center)
    SCREEN.screen.blit(dialog, dialog_rect)