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
        self.size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self):
        pygame.display.set_caption("Slice Fruits")
        background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE), (self.size))

        self.screen.blit(background, (0, 0)) 

class Fruits():
    def __init__(self, x, y, height, image, letter):
        self.x = x
        self.y = y
        self.height = height
        self.width = height
        self.size = (self.width, self.height)

        self.image = pygame.transform.scale(pygame.image.load(image), (self.size))

        self.letter = letter
        self.vel = 5

    def fall(self):
        self.y += self.vel

    def text_render(self):
        font_size = round(self.width // 1.5) 
        font = pygame.font.Font(FONT, font_size)
        text = font.render(self.letter, True, (0, 0, 0))
        screen.screen.blit(text, (self.x + self.width // 4, self.y + self.height // 9))

    def draw(self):
        self.rect = self.image.get_rect(x=self.x, y=self.y)
        screen.screen.blit(self.image, self.rect)
        self.text_render()

def create_fruits():
    fruits_list = ["limon", "strawberry", "apple"]
    index = secrets.randbelow(len(fruits_list))

    random_height = random.randrange(50, 150)
    random_x_position = secrets.randbelow(screen.width)
    match fruits_list[index]:
        case "limon":
            fruit = Fruits(random_x_position, -(random_height), random_height, LIMON_IMAGE, "L")
        case "apple":
            fruit = Fruits(random_x_position, -(random_height), random_height, APPLE_IMAGE, "A")
        case "strawberry":
            fruit = Fruits(random_x_position, -(random_height), random_height, STRAWBERRY_IMAGE, "S")

    return fruit


screen = Screen(1080, 720)

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []
fruit_timer = 0
max_fruits_on_screen = 3
fruit_base_speed = 5
speed_increase_interval = 5000
next_speed_increase = pygame.time.get_ticks() + speed_increase_interval

run = True

while run:

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Créer des fruits à intervalles réguliers s'il y a de la place
    fruit_timer += 1
    if fruit_timer >= 30 and len(fruits) < max_fruits_on_screen:
        fruit = create_fruits()
        fruit.vel = fruit_base_speed
        fruits.append(fruit)
        fruit_timer = 0

    # Augmenter la vitesse et le nombre maximal de fruits avec le temps
    current_time = pygame.time.get_ticks()
    if current_time >= next_speed_increase:
        fruit_base_speed += 1
        if max_fruits_on_screen < 10:
            max_fruits_on_screen += 1
        next_speed_increase = current_time + speed_increase_interval

    # Mettre à jour l'écran
    screen.background()

    # Mettre à jour et dessiner les fruits
    for fruit in fruits[:]:
        fruit.draw()
        fruit.fall()
        if fruit.y > screen.height:  # Supprimer les fruits hors de l'écran
            fruits.remove(fruit)

    pygame.display.update()
