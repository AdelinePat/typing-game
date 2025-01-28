import pygame
import random
import secrets

BACKGROUND_IMAGE = "fruits/assets/background_name_v2.jpg"

APPLE_IMAGE = "fruits/assets/apple_full.png"
COCONUT_IMAGE = "fruits/assets/coconut_full.png"
KIWI_IMAGE = "fruits/assets/kiwi_full.png"
LIMON_IMAGE = "fruits/assets/limon_full.png"
MELON_IMAGE = "fruits/assets/melon_full.png"
ORANGE_IMAGE = "fruits/assets/orange_full.png"
PINEAPPLE_IMAGE = "fruits/assets/pineapple_full.png"
WATERMELON_IMAGE = "fruits/assets/watermelon_full.png"

FONT = "fruits/assets/Coolvetica Rg.otf"


class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self):
        pygame.display.set_caption("Fruit Slicer")
        background = pygame.transform.scale(
            pygame.image.load(BACKGROUND_IMAGE), (self.size))

        # put a background picture instead of color
        self.screen.blit(background, (0, 0))


class Fruits():
    def __init__(self, x, y, size, image, rotation, letter):
        self.x = x
        self.y = y
        self.height = size
        self.width = size
        self.size = (self.width, self.height)
        self.rotation = rotation

        self.image = pygame.transform.scale(
            pygame.image.load(image), (self.size))
        # self.image = pygame.image.load(image)
        # self.image = pygame.transform.rotozoom(self.image, self.rotation, self.size)

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
        font_size = round(self.width // 3)
        font = pygame.font.Font(FONT, font_size)

        text = font.render(self.letter, True, (0, 0, 0))
        text_shadow = font.render(self.letter, True, (255, 255, 255))

        # get image center
        image_center = pygame.Rect(
            self.x, self.y, self.width, self.height).center
        text_box = text.get_rect(center=image_center)

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
    fruits_list = ["watermelon", "orange", "coconut",
                   "melon", "limon", "kiwi", "apple", "pineapple"]
    # fruits_list = ["limon", "strawberry", "apple"]
    index = secrets.randbelow(len(fruits_list))
    random_size = random.randrange(75, 200)
    random_rotation = random.randrange(-15, 15)
    random_x_position = secrets.randbelow(screen.width)

    match fruits_list[index]:
        case "watermelon":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, WATERMELON_IMAGE, random_rotation, "W")
        case "orange":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, ORANGE_IMAGE, random_rotation, "O")
        case "coconut":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, COCONUT_IMAGE, random_rotation, "C")
        case "melon":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, MELON_IMAGE, random_rotation, "M")
        case "limon":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, LIMON_IMAGE, random_rotation, "L")
        case "kiwi":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, KIWI_IMAGE, random_rotation, "K")
        case "apple":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, APPLE_IMAGE, random_rotation, "A")
        case "pineapple":
            fruit = Fruits(random_x_position, -(random_size),
                           random_size, PINEAPPLE_IMAGE, random_rotation, "A")
        # case "strawberry":
        #     fruit = Fruits(random_x_position, -(random_height), random_height, WATERMELON_IMAGE, "S")

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
        if event.type == pygame.QUIT:  # QUIT => listen to close button of window
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
