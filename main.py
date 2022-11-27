import pygame,sys
from pygame.locals import *
import menu 
width,height = 800,600
clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((width, height))

def sex():
    bg = (125, 125, 125)
    x = width/2
    y = height/2

    while True:
        screen.fill(bg)
        keys = pygame.key.get_pressed()
        pygame.draw.rect (screen, (166, 30, 30,), (x, y, 100, 50))
        if keys[K_DOWN]:
            y += 1
        if keys[K_UP]:
            y -= 1
        if keys[K_RIGHT]:
            x += 1
        if keys[K_LEFT]:
            x -= 1
        
        clock.tick(60)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()

menu.menu()
sex()


