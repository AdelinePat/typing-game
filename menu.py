import pygame
from class_folder.Screen import Screen
from __settings__ import STYLE_FONT, BUTTON_IMAGE
TEXT_COLOR = (218, 133, 51)
pygame.init()

width = 1200
height = 720
# screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menu Principal")
# background_image = pygame.image.load(BACKGROUND_IMAGE)
screen = Screen(1080, 720)
background_final = screen.background()
screen.screen.blit(background_final, (0, 0))
# screen.blit(background_image, (0, 0))
fps = 60
timer = pygame.time.Clock()
main_menu = False

menu_command = 0


class Button:
    def __init__(self, width, height, text, flip, center):
        self.text = text
        self.width = width
        self.height = height
        self.surface = (self.width, self.height)
        self.image = pygame.transform.smoothscale(
            pygame.image.load(BUTTON_IMAGE).convert_alpha(), (self.surface))
        # self.center = (self.x + self.width //2, self.y + self.height // 2)
        self.center = center
        self.rect = self.image.get_rect(center=self.center)
        self.flip = flip

        # self.button = pygame.Rect(self.x, self.y, 260, 40)
        self.clicked = False

    def draw(self):
        # pygame.draw.rect(screen.screen, 'orange', self.button, 0, 5)
        # pygame.draw.rect(screen.screen, 'beige', self.button, 5, 5)
        screen.screen.blit(self.image, self.rect)

        font_size = round(self.height // 2)
        font = pygame.font.Font(STYLE_FONT, font_size)
        dialog = font.render(self.text, True, TEXT_COLOR)

        dialog_rect = dialog.get_rect(center=self.center)
        screen.screen.blit(dialog, dialog_rect)

    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if not self.clicked:
                self.clicked = True
                return True
        else:
            self.clicked = False
        return False


def draw_game(translation):
    # screen_rect_center = screen.screen.get_rect().center
    main_menu_text = translation.translate("main_menu")
    main_menu_button = Button(
        700, 150, main_menu_text, 1, screen.screen.get_rect().center)
    # button_rect = button.image.get_rect(center = screen_rect_center)
    main_menu_button.draw()
    return main_menu_button.check_clicked()


def draw_menu(translation):

    command = 0
    # pygame.draw.rect(screen, 'green', [500, 500, 210, 40])
    game_menu_text = translation.translate("main_menu")
    game_menu_button = Button(450, 100, game_menu_text, 1,
                              ((screen.width // 2), (screen.height // 8)))
    mode_menu_text = translation.translate("Mode")
    mode_menu_button = Button(450, 100, mode_menu_text, 1, ((
        screen.width // 2), (screen.height // 8) + (screen.height // 4)))
    score_menu_text = translation.translate("Score")
    score_menu_button = Button(450, 100, score_menu_text, 1, ((
        screen.width // 2), (screen.height // 8) + (screen.height // 4)*2))
    exit_menu_text = translation.translate("Exit_menu")
    exit_menu_button = Button(450, 100, exit_menu_text, 1, ((
        screen.width // 2), (screen.height // 8) + (screen.height // 4)*3))
    # btn2 = Button("Modes", (500, 200))
    # btn3 = Button("Jouer", (500, 250))
    score_menu_button.draw()
    mode_menu_button.draw()
    game_menu_button.draw()
    exit_menu_button.draw()
    if exit_menu_button.check_clicked():
        command = 1
    elif score_menu_button.check_clicked():
        command = 2
    elif mode_menu_button.check_clicked():
        command = 3
    elif game_menu_button.check_clicked():
        command = 4
    else:
        print('impossible')
    return command


run = True
while run:
    timer.tick(fps)
    if main_menu:
        menu_command = draw_menu()
        if menu_command > 0:
            main_menu = False
    else:
        main_menu = draw_game()
        # if menu_command >= 1:
        #     text = font.render(
        #         f'Le bouton {menu_command - 1} a été cliqué :', True, 'White')
        #     screen.screen.blit(text, (100, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
