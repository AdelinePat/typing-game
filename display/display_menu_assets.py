import pygame,json, os
from class_folder.Screen import Screen
from __settings__ import STYLE_FONT, MAIN_FONT, BUTTON_IMAGE, ASSETS_DICT, SCORE_PATH, TEXT_COLOR, TEXT_COLOR_LIGHT, BACKGROUND_IMAGE_MENU
from class_folder.Button import Button
from class_folder.Button_simple import Button_simple

BUTTON_IMAGE = pygame.image.load(ASSETS_DICT["plank2"])
HEART_IMAGE = pygame.image.load(ASSETS_DICT["heart"])

width = 1200
height = 720
screen = Screen(1080, 720)


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

def get_buttons():
    main_menu_button = Button(700, 150, 'Menu Principal', "main_menu", 1, screen.screen.get_rect().center)
    game_menu_button = Button(450, 100, "Jouer", "game_on", 1, ((screen.width // 2), (screen.height // 8)))
    mode_menu_button = Button(450, 100, "Mode", "mode_menu", 2, ((screen.width // 2), (screen.height // 8) + (screen.height //4)))
    score_menu_button = Button(450, 100, "Scores", "score_menu", 3, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*2))
    exit_menu_button = Button(450, 100, "Quitter", "exit_menu", 4, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*3))
    button_list = [game_menu_button, mode_menu_button, score_menu_button, exit_menu_button]

    return main_menu_button, game_menu_button, mode_menu_button, score_menu_button, exit_menu_button, button_list

def load_scores():
    if not os.path.exists(SCORE_PATH):
        # Create an empty JSON file if it doesn't exist
        with open(SCORE_PATH, "w", encoding="UTF-8") as file:
            json.dump({}, file)

    with open(SCORE_PATH, "r") as file:
        scores = json.load(file)
    return scores


def create_mode_menu_button():
    in_menu_button = Button(450, 100, "Mode", "mode_menu", 2, ((screen.width // 2), 70))
    in_menu_button.draw(TEXT_COLOR)
    difficulty_button = Button(300, 70, "Difficulté", "mode_menu", 1, ((screen.width // 4), (screen.height // 2 - 100)))
    language_button = Button(300, 70, "Langue", "mode_menu", 3, ((screen.width // 4)*3, (screen.height // 2 - 100)))
    difficulty_button.draw(TEXT_COLOR)
    language_button.draw(TEXT_COLOR)


def display_mode_menu(game_mode, language_mode):
    create_mode_menu_button()
    

    #  width, height, text, identification, flip, center
    

    
    # easy_difficulty_button = Button(250, 50, "Facile", "easy_mode", 2, ((screen.width // 4), (screen.height // 2 - 10)))
    # normal_difficulty_button = Button(250, 50, "Normal", "normal_mode", 3, ((screen.width // 4), (screen.height // 2 + 70)))
    # nightmare_difficulty_button = Button(250, 50, "Nightmare", "nightmare_mode", 3, ((screen.width // 4), (screen.height // 2 + 150)))
    # french_button = Button(250, 50, "Français", "french_mode", 4, ((screen.width // 4)*3, (screen.height // 2 - 10)))
    # english_button = Button(250, 50, "Anglais", "english_mode", 1, ((screen.width // 4)*3, (screen.height // 2 + 70)))
    # easy_difficulty_button.draw(TEXT_COLOR)
    # normal_difficulty_button.draw(TEXT_COLOR)
    # nightmare_difficulty_button.draw(TEXT_COLOR)
    # french_button.draw(TEXT_COLOR)
    # english_button.draw(TEXT_COLOR)

    #text, identification, font, font_size, color

    easy_difficulty_button = Button_simple("Facile", "easy_mode", 28, screen.screen, ((screen.width // 4), (screen.height // 2 - 10)))
    normal_difficulty_button = Button_simple("Normal", "normal_mode", 28, screen.screen, (screen.width // 4, screen.height // 2 + 70))
    nightmare_difficulty_button = Button_simple("Nighmare", "nightmare_mode", 28, screen.screen, (screen.width // 4, screen.height // 2 + 150))
    french_button = Button_simple("Français", "french_mode", 28, screen.screen, ((screen.width // 4)*3, screen.height // 2 - 10))
    english_button = Button_simple("Anglais", "english_mode", 28, screen.screen, ((screen.width // 4)*3, screen.height // 2 + 70))

    # easy_difficulty_button.text_render(MAIN_FONT, "white")
    # normal_difficulty_button.text_render(MAIN_FONT, "white")
    # nightmare_difficulty_button.text_render(MAIN_FONT, "white")

    # french_button.text_render(MAIN_FONT, "white")
    # english_button.text_render(MAIN_FONT, "white")
                                            

    button_list = [easy_difficulty_button, normal_difficulty_button, nightmare_difficulty_button]
    # difficulty_list = [easy_difficulty_button, normal_difficulty_button, nightmare_difficulty_button]
    language_list = [french_button, english_button]

    for button in button_list:
        if game_mode == button.identification:
                button.text_render(MAIN_FONT, "red")
        else:
            button.text_render(MAIN_FONT, "white")

    for language in language_list:
        if language_mode == language.identification:
                language.text_render(MAIN_FONT, "red")
        else:
            language.text_render(MAIN_FONT, "white")
            
    return button_list, language_list


                    
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     game_mode = button.identification

                # if game_mode == button.identification:
            #     #     button.text_render(MAIN_FONT, "blue")

                    
            # for language in language_list:
            #     if language.rect.collidepoint(mouse_position):
            #         language.text_render(MAIN_FONT, "red")
                    
            #         if event.type == pygame.MOUSEBUTTONDOWN:
            #             language = language.identification   
            #             button.text_render(MAIN_FONT, "blue")

    # return game_mode, language_mode
                




def display_scores(scores):
    in_score_button = Button(450, 100, "Scores", "in_score", 3, ((screen.width // 2), 70))
    in_score_button.draw(TEXT_COLOR)

    if not scores:
        print("y'a pas de scores enregistré")
    else:
        
        all_player_score = list(scores.keys())

        
        position_x = 20
        position_y = 150
        for player_score in all_player_score:

            if position_x < screen.width + 30:
            # if all_player_score.index(player_score) < 4:
                display_player_score(scores, player_score, position_x, position_y)
                position_x += screen.width // 4
            else:
            # elif all_player_score.index(player_score) > 4:
                position_x = 20
                position_y += screen.height // 4 + 20
                display_player_score(scores, player_score, position_x, position_y)
                position_x += screen.width // 4

            

def display_player_score(scores, player, position_x, position_y):
    box = pygame.Rect(position_x, position_y, (screen.width // 4) - 40 , (screen.height // 4))
    center = box.center

    # draw_box = pygame.draw.rect(screen.screen, "red", box, 3)

    user = dialog_render(player.capitalize(), STYLE_FONT, 34, TEXT_COLOR)
    highscore = dialog_render("Highscore : " + str(scores[player]["highscore"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT)
    slice = dialog_render("Slashed Fruits : " + str(scores[player]["slashed_fruits"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT)
    game = dialog_render("Game Played : " + str(scores[player]["games_played"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT)

   
    box_user = user.get_rect(center= (center[0], center[1] - box.height // 2 + 40))

    box_highscore = highscore.get_rect(center= (center[0], center[1] - box.height // 2 + 90))

    box_slice = slice.get_rect(center= (center[0], center[1] - box.height // 2 + 120))

    box_game = game.get_rect(center= (center[0], center[1]- box.height // 2 + 150))

    screen.screen.blit(user, box_user)
    screen.screen.blit(highscore, box_highscore)
    screen.screen.blit(slice, box_slice)
    screen.screen.blit(game, box_game)


    
def dialog_render(text, font, font_size, color):
    font = pygame.font.Font(font, font_size)
    dialog = font.render(text, True, color)
    return dialog





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