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
# screen.screen.blit(background_final, (0,0))
# screen.blit(background_image, (0, 0))
fps = 60
timer = pygame.time.Clock()
main_menu = False

menu_command = 0


class Button:
    def __init__(self,width, height, text, identification, flip, center):
        self.text = text
        self.width = width
        self.height = height
        self.identification = identification
        self.surface = (self.width, self.height)
        self.image = pygame.transform.smoothscale(pygame.image.load(BUTTON_IMAGE).convert_alpha(), (self.surface))
        # self.center = (self.x + self.width //2, self.y + self.height // 2)
        self.center = center
        self.rect = self.image.get_rect(center = self.center)
        self.flip = flip
        self.hovered = False
        
        # self.button = pygame.Rect(self.x, self.y, 260, 40)
        self.clicked = False

    def draw(self, color):
        # pygame.draw.rect(screen.screen, 'orange', self.button, 0, 5)
        # pygame.draw.rect(screen.screen, 'beige', self.button, 5, 5)
        screen.screen.blit(self.image, self.rect)

        font_size = round(self.height // 2)
        font = pygame.font.Font(STYLE_FONT, font_size)
        dialog = font.render(self.text, True, color)

        dialog_rect = dialog.get_rect(center = self.center)
        screen.screen.blit(dialog, dialog_rect)
        

    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if not self.clicked:
                self.clicked = True
                return True
        else:
            self.clicked = False
        return False


def draw_game():
    # screen_rect_center = screen.screen.get_rect().center
    
    # button_rect = button.image.get_rect(center = screen_rect_center)
    main_menu_button.draw(TEXT_COLOR)
    return main_menu_button.check_clicked()


def draw_menu():
    command = 0
    # pygame.draw.rect(screen, 'green', [500, 500, 210, 40])
    
    # btn2 = Button("Modes", (500, 200))
    # btn3 = Button("Jouer", (500, 250))
    score_menu_button.draw(TEXT_COLOR)
    mode_menu_button.draw(TEXT_COLOR)
    game_menu_button.draw("red")
    exit_menu_button.draw(TEXT_COLOR)
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



def main():
    # screen_rect_center = screen.screen.get_rect().center
    main_menu_button = Button(700, 150, 'Menu Principal', "main_menu", 1, screen.screen.get_rect().center)
    game_menu_button = Button(450, 100, "Jouer", "game_on", 1, ((screen.width // 2), (screen.height // 8)))
    mode_menu_button = Button(450, 100, "Mode", "mode_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)))
    score_menu_button = Button(450, 100, "Score", "score_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*2))
    exit_menu_button = Button(450, 100, "Quitter", "exit_menu", 1, ((screen.width // 2), (screen.height // 8) + (screen.height //4)*3))
    button_list = [game_menu_button, mode_menu_button, score_menu_button, exit_menu_button]
    
    run = True
    screen.screen.blit(background_final, (0,0))

    clock = pygame.time.Clock()

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
                    screen.screen.blit(background_final, (0,0))
                    game_menu_button.draw("black")
                    # exit_menu_button.draw("blue")
                case "exit_menu":
                    run = False
                
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_menu = "start_menu"

        

        # pygame.display.flip()

        pygame.display.update() 


    pygame.quit()

main()
