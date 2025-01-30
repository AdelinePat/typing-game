import pygame

pygame.init()

width = 1200
height = 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menu Principal")
background_image = pygame.image.load('background.jpg')
screen.blit(background_image, (0, 0))
fps = 60
timer = pygame.time.Clock()
main_menu = False
font = pygame.font.Font('freesansbold.ttf', 24)
menu_command = 0


class Button:
    def __init__(self, txt, pos):
        self.txt = txt
        self.pos = pos
        self.button = pygame.Rect(self.pos[0], self.pos[1], 260, 40)
        self.clicked = False

    def draw(self):
        pygame.draw.rect(screen, 'orange', self.button, 0, 5)
        pygame.draw.rect(screen, 'beige', self.button, 5, 5)
        text = font.render(self.txt, True, 'brown')
        screen.blit(text, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            if not self.clicked:
                self.clicked = True
                return True
        else:
            self.clicked = False
        return False


def draw_game():
    button = Button('Menu Principal', (500, 100))
    button.draw()
    return button.check_clicked()


def draw_menu():
    command = 0
    # pygame.draw.rect(screen, 'green', [500, 500, 210, 40])
    menu_btn = Button("Exit Menu", (500, 300))
    btn1 = Button("Scores", (500, 150))
    btn2 = Button("Modes", (500, 200))
    btn3 = Button("Jouer", (500, 250))
    btn1.draw()
    btn2.draw()
    btn3.draw()
    menu_btn.draw()
    if menu_btn.check_clicked():
        command = 1
    elif btn1.check_clicked():
        command = 2
    elif btn2.check_clicked():
        command = 3
    elif btn3.check_clicked():
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
        if menu_command >= 1:
            text = font.render(
                f'Le bouton {menu_command - 1} a été cliqué :', True, 'White')
            screen.blit(text, (100, 200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
