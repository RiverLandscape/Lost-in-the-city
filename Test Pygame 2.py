import pygame, os, sys

class Obj:
    def __init__(self, x, y, lado):
        self.x = x
        self.y = y
        self.lado = lado
        self.rect = pygame.Rect(self.x,
                                self.y,
                                self.lado,
                                self.lado)
    def collision(self, obj):
        return self.rect.colliderect(obj.rect)

    def player(self, x_change, y_change):
        self.rect.move_ip(x_change, y_change)
        
    def pinta(self, pantalla):
        'Pinta el cuadrado con el color propio'
        self.__pinta(pantalla, self.color)

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('LostIn the cityyyyyyyy')


#Variables

FPS = 60
black = (0,0,0)
white = (255,255,255)
green = (50, 205, 50)
blue = (0, 206, 209)

#Objectes i fons
clock = pygame.time.Clock()
crashed = False
print(os.path.abspath("29E.png"))
carImg = pygame.image.load(os.path.abspath('29E.png'))
carImg = pygame.transform.scale(carImg, (40,40))
carImg = Obj(20, 20, 40)

h1 = pygame.Surface((60, 60))
h1.fill(green)

print(os.path.abspath("Test_C.jpg"))
ciutat = pygame.image.load(os.path.abspath('Test_C.jpg'))
ciutat = pygame.transform.scale(ciutat, (800,600))

################################



#x =  (display_width * 0.45)
#y = (display_height * 0.8)
x_change = 0
y_change = 0
player_speed = 0

while not crashed:
    for event in pygame.event.get():
        #if event.type == pygame.QUIT:
        #    crashed = True
 
        ############################
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0
        print(x_change, y_change)

        ######################
    ##
while not Obj.collision(h1):
    x += x_change
    y += y_change
   ##         
    #gameDisplay.fill(white)
    #gameDisplay.blit(ciutat, (0, 0))
    obj.pinta(gameDisplay)
    obj.player(x, y)
    obj.collision(carImg, h1)
    pygame.display.update()
clock.tick(FPS)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

