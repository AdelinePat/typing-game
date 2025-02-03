import pygame
from display.display_models.Button_image import Button_image
from display.display_models.Button import Button
from __settings__ import SCREEN, BUTTON_IMAGE3, BUTTON_IMAGE2, BUTTON_IMAGE4, MAIN_FONT,\
    STYLE_FONT, TEXT_COLOR, TEXT_COLOR_LIGHT, TEXT_COLOR_DARK, PLANK_ARROW_RIGHT, PLANK_ARROW_LEFT

def get_scores_menu_page(scores, translator):
    if not scores:
        display_empty_score(translator)
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

def create_score_title(translator):
    score_text = translator.translate("score_menu")
    in_score_button = Button_image(450, 100, score_text, "in_score", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 2), 70))
    in_score_button.draw(TEXT_COLOR)

def display_empty_score(translator):
    create_score_title(translator)
    empty_score_text = translator.translate("No_score_record")

    message = Button(empty_score_text, "empty_score", 24, MAIN_FONT, SCREEN.screen, (SCREEN.width//2, SCREEN.height//2))
    message.draw("white")

def create_escape_button(translator, center):
    escape_text = translator.translate("escape_button")
    escape_button = Button_image(200, 60, escape_text, "escape_button", BUTTON_IMAGE4, SCREEN.screen, center)

    return escape_button

def create_footer_buttons(translator):
    reset_text = translator.translate("reset_all_score")
    reset_score_button = Button_image(200, 60, reset_text, "reset_all_score", BUTTON_IMAGE2, SCREEN.screen, (SCREEN.width - 180, 7* SCREEN.height //8))
    escape_button = create_escape_button(translator, (180, 7* SCREEN.height //8))

    return reset_score_button, escape_button

def range_pages(number_pages, all_player):
    index_start_list = []
    index_end_list = []
    index_start = 0
    index_end = 8

    for page_index in range(number_pages):
        index_start_list.append(index_start)
        index_end_list.append(index_end)
        if index_start +8 < len(all_player):
            index_start += 8
            index_end += 8    
        if index_end > len(all_player):
            index_end = len(all_player)
            
    return index_start_list, index_end_list

def draw_arrows(page, number_pages):
    arrow_left, arrow_right = create_arrows()
    if page == 0:
        arrow_right.draw(TEXT_COLOR_DARK)
    elif page < number_pages-1:
        arrow_left.draw(TEXT_COLOR_DARK)
        arrow_right.draw(TEXT_COLOR_DARK)
    else:
        arrow_left.draw(TEXT_COLOR_DARK)
    return arrow_left, arrow_right

def display_scores(scores, page, translator):   
    all_player, number_pages = get_scores_menu_page(scores, translator)
    index_start_list, index_end_list = range_pages(number_pages, all_player)
    arrow_left, arrow_right = draw_arrows(page, number_pages)

    position_x = 20
    position_y = 150
    for index in range(index_start_list[page], index_end_list[page]):
        if position_x < SCREEN.width - 30:
            display_player_score(scores, all_player[index], position_x, position_y, translator)
            position_x += SCREEN.width // 4
        else:
            position_x = 20
            position_y += SCREEN.height // 4 + 20
            display_player_score(scores, all_player[index], position_x, position_y, translator)
            position_x += SCREEN.width // 4
    return arrow_left, arrow_right, number_pages

def display_player_score(scores, player, position_x, position_y, translator):
    box = pygame.Rect(position_x, position_y, (SCREEN.width // 4) - 40 , (SCREEN.height // 4))
    box_center = box.center

    highscore_text = translator.translate("highscore")
    full_highscore_text = f"{highscore_text} : {str(scores[player]["highscore"])}"

    slice_text = translator.translate("Slashed_Fruits")
    full_slice_text = f"{slice_text} : {str(scores[player]["slashed_fruits"])}"

    game_text = translator.translate("Game_Played")
    full_game_text = f"{game_text} : {str(scores[player]["games_played"])}"

    user = dialog_render(player.capitalize(), STYLE_FONT, 34, TEXT_COLOR, (box_center[0], box_center[1] - box.height // 2 + 40), SCREEN.screen)
    highscore = dialog_render(full_highscore_text, MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1] - box.height // 2 + 90), SCREEN.screen)
    slice = dialog_render(full_slice_text , MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1] - box.height // 2 + 120), SCREEN.screen)
    game = dialog_render(full_game_text, MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1]- box.height // 2 + 150), SCREEN.screen)
    
def dialog_render(text, font, font_size, color, box_center, screen):
    font = pygame.font.Font(font, font_size)
    dialog = font.render(text, True, color)
    dialog_rect = dialog.get_rect(center = box_center)

    screen.blit(dialog, dialog_rect)