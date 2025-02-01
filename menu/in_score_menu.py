import pygame
from __settings__ import SCREEN, TEXT_COLOR, TEXT_COLOR_DARK, FPS
# from display.display_models.Screen import Screen
from display.display_models.__settings__ import BACKGROUND_IMAGE_MENU
from display.display_scores import display_scores, display_empty_score, create_score_title, create_footer_buttons
from game.scores.Scores import Scores
from game.game_functions import clock_tick

def in_score_menu(clock, fps):
    page_score = 0
    # score_menu = True
    
    scores = Scores()
    while True:
        new_background = SCREEN.background(BACKGROUND_IMAGE_MENU, "Fruits Slicer - Scores")
        SCREEN.screen.blit(new_background, (0,0))
        create_score_title()
        reset_score_button, escape_button = create_footer_buttons()

        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score_menu = False
                exit()
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                    # score_menu = False
                    game_menu = "main_menu"
                    return game_menu
        if escape_button.image_rect.collidepoint(mouse_position):
            escape_button.draw(TEXT_COLOR_DARK)
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_menu = "start_menu"
                # score_menu = False
                return game_menu        
        
        if not bool(scores.scores):
            display_empty_score()
            escape_button.draw(TEXT_COLOR)
        else:
            escape_button.draw(TEXT_COLOR)
            reset_score_button.draw(TEXT_COLOR)

            arrow_left, arrow_right, number_page = display_scores(scores.scores, page_score)
            if arrow_left.image_rect.collidepoint(mouse_position):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if page_score > 0:
                        page_score -= 1

            if arrow_right.image_rect.collidepoint(mouse_position):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if page_score < number_page - 1:
                        page_score += 1

        if reset_score_button.image_rect.collidepoint(mouse_position) and bool(scores.scores):
            reset_score_button.draw(TEXT_COLOR_DARK)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if scores:
                    scores.erase_all_record()
                    scores = Scores()
        
        clock_tick(clock, fps)
    # return game_menu
