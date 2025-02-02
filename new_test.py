from display.display_menu_assets import display_hearts, display_score_in_game, get_buttons, load_scores, display_scores, display_mode_menu
import pygame
from class_folder.Button import Button
from class_folder.Screen import Screen
from game.menues.game_functions import init_game_functions, game_off, clock_tick
from game.menues.game_round import run_new_game
from game.menues.game_set_up import run_set_up_game
from class_folder.translation_manager import TranslationManager

from __settings__ import TEXT_COLOR, BACKGROUND_IMAGE, BACKGROUND_IMAGE_MENU

translate_all = TranslationManager()
pygame.init()
screen = pygame.display.set_mode((600, 400))
font = pygame.font.Font(None, 36)


def menu_display(translation):
    screen = Screen(1080, 720)
    current_background = screen.background(
        BACKGROUND_IMAGE, translate_all.translate("fruit_slicer"))
    # screen_rect_center = screen.screen.get_rect().center

    run = True
    screen.screen.blit(current_background, (0, 0))

    screen, fps, clock, player, game_mode, game_menu, language_mode = init_game_functions()

    while run:
        clock_tick(clock, fps)
        main_menu_button, game_menu_button, mode_menu_button, score_menu_button, exit_menu_button, button_list = get_buttons(
            translation)

        mouse_position = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = "main_menu"

            match game_menu:
                case "start_menu":
                    game_menu_text = translation.translate("start_menu")
                    screen.screen.blit(current_background, (0, 0))
                    game_menu_button = Button(450, 100, game_menu_text, "game_on", 1, ((
                        screen.width // 2), (screen.height // 8)))
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
                    screen.screen.blit(current_background, (0, 0))
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
                    # TODO afficher les scores et les joueurs associés sur plusieurs page avec option supression
                    window_title = translate_all.translate(
                        "fruit_slicer")+"  - " + translate_all.translate("score")
                    new_background = screen.background(
                        BACKGROUND_IMAGE_MENU, window_title)
                    screen.screen.blit(new_background, (0, 0))
                    scores = load_scores()
                    display_scores(scores, translate_all)
                    # score_menu_button.draw("green")

                    # exit_menu_button.draw("brown")

                case "mode_menu":
                    # TODO afficher les modes de jeu possible et les langues (si on a les temps)
                    # screen.screen.blit(current_background, (0,0))
                    # mode_menu_button.draw("purple")
                    # exit_menu_button.draw("blue")
                    window_title = translate_all.translate(
                        "fruit_slicer")+"  - " + translate_all.translate("score")
                    new_background = screen.background(
                        BACKGROUND_IMAGE_MENU, window_title)
                    screen.screen.blit(new_background, (0, 0))
                    button_mode_list, language_list = display_mode_menu(
                        game_mode, language_mode, translate_all)

                    for language in language_list:
                        # for event in pygame.event.get():
                        if language.rect.collidepoint(mouse_position):
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                language_mode = language.identification
                                if language_mode == "english_mode":
                                    translate_all.set_language("eng")
                                elif language_mode == "french_mode":
                                    translate_all.set_language("fr")
                                else:
                                    print("Langue invalide !!")
                    # print(game_mode)
                    # print(language)

                case "game_on":
                    # TODO fonction qui demande le nom d'utilisateur avant de lancer la boucle de jeu
                    game_menu, game_mode, player = run_set_up_game(
                        screen, clock, fps, game_mode, player)

                case "in_game":
                    game_menu = run_new_game(
                        screen, clock, fps, game_mode, player)

                case "menu_game_over":
                    pass
                    # TODO créer le menu game over ololol

                    # TODO boucle de jeu et tout ce qui va avec

                    # game_menu_screen()
                    # screen.screen.blit(current_background, (0,0))
                    # game_menu_button.draw("black")
                    # exit_menu_button.draw("blue")
                case "exit_menu" | _:
                    game_off()

        # pygame.display.flip()

        pygame.display.update()


menu_display(translate_all)

