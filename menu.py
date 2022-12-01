import pygame, sys
from pygame.locals import *
import player
pygame.init()
width,height = 800,600
clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))
player = player.player_obj()
pygame.display.set_caption('Flappy Cat')
pygame.display.set_icon(player.sprite)


class button():
    def __init__(self, text, x, y, tamx, tamy, col):
        self.tamt = (tamx + tamy) * 0.25
        button_font = pygame.font.SysFont('arialcursiva', int(self.tamt))
        self.text = text
        button_text = button_font.render(self.text, False, (255, 255, 255,))
        self.x = x
        self.y = y
        self.tamx = tamx
        self.tamy = tamy
        rect = button_text.get_rect(center =(x+tamx/2 , y+tamy/2))
        self.col = col
        pygame.draw.rect(screen, col, (x, y, tamx, tamy))
        screen.blit(button_text, rect)
    
    def check(self):
        mouseX = pygame.mouse.get_pos()[0]
        mouseY = pygame.mouse.get_pos()[1]
        if mouseX >= self.x and mouseX <= self.x+self.tamx:
            if mouseY >= self.y and mouseY <= self.y+self.tamy:
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    return True


def menu():
    bgc = (0,0,0)
    menu_font = pygame.font.SysFont('arialcursiva', 50)
    game_name = menu_font.render("Flappy Cat", False, (255, 255, 255))
    center_title = game_name.get_rect(center = (width/2, height/4))
    
    while True:
        
        screen.fill(bgc)
        screen.blit(game_name, center_title)
        
        button_Salir = button("Salir", width/2+50, height/2, 100, 50, (255,0,0))
        button_Jugar = button("Jugar", width/2-150, height/2, 100, 50, (0,255,0))

        if button_Salir.check():
                pygame.quit()
                sys.exit()
        
        if button_Jugar.check():
                break
        
        
        pygame.display.update()
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()



