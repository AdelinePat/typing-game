import pygame
from class_folder.Screen import Screen
from __settings__ import STYLE_FONT, BUTTON_IMAGE, ASSETS_DICT
from class_folder.Button import Button
TEXT_COLOR = (218, 133, 51)
pygame.init()

width = 1200
height = 720
# screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menu Principal")
# background_image = pygame.image.load(BACKGROUND_IMAGE)
screen = Screen(1080, 720)
background_final = screen.background()
# screen.screen.blit(background_final, (0,0))
# screen.blit(background_image, (0, 0))
fps = 60
timer = pygame.time.Clock()
main_menu = False

menu_command = 0
clock = pygame.time.Clock()

def display_hearts(strike):
    life = 3
    hearts = []
    life_count = life - strike
    if life_count > 0 : 
        life_rect = pygame.Rect(0, 0, 500, 70)
        heart = pygame.transform.smoothscale(pygame.image.load(ASSETS_DICT["heart"]).convert_alpha(), (50, 50))
        hearts.append(heart)

        spacing = 0
        for index in range(life_count):
            for heart in hearts:
                heart_rect = heart.get_rect(center = (40 + spacing, life_rect.center[1]), top=20)
                screen.screen.blit(heart, heart_rect)
                spacing += 60

def display_score_in_game(score):
    score_width = 200
    score_height = 100
    score_rect = pygame.Rect(0, 0, score_width, score_height)
    score_image = pygame.transform.smoothscale(pygame.image.load(ASSETS_DICT["plank2"]).convert_alpha(), (score_width, score_height))
    score_image_rect = score_image.get_rect(top= 10, right= screen.width - 10)
    screen.screen.blit(score_image, score_image_rect)

    font_size = round((score_height // 3)*2)
    font = pygame.font.Font(STYLE_FONT, font_size)
    dialog = font.render(str(score), True, (96, 57, 2))

    dialog_rect = dialog.get_rect(center = score_image_rect.center)
    screen.screen.blit(dialog, dialog_rect)


def game_menu_screen():
    
    KEYDOWN = pygame.KEYDOWN
    counter = 0
    run = True
    while run:

        timer = clock.tick(20)
        counter += 1    
        # timer = time.time()
        screen.screen.blit(background_final, (0, 0))
        strike = 0
        display_hearts(strike)
        score = 1234
        display_score_in_game(score)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # QUIT => listen to close button of window
                run = False
            
            # if event == pygame.KEYDOWN:
            if event.type == KEYDOWN:
                letter = pygame.key.name(event.key)
                print(letter)
        
        pygame.display.update()

def menu_display():
    # screen_rect_center = screen.screen.get_rect().center
    main_menu_button = Button(700, 150, 'Menu Principal', "main_menu", 1, screen.screen.get_rect().center)
    game_menu_button = Button(450, 100, "Jouer", "game_on", 1, ((screen.width // 2), (screen.height // 8)))
    mode_menu_button = Button(450, 100, "Mode", "mode_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)))
    score_menu_button = Button(450, 100, "Score", "score_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*2))
    exit_menu_button = Button(450, 100, "Quitter", "exit_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*3))
    button_list = [game_menu_button, mode_menu_button, score_menu_button, exit_menu_button]
    
    run = True
    screen.screen.blit(background_final, (0,0))
   
    game_menu = "start_menu"

    while run:
        # timer.tick(fps)
        timer = clock.tick(10)

        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = "start_menu"

            match game_menu:
                case "start_menu":
                        screen.screen.blit(background_final, (0,0))         
                        if main_menu_button.rect.collidepoint(mouse_position):
                            main_menu_button.hovered = True
                            main_menu_button.draw("red")
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                game_menu = "main_menu"
                                # return game_menu
                        else:
                            main_menu_button.hovered = False
                            main_menu_button.draw(TEXT_COLOR)

                case "main_menu":
                    screen.screen.blit(background_final, (0,0))
                    for button in button_list:  
                        if button.rect.collidepoint(mouse_position):
                            button.hovered = True
                            button.draw("red")

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                # print("ohlalala")   
                                game_menu = button.identification
                        else:
                            button.hovered = False
                            button.draw(TEXT_COLOR)

                case "score_menu":
                    screen.screen.blit(background_final, (0,0))
                    score_menu_button.draw("green")
                    # exit_menu_button.draw("brown")
                case "mode_menu":
                    screen.screen.blit(background_final, (0,0))
                    mode_menu_button.draw("purple")
                    # exit_menu_button.draw("blue")
                case "game_on":
                    game_menu_screen()
                    # screen.screen.blit(background_final, (0,0))
                    # game_menu_button.draw("black")
                    # exit_menu_button.draw("blue")
                case "exit_menu":
                    run = False
                  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = "main_menu"

        # pygame.display.flip()

        pygame.display.update() 


    pygame.quit()

menu_display()


# game_menu_screen()