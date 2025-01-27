import pygame

BACKGROUND_IMAGE = "fruits/assets/background.jpg"

APPLE_IMAGE = "fruits/assets/apple.JPG"
LIMON_IMAGE = "fruits/assets/limon.JPG"
STRAWBERRY_IMAGE = "fruits/assets/strawberry.JPG"

FONT = "fruits/assets/Coolvetica Rg.otf"

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self):
        pygame.display.set_caption("Slice Fruits")
        background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), (self.size))

        self.screen.blit(background, (0, 0)) # put a background picture instead of color

class Fruits():
    def __init__(self, x, y, height, image, letter):
        self.x = x
        self.y = y
        self.height = height
        self.width = height
        self.size = (self.width, self.height)
        self.image =  pygame.transform.scale(pygame.image.load(image), (self.size))
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        self.letter = letter
        self.vel = 35

    def text_render(self):
        font_size = round(self.width // 1.5) 
        font = pygame.font.Font(FONT, font_size )

        text = font.render(self.letter, True, (0, 0, 0))

        screen.screen.blit(text, (self.x + self.width // 4 , self.y + self.height // 9))

    def draw(self):
        # pygame.draw.rect(screen.screen, (0,0,0), (self.x, self.y, self.width, self.height))
        screen.screen.blit(self.image, self.rect)



screen = Screen(1080, 720)

apple = Fruits(540, 0, 100, APPLE_IMAGE, "A")

pygame.init()
pygame.font.init()

run = True
while run:

    

    pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
    screen.background()
    apple.draw()
    apple.text_render()
    
    pygame.display.update() 