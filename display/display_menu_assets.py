import pygame
from class_folder.Screen import Screen
from __settings__ import STYLE_FONT, BUTTON_IMAGE, ASSETS_DICT
from class_folder.Button import Button

BUTTON_IMAGE = pygame.image.load(ASSETS_DICT["plank2"])
HEART_IMAGE = pygame.image.load(ASSETS_DICT["heart"])
# pygame.init()

width = 1200
height = 720
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Menu Principal")
# background_image = pygame.image.load(BACKGROUND_IMAGE)
screen = Screen(1080, 720)
# screen.screen.blit(background_final, (0,0))
# screen.blit(background_image, (0, 0))
# fps = 60
# timer = pygame.time.Clock()
# main_menu = False

# menu_command = 0
# clock = pygame.time.Clock()

def display_hearts(life, strike):
    hearts = []
    life_count = life - strike
    if life_count > 0 : 
        life_rect = pygame.Rect(0, 0, 500, 70)
        heart = pygame.transform.smoothscale(HEART_IMAGE, (50, 50)).convert_alpha()
        for index in range(life_count):
            hearts.append(heart)

        spacing = 0
        # for index in range(life_count):
        for heart in hearts:
            heart_rect = heart.get_rect(center = (40 + spacing, life_rect.center[1]), top=20)
            screen.screen.blit(heart, heart_rect)
            spacing += 60

def display_score_in_game(score):
    score_width = 200
    score_height = 100
    score_rect = pygame.Rect(0, 0, score_width, score_height)
    score_image = pygame.transform.smoothscale(BUTTON_IMAGE, (score_width, score_height)).convert_alpha()
    score_image_rect = score_image.get_rect(top= 10, right= screen.width - 10)
    screen.screen.blit(score_image, score_image_rect)

    font_size = round((score_height // 3)*2)
    font = pygame.font.Font(STYLE_FONT, font_size)
    dialog = font.render(str(score), True, (96, 57, 2))

    dialog_rect = dialog.get_rect(center = score_image_rect.center)
    screen.screen.blit(dialog, dialog_rect)


# def game_menu_screen():
    
#     KEYDOWN = pygame.KEYDOWN
#     counter = 0
#     run = True
#     while run:

#         timer = clock.tick(20)
#         counter += 1    
#         # timer = time.time()
#         screen.screen.blit(background_final, (0, 0))
#         strike = 0
#         display_hearts(strike)
#         score = 1234
#         display_score_in_game(score)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT: # QUIT => listen to close button of window
#                 run = False
#                 pygame.quit()
#                 exit()
                
            
#             # if event == pygame.KEYDOWN:
#             if event.type == KEYDOWN:
#                 letter = pygame.key.name(event.key)
#                 print(letter)
        
#         pygame.display.update()




# game_menu_screen()