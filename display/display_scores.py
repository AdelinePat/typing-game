import pygame
from display.display_models.Button_image import Button_image
from display.display_models.Button import Button
from __settings__ import SCREEN, BUTTON_IMAGE3, BUTTON_IMAGE2, BUTTON_IMAGE4, MAIN_FONT, STYLE_FONT, TEXT_COLOR, TEXT_COLOR_LIGHT, TEXT_COLOR_DARK, PLANK_ARROW_RIGHT, PLANK_ARROW_LEFT


def get_scores_menu_page(scores):
    if not scores:
        display_empty_score()
    else:
        all_player = list(scores.keys())
        if len(all_player)%8 != 0:
            number_pages = len(all_player)//8 + 1
        else:
            number_pages = len(all_player)//8
            
    return all_player, number_pages

def create_arrows():
    arrow_right = Button_image(150, 75, "", "button_next", PLANK_ARROW_RIGHT, SCREEN.screen, (SCREEN.width //2 + 100, 7 * SCREEN.height //8))
    arrow_left = Button_image(150, 75, "", "button_previous", PLANK_ARROW_LEFT, SCREEN.screen, (SCREEN.width //2 - 100, 7* SCREEN.height //8))
    return arrow_left, arrow_right

def create_score_title():
    in_score_button = Button_image(450, 100, "Scores", "in_score", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 2), 70))
    in_score_button.draw(TEXT_COLOR)

def display_empty_score():
    create_score_title()
    message = Button("Il n'y a pas encore de scores enregistré", "empty_score", 24, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2))
    message.draw("white")


def display_scores(scores, page):
    arrow_left, arrow_right = create_arrows()
    all_player, number_pages = get_scores_menu_page(scores)

    reset_score_button = Button_image(200, 60, "Réinitialiser", "reset_all_score", BUTTON_IMAGE2, SCREEN.screen, (SCREEN.width - 180, 7* SCREEN.height //8))
    escape_button = Button_image(200, 60, "Retour", "escape_button", BUTTON_IMAGE4, SCREEN.screen, (180, 7* SCREEN.height //8))
    reset_score_button.draw(TEXT_COLOR)
    escape_button.draw(TEXT_COLOR)

    create_score_title()
    
    index_start_list = []
    index_range_list = []
    index_start = 0
    index_range = 8
    for page_id in range(number_pages):
        index_start_list.append(index_start)
        index_range_list.append(index_range)
        if index_start +8 < len(all_player):
            index_start += 8
            index_range += 8    
        if index_range > len(all_player):
            index_range = len(all_player)
    
    position_x = 20
    position_y = 150

    if page == 0:
        arrow_right.draw(TEXT_COLOR_DARK)
    elif page < number_pages:
        arrow_left.draw(TEXT_COLOR_DARK)
        arrow_right.draw(TEXT_COLOR_DARK)
    else:
        arrow_left.draw(TEXT_COLOR_DARK)


    for index in range(index_start_list[page], index_range_list[page]):
        if position_x < SCREEN.width - 30:
            display_player_score(scores, all_player[index], position_x, position_y)
            position_x += SCREEN.width // 4
        else:
            position_x = 20
            position_y += SCREEN.height // 4 + 20
            display_player_score(scores, all_player[index], position_x, position_y)
            position_x += SCREEN.width // 4


    return arrow_left, arrow_right, len(all_player), reset_score_button, escape_button
        # position_x = 20
        # position_y = 150
        # for player in all_player:
        #     if position_x < SCREEN.width - 30:
        #         display_player_score(scores, player, position_x, position_y)
        #         position_x += SCREEN.width // 4
        #     else:
        #         position_x = 20
        #         position_y += SCREEN.height // 4 + 20
        #         display_player_score(scores, player, position_x, position_y)
        #         position_x += SCREEN.width // 4

def display_player_score(scores, player, position_x, position_y):
    box = pygame.Rect(position_x, position_y, (SCREEN.width // 4) - 40 , (SCREEN.height // 4))
    box_center = box.center
    # draw_box = pygame.draw.rect(SCREEN.screen, "red", box, 3)

    user = dialog_render(player.capitalize(), STYLE_FONT, 34, TEXT_COLOR, (box_center[0], box_center[1] - box.height // 2 + 40), SCREEN.screen)
    highscore = dialog_render("Highscore : " + str(scores[player]["highscore"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1] - box.height // 2 + 90), SCREEN.screen)
    slice = dialog_render("Slashed Fruits : " + str(scores[player]["slashed_fruits"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1] - box.height // 2 + 120), SCREEN.screen)
    game = dialog_render("Game Played : " + str(scores[player]["games_played"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1]- box.height // 2 + 150), SCREEN.screen)
    
def dialog_render(text, font, font_size, color, box_center, screen):
    font = pygame.font.Font(font, font_size)
    dialog = font.render(text, True, color)
    dialog_rect = dialog.get_rect(center = box_center)

    screen.blit(dialog, dialog_rect)