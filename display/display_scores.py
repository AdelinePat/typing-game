import pygame
from display.display_models.Button_image import Button_image
from __settings__ import SCREEN, BUTTON_IMAGE3, MAIN_FONT, STYLE_FONT, TEXT_COLOR, TEXT_COLOR_LIGHT


def display_scores(scores):
    in_score_button = Button_image(450, 100, "Scores", "in_score", BUTTON_IMAGE3, SCREEN.screen, ((SCREEN.width // 2), 70))
    in_score_button.draw(TEXT_COLOR)

    if not scores:
        print("y'a pas de scores enregistré")
    else:
        all_player = list(scores.keys())

        position_x = 20
        position_y = 150
        for player in all_player:
            if position_x < SCREEN.width - 30:
                display_player_score(scores, player, position_x, position_y)
                position_x += SCREEN.width // 4
            else:
                position_x = 20
                position_y += SCREEN.height // 4 + 20
                display_player_score(scores, player, position_x, position_y)
                position_x += SCREEN.width // 4

def display_player_score(scores, player, position_x, position_y):
    box = pygame.Rect(position_x, position_y, (SCREEN.width // 4) - 40 , (SCREEN.height // 4))
    box_center = box.center
    draw_box = pygame.draw.rect(SCREEN.screen, "red", box, 3)

    user = dialog_render(player.capitalize(), STYLE_FONT, 34, TEXT_COLOR, (box_center[0], box_center[1] - box.height // 2 + 40), SCREEN.screen)
    highscore = dialog_render("Highscore : " + str(scores[player]["highscore"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1] - box.height // 2 + 90), SCREEN.screen)
    slice = dialog_render("Slashed Fruits : " + str(scores[player]["slashed_fruits"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1] - box.height // 2 + 120), SCREEN.screen)
    game = dialog_render("Game Played : " + str(scores[player]["games_played"]), MAIN_FONT, 20, TEXT_COLOR_LIGHT, (box_center[0], box_center[1]- box.height // 2 + 150), SCREEN.screen)
    
def dialog_render(text, font, font_size, color, box_center, screen):
    font = pygame.font.Font(font, font_size)
    dialog = font.render(text, True, color)
    dialog_rect = dialog.get_rect(center = box_center)

    screen.blit(dialog, dialog_rect)