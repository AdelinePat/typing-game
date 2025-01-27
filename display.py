import pygame
import random, secrets

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
        pygame.display.set_caption("Fruit Slicer")
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

        # self.image_center = pygame.Rect(self.x, self.y, self.width, self.height).center
        # (center = (self.width/2, self.height/2))

        self.letter = letter

        self.vel = 30
        self.max_vel = 150
        self.movement = 0

    def fall(self):
        if self.y < screen.height:
            self.movement += 2

        if self.movement < (self.max_vel - self.vel) / 2:
            self.vel += self.movement

        self.y += self.vel

    def text_render(self):
        font_size = round(self.width // 2)
        font = pygame.font.Font(FONT, font_size)
        
        text = font.render(self.letter, True, (0, 0, 0))
        text_shadow = font.render(self.letter, True, (255,255,255))

        # get image center
        image_center = pygame.Rect(self.x, self.y, self.width, self.height).center
        text_box = text.get_rect(center = image_center)

        # screen.screen.blit(text, (self.x + self.width // 4 , self.y + self.height // 9))
        screen.screen.blit(text_shadow, (text_box[0]+2, text_box[1]+2))
        screen.screen.blit(text_shadow, (text_box[0]-2, text_box[1]-2))
        screen.screen.blit(text_shadow, (text_box[0]-2, text_box[1]+2))
        screen.screen.blit(text_shadow, (text_box[0]+2, text_box[1]-2))

        screen.screen.blit(text, text_box)
        

    def draw(self):
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        screen.screen.blit(self.image, self.rect)
        self.text_render()

def create_fruits():
    # fruits_list = ["watermelon", "orange", "coconut", "melon", "limon", "kiwi", "apple"]
    fruits_list = ["limon", "strawberry", "apple"]
    index = secrets.randbelow(len(fruits_list))
    random_height = random.randrange(50, 150)
    random_x_position = secrets.randbelow(screen.width)

    match fruits_list[index]:
        # case "watermelon":
        #     pass
        # case "orange":
        #     pass
        # case "coconut":
        #     pass
        case "limon":
            fruit = Fruits(random_x_position, -(random_height), random_height, LIMON_IMAGE, "L")
        # case "kiwi":
        #     pass
        case "apple":
            fruit = Fruits(random_x_position, -(random_height), random_height, APPLE_IMAGE, "A")
        case "strawberry":
            fruit = Fruits(random_x_position, -(random_height), random_height, STRAWBERRY_IMAGE, "S")
        
    return fruit

            


 
screen = Screen(1080, 720)
# fruit = Fruits(540, -100, 100, APPLE_IMAGE, "A")
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []

run = True

is_create_fruit = True
while run:

    clock.tick(60)
    # pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
    keys = pygame.key.get_pressed()

    if is_create_fruit:
        fruit = create_fruits()
        fruits.append(fruit)
        
        if len(fruits) > 20:
            fruits.pop(0)

    screen.background()
    # fruit = create_fruits()

    for fruit in fruits:
        fruit.draw()    
        fruit.fall()
    # print("ceci est un fruit : ")
    # print(fruit)
    
    
    pygame.display.update() 
    