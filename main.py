import pygame, sys
from pygame.locals import *

pygame.init()
width,height = 800,600
screen = pygame.display.set_mode((width, height))




def menu():
    bgc = (0,0,0)
    menu_font = pygame.font.SysFont('arialcursiva', 50)
    game_name = menu_font.render("Juegardo", False, (255, 255, 255))
    
    while True:
        screen.fill(bgc)
        screen.blit(game_name,(width/2-80, height/4))

        pygame.display.update()
        pygame.time.delay(10)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()


menu()