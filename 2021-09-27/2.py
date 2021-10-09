import pygame
from pygame.draw import *

#colours in RGB-format

MOUNTAINS = (179, 179, 179)
EARTH = (170, 222, 135)
WHITE = (255, 255, 255)
SKY = (175, 221, 233)
LILAAUGEN = (229, 128, 255)
GREENBUSH = (113, 200, 55)
BLACK = (0, 0, 0)
YELLOW = (255, 233, 0)

pygame.init()
FPS = 30
SCREEN_WIDTH, SCREEN_HEIGHT = 397, 562
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#functions to draw anything in this world

def contouredellipse(surface, color1, color2, tupleofparametres):
    '''
    contouredellipse draws contoured ellipse
    surface defines the surface it will be drawn on
    color2 defines the color of contour
    color1 defines the filling color
    tuple of parametres defines rectangle 
    to indicate the position and dimensions of the ellipse 
    the ellipse will be centered inside the rectangle and bounded by it
    '''
    ellipse(surface, color1, tupleofparametres)
    ellipse(surface, color2, tupleofparametres, width=1)
    
def draw_cvetochek(x, y, scale, surf):
    '''
    draw_cvetochek draws cvetochek
    x, y define the position of cvetochek
    x must be less than SCREEN_WIDTH
    y must be less than SCREEN_HEIGHT
    surf defines the surface the cvetochek will be drawn on
    '''
    l = 15 * scale  # характерный размер цветочка
    x_list = [-0.9, 0, 0.8]
    y_list = [-0.3, -0.5, -0.3]
    for i in range(3):
        contouredellipse(surf, WHITE, MOUNTAINS, 
                (x + x_list[i] * l, y + y_list[i] * l, 2 * l, l))
    ellipse(surf, YELLOW, (x, y, 2 * l, l))
    for i in range(3):
        contouredellipse(surf, WHITE, MOUNTAINS,
                (x - x_list[i] * l, y - y_list[i] * l, 2 * l, l))

def draw_klumba(x, y, scale, should_be_flipped=False):
    '''
    draw_klumba draws klumba consisting of cvetochki
    using function draw_cvetochek()
    x, y define the position of cvetochek(top left corner)
    x, y must be less than SCREEN_WIDTH, SCREEN_HEIGHT respectively
    scale defines the size of klumba
    should_be_flipped takes meaning TRUE or FALSE
    should_be_flipped bool indicates if big floppa should flop the klumba 
    '''
    klumba_surf = pygame.Surface((scale * 70, scale * 70), pygame.SRCALPHA, 32)
    klumba_surf = klumba_surf.convert_alpha()
    # pygame.draw.rect(klumba_surf, EARTH, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
    circle(klumba_surf, GREENBUSH, (scale * 35, scale * 35), scale * 35)
    for i in [(12, 18), (30, 8), (45, 18), (31, 31), (12, 31), (20, 45), (40, 50), (45, 35)]:
        draw_cvetochek(scale * i[0], scale * i[1], scale * 0.5, klumba_surf)
    if(should_be_flipped == True):
        klumba_surf = pygame.transform.flip(klumba_surf, True, False)
    screen.blit(klumba_surf, (x, y))

def draw_animal_leg(x, y, scale, surface):
    '''
    is a support function that draws llama's leg
    x, y define the position of llama's leg
    x, y must be less than SCREEN_WIDTH, SCREEN_HEIGHT respectively
    scale defines the size of leg
    '''
    leg_surf = pygame.Surface((scale * 35, scale * 100), pygame.SRCALPHA, 32)
    leg_surf = leg_surf.convert_alpha()
    ellipse(leg_surf, WHITE, (0, 0, scale * 25, scale * 40))
    ellipse(leg_surf, WHITE, (0, scale * 40, scale * 25, scale * 40))
    ellipse(leg_surf, WHITE, (0, scale * 80, scale * 35, scale * 20))
    surface.blit(leg_surf, (x, y))

