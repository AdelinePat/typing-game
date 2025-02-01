import pygame
from __settings__ import SCREEN, TEXT_COLOR, TEXT_COLOR_DARK
# from display.display_models.Screen import Screen
from display.display_models.__settings__ import BACKGROUND_IMAGE_MENU
from display.display_scores import display_scores, display_empty_score, display_player_score
from game.scores.Scores import Scores
from game.menues.game_functions import clock_tick

def in_score_menu(clock, fps, scores):
    page_score = 0

    score_menu = True
    
    while score_menu:
        clock_tick(clock,fps)
        new_background = SCREEN.background(BACKGROUND_IMAGE_MENU, "Fruits Slicer - Scores")
        SCREEN.screen.blit(new_background, (0,0))

        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score_menu = False
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    score_menu = False
                    game_menu = "main_menu"

        if not scores:
            display_empty_score()
        else:
            arrow_left, arrow_right, last_player_index, reset_score_button, escape_button = display_scores(scores.scores, page_score)
            if arrow_left.image_rect.collidepoint(mouse_position):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if page_score > 0:
                        page_score -= 1
            if arrow_right.image_rect.collidepoint(mouse_position):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if page_score < last_player_index:
                        page_score += 1
                    else:
                        page_score = 0

        if escape_button.image_rect.collidepoint(mouse_position):
            escape_button.draw(TEXT_COLOR_DARK)
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_menu = "start_menu"
                
        if reset_score_button.image_rect.collidepoint(mouse_position):
            reset_score_button.draw(TEXT_COLOR_DARK)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scores:
                    scores.erase_all_record()

    return game_menu
