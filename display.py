import pygame
import random, secrets

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
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)

    def background(self):
        pygame.display.set_caption("Fruit Slicer")
        background = pygame.transform.scale(pygame.image.load(BACKGROUND_IMAGE).convert_alpha(), (self.size))

        return background

        # self.screen.blit(background, (0, 0)) # put a background picture instead of color

class Fruits():
    def __init__(self, x, y, size, image, rotation, letter):
        self.x = x
        self.y = y
        self.height = size
        self.width = size
        self.surface = (self.width, self.height)
        self.rotation = rotation

        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        
        self.image =  pygame.transform.smoothscale(pygame.image.load(image).convert_alpha(), (self.surface))
        self.image_rotate = pygame.transform.rotozoom(self.image, self.rotation, 1)
        self.rect_image = self.image.get_rect(center = self.box_center)

        # self.image = pygame.image.load(image)
        # self.image = pygame.transform.rotozoom(self.image, self.rotation, 1)

        

        # self.image_center = pygame.Rect(self.x, self.y, self.width, self.height).center
        # (center = (self.width/2, self.height/2))

        self.letter = letter

        self.vel = 1
        self.max_vel = 150
        self.movement = 0

        self.vel_x = random.randrange(-2, 2)
        self.vel_y = (random.randrange(screen.height//2, (screen.height-50)))*-1

    def fall(self):
        # gravity = 0.5
        # friction = 0.99
        # velocity = 1

        # velocity += gravity
        # self.y += velocity
        # if self.y + self.height > screen.height:
        #     self.y = screen.height - self.height

        if self.y > (screen.height + self.height + 1):
            return "dropped" # pour savoir si le fruit n'a pas pu être coupé à temps
        else:
            self.y += self.vel_y
            self.x += self.vel_x
            self.vel_y += 1 + abs(self.vel_y*0.8)



        # if self.y < screen.height:
        #     self.movement += 2
        # if self.movement < (self.max_vel - self.vel) / 2:
        #     self.vel += self.movement

        # self.y += self.vel

    def text_render(self):
        self.box_center = ((self.x + self.width //2) - (self.width // 50), self.y + self.height // 2)
        font_size = round(self.width // 3)
        font = pygame.font.Font(FONT, font_size)
        
        text = font.render(self.letter, True, (0, 0, 0))
        text_shadow = font.render(self.letter, True, (255,255,255))

        text_box = text.get_rect(center = self.box_center)

        text_rotate = pygame.transform.rotate(text, self.rotation)
        text_shadow_rotate = pygame.transform.rotate(text_shadow, self.rotation)

        # screen.screen.blit(text, (self.x + self.width // 4 , self.y + self.height // 9))
        screen.screen.blit(text_shadow_rotate, (text_box[0]+2, text_box[1]+2))
        screen.screen.blit(text_shadow_rotate, (text_box[0]-2, text_box[1]-2))
        screen.screen.blit(text_shadow_rotate, (text_box[0]-2, text_box[1]+2))
        screen.screen.blit(text_shadow_rotate, (text_box[0]+2, text_box[1]-2))

        screen.screen.blit(text_rotate, text_box)
        

    def draw(self):
        self.box_center = (self.x + self.width //2, self.y + self.height // 2)
        self.rect = self.image_rotate.get_rect(x=self.x, y=self.y, center=self.box_center)
        screen.screen.blit(self.image_rotate, self.rect)
        self.text_render()

def create_fruits():
    fruits_list = ["watermelon", "orange", "coconut", "melon", "limon", "kiwi", "apple", "pineapple"]
    # fruits_list = ["limon", "strawberry", "apple"]
    index = secrets.randbelow(len(fruits_list))
    random_size = random.randrange(75, 200)
    random_rotation = random.randrange(-15, 15)
    random_x_position = secrets.randbelow(screen.width)

    match fruits_list[index]:
        case "watermelon":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, WATERMELON_IMAGE, random_rotation, "W")
        case "orange":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, ORANGE_IMAGE,random_rotation, "O")
        case "coconut":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, COCONUT_IMAGE,random_rotation, "C")
        case "melon":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, MELON_IMAGE,random_rotation, "M")
        case "limon":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, LIMON_IMAGE,random_rotation, "L")
        case "kiwi":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, KIWI_IMAGE,random_rotation, "K")
        case "apple":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, APPLE_IMAGE,random_rotation, "A")
        case "pineapple":
            fruit = Fruits(random_x_position, (screen.height+random_size), random_size, PINEAPPLE_IMAGE,random_rotation, "A")
        # case "strawberry":
        #     fruit = Fruits(random_x_position, -(random_height), random_height, WATERMELON_IMAGE, "S")
        
    return fruit
 
screen = Screen(1080, 720)
# fruit = Fruits(540, -100, 100, APPLE_IMAGE, "A")
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

fruits = []

fruits_surface = pygame.Surface(screen.size, pygame.SRCALPHA)
global_rotation = 1

run = True
is_create_fruit = True  

actual_background = screen.background()
screen.screen.blit(actual_background, (0, 0))

while run:

    clock.tick(30)
    # pygame.time.delay(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT => listen to close button of window
            run = False
    keys = pygame.key.get_pressed()

    if is_create_fruit and secrets.randbelow(100) > 80:
        fruit = create_fruits()
        fruits.append(fruit)
        
        if len(fruits) > 20:
            fruits.pop(0)

    screen.screen.blit(actual_background, (0, 0))
    
    # fruit = create_fruits()

    for fruit in fruits:
        fruit.draw()    
        fruit.fall()
    

    # rotated_surface = pygame.transform.rotate(fruits_surface, global_rotation)
    # rotation_rect = rotated_surface.get_rect(center = (screen.width//2, screen.height // 2))
    # global_rotation += 1

    # screen.screen.blit(rotated_surface, rotation_rect.topleft)
        
    # print("ceci est un fruit : ")
    # print(fruit)
    
    
    pygame.display.update() 
    