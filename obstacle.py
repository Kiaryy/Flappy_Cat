import pygame
from random import randint as rd
pygame.init()
class obst:
    def __init__(self):
        self.x = 800
        self.y1 = rd(250, 500)
        self.y2 = self.y1 - 650
        self.width = 100
        self.height = 500
    
    def move(self):
        
        self.x -= 5
    def respawn(self):
        if self.x + self.width <= 0:
            self.y1 = rd(250, 500)
            self.y2 = self.y1 - 650
            self.x = 800