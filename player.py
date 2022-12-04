import pygame
from utils import resource_path
class player_obj:
    pos = pygame.Vector2()
    pos.xy = 350,300
    vel = pygame.Vector2()
    sprite = pygame.image.load(resource_path('assets\\player.png'))
    vel.xy = 3,0
    angle = 0
    jumpforce = 4.5
    