def draw_animal_ear(x, y, scale, surface):
    '''
    is a support function that draws llama's ear
    x, y define the position of llama's ear
    x, y must be less than SCREEN_WIDTH, SCREEN_HEIGHT respectively
    scale defines the size of ear    
    '''
    polygon(surface, WHITE, [(x, y), (x + scale * 10, y+ scale * 3), (x+scale * 4, y - scale * 3)])

def draw_eye(surf, color, x, y, scale, should_be_flipped=False):
    ''' 
    draw_eye draws llama's eye with a gleam
    surf defines the surface
    x, y define position of left corner of the eye
    x, y must be less than SCREEN_WIDTH, SCREEN_HEIGHT respectively
    color defines the color of the eye
    scale defines the size of the eye
    should_be_flipped takes meaning TRUE or FALSE
    should_be_flipped bool indicates if big floppa should flop the eye
    '''
    #drawing an eye
    circle(surf, color, (230 * scale, 15 * scale), 12 * scale)
    circle(surf, BLACK, (235 * scale, 15 * scale), 8 * scale)
    #drawing an eye gleam
    blik_surf = pygame.Surface((scale * 10, scale * 5), pygame.SRCALPHA, 32)
    blik_surf = blik_surf.convert_alpha()
    ellipse(blik_surf, WHITE, (0, 0, scale * 10, scale * 5))
    blik_surf = pygame.transform.rotate(blik_surf, -60)
    surf.blit(blik_surf, (225 * scale, 5 * scale))
    if(should_be_flipped == True):
        surf = pygame.transform.flip(surf, True, False)    
    screen.blit(surf, (x, y))

def draw_animal(x, y, scale, should_be_flipped=False):
    '''
    draw_animal draws the llama
    x, y define position of llama
    x, y must be less than SCREEN_WIDTH, SCREEN_HEIGHT respectively
    scale defines the size of llama
    should_be_flipped takes meaning TRUE or FALSE
    should_be_flipped bool indicates if big floppa should flop the animal
    '''
    ani_surf = pygame.Surface((scale * 250, scale * 300), pygame.SRCALPHA, 32)
    ani_surf = ani_surf.convert_alpha()
    ellipse(ani_surf, WHITE, (scale * 30, scale * 100, scale * 200, scale * 60)) #drawing the body
    ellipse(ani_surf, WHITE, (scale * 200, 0, scale * 30, scale * 140)) #drawing the neck
    ellipse(ani_surf, WHITE, (scale * 190, 0, scale * 60, scale * 40)) #drawing the head
    draw_animal_ear(179 * scale, 10 * scale, scale * 3, ani_surf)
    draw_animal_ear(178 * scale, 20*scale, scale * 3, ani_surf)
    for i in [(40 * scale, 120 * scale), (80 * scale, 140 * scale), (120 * scale, 125 * scale), (160 * scale, 140 * scale)]:
        draw_animal_leg(i[0], i[1], scale, ani_surf)
    draw_eye(ani_surf, LILAAUGEN, x, y, scale, should_be_flipped)

#sky, earth and mountains

ground = [(0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), (SCREEN_WIDTH, 280),
                (200, 280), (190, 275), (180, 240),(40, 240), (20, 250), (0, 263)]
mountains = [(0, SCREEN_HEIGHT), (SCREEN_WIDTH, SCREEN_HEIGHT), (SCREEN_WIDTH, 50), 
                 (300, 140), (200, 25), (120, 100), (80, 120), (40, 10), (0, 130)]

pygame.draw.rect(screen, SKY, [0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])
polygon(screen, MOUNTAINS, mountains)
polygon(screen, BLACK, mountains, width=1)
polygon(screen, EARTH, ground)
polygon(screen, BLACK, ground, width=1)

#animals and flowers

draw_klumba(200, 390, 2, True)
draw_animal(-150, 290, 2, False)
draw_klumba(10, 250, 1, False)
draw_animal(-290, 150, 2, False)
draw_animal(240, 180, 0.5, True)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
