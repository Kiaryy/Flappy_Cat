import pygame,sys
from pygame.locals import *
import menu
from player import player_obj
from utils import collisions
from utils import resource_path
from utils import map
from obstacle import obst
from random import choice as rdc
from random import randint as rd



jump_sound = pygame.mixer.Sound(resource_path('assets\\jump.wav'))    

die_2 = pygame.mixer.Sound(resource_path('assets\\die_2.wav'))
die_3 = pygame.mixer.Sound(resource_path('assets\\die_3.wav'))
die_4 = pygame.mixer.Sound(resource_path('assets\\die_4.wav'))
audio_pint = pygame.mixer.Sound(resource_path('assets\\point.wav'))

hi_score = 0 
def main():
    pygame.init()
    pygame.display.set_caption('Flappy Cat')
    width,height = 800,600    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    player = player_obj()
    pygame.display.set_icon(player.sprite)
    points = 0
    col = False
    points_font = pygame.font.SysFont('Comics Sans MS', 200)
    
    obst1 = obst()
    obst2 = obst()
    obst2.x += 300
    obst3 = obst()
    obst3.x += 600
    
    
    
    player.pos.x = 350
    player.pos.y = 300
    player.vel.y = 0
    player.angle = 0
    
    
    def game_over():
        global hi_score
        if points >= hi_score:
            hi_score = points
        menu_font = pygame.font.SysFont('arialcursiva', 50)
        score_text = menu_font.render("Score: " + str(points), False, (255, 255, 255))
        hi_score_text = menu_font.render("High Score: " + str(hi_score), False, (255, 255, 255))
        score_pos = score_text.get_rect(center = (width/2, height/4))
        hi_score_pos = score_text.get_rect(center = (width/2, height/3))
        s = pygame.Surface((1000,750))
        s.set_alpha(128)
        s.fill((0,0,0))
        screen.blit(s, (0,0))
        screen.blit(score_text, score_pos)
        screen.blit(hi_score_text, hi_score_pos)
        button_Salir = menu.button("Exit", width/2+50, height/2, 100, 50, (255,0,0))
        button_Jugar = menu.button("Retry", width/2-150, height/2, 100, 50, (0,255,0))
        
        if button_Salir.check():
            pygame.quit()
            sys.exit()
        
        if button_Jugar.check():
            main()
    
    
    
    death = [ die_2, die_3, die_4]
    
    
    dead = False
    once = True
    
    g = rd(50, 255)
    b = rd(50, 255)

    
    if g > 180 or b > 180:
        rect_colors = (0, 0, 0)
    else:
        rect_colors = (255, 255, 255)
    
    print(g, b)
    while True:
        
        screen.fill((map(player.pos.y, -5, 615, 0, 255), g, b))
        
        points_text = points_font.render(str(points), False, (0, 0, 0))
        pointst = points_text.get_rect(center = (width/2, height/2))
        screen.blit(points_text, pointst)
        
        
        
        pygame.draw.rect(screen, rect_colors, (obst1.x, obst1.y1, obst1.width, obst1.height), border_radius= 5)
        pygame.draw.rect(screen, rect_colors, (obst1.x, obst1.y2, obst1.width, obst1.height), border_radius= 5)
        
        pygame.draw.rect(screen, rect_colors, (obst2.x, obst2.y1, obst2.width, obst2.height), border_radius= 5)
        pygame.draw.rect(screen, rect_colors, (obst2.x, obst2.y2, obst2.width, obst2.height), border_radius= 5)
        
        pygame.draw.rect(screen, rect_colors, (obst3.x, obst3.y1, obst3.width, obst3.height), border_radius= 5)
        pygame.draw.rect(screen, rect_colors, (obst3.x, obst3.y2, obst3.width, obst3.height), border_radius= 5)
        
        
        
        jump = False
        for event in pygame.event.get():           
            if event.type==pygame.KEYDOWN and event.key==K_SPACE:
                jump = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_presses = pygame.mouse.get_pressed()
                if mouse_presses[0]:
                    jump = True
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        
        rotate = pygame.transform.rotate(player.sprite, player.angle)
        
        screen.blit(rotate, (player.pos.x, player.pos.y))
        
        
        
        if jump and not dead:
            pygame.mixer.Sound.play(jump_sound)
            player.vel.y = 0 
            player.vel.y -= player.jumpforce
        
        if not dead:
            player.pos.y += player.vel.y
            player.vel.y += 0.2
            player.angle = player.vel.y * -2
            obst1.move()
            obst2.move()
            obst3.move()
            
            if not collisions(player.pos.x, player.pos.y, player.sprite.get_width(), player.sprite.get_height(), obst1.x, obst1.y1-150, obst1.width, 150):
                col = False
            
            if not collisions(player.pos.x, player.pos.y, player.sprite.get_width(), player.sprite.get_height(), obst2.x, obst2.y1-150, obst2.width, 150):
                col = False
            
            if not collisions(player.pos.x, player.pos.y, player.sprite.get_width(), player.sprite.get_height(), obst3.x, obst3.y1-150, obst3.width, 150):
                col = False
            
            
            if not col:
                
                
                if player.pos.y + player.sprite.get_height() >= obst1.y1-150 and player.pos.y <= obst1.y1 and obst1.x == player.pos.x:
                    col = True
                    points += 1
                    pygame.mixer.Sound.play(audio_pint)
                if player.pos.y + player.sprite.get_height() >= obst2.y1-150 and player.pos.y <= obst2.y1 and obst2.x == player.pos.x:
                    col = True
                    points += 1
                    pygame.mixer.Sound.play(audio_pint)
                if player.pos.y + player.sprite.get_height() >= obst3.y1-150 and player.pos.y <= obst3.y1 and obst3.x == player.pos.x:
                    col = True
                    points += 1
                    pygame.mixer.Sound.play(audio_pint)

        
        
        
        
        
        
        
        if player.pos.y >= 600:
            dead = True
        
        
        
        if collisions(player.pos.x, player.pos.y+10, player.sprite.get_width()-5, player.sprite.get_height(), obst1.x, obst1.y2, obst1.width, obst1.height):
            dead = True
        if collisions(player.pos.x, player.pos.y+10, player.sprite.get_width()-5, player.sprite.get_height(), obst2.x, obst2.y2, obst2.width, obst2.height):
            dead = True
        if collisions(player.pos.x, player.pos.y+10, player.sprite.get_width()-5, player.sprite.get_height(), obst3.x, obst3.y2, obst3.width, obst3.height):
            dead = True
        
        if collisions(player.pos.x, player.pos.y, player.sprite.get_width()-5, player.sprite.get_height()-5, obst1.x, obst1.y1, obst1.width, obst1.height):
            dead = True
        if collisions(player.pos.x, player.pos.y, player.sprite.get_width()-5, player.sprite.get_height()-5, obst2.x, obst2.y1, obst2.width, obst2.height):
            dead = True
        if collisions(player.pos.x, player.pos.y, player.sprite.get_width()-5, player.sprite.get_height()-5, obst3.x, obst3.y1, obst3.width, obst3.height):
            dead = True
        
        
        
        obst1.respawn()
        obst2.respawn()
        obst3.respawn()
        
        
        
        
        
        if dead:
            if once:
                once = False
                pygame.mixer.Sound.play(rdc(death))
                
            game_over()
        
        
        
        
        clock.tick(60)
        pygame.display.update()
        
        

menu.menu()
main()





