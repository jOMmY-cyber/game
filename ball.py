import random 
import pygame
class ball:
    def __init__(self, screen, color):
        self.c = color
        self.screen = screen
        self.x = random.randint(0,300)
        self.y = random.randint(0,50)
        self.speed = 2
    def draw(self):
        pygame.draw.circle(self.screen, self.c,(self.x,self.y), 5)
        self.y += self.speed
        if self.y > 300:
            self.reset()
    def checkhit(self, xmin, xmax, score, combo):
        c1 = self.y > 245 and self.y < 255
        if self.x > xmin and self.x < xmax and c1:
            score += 1
            self.speed += 1
            self.reset()
            combo += 1
        if self.y >290:
            self.speed  = 2
            combo = 0
        return score,combo
    def reset(self):
        self.x = random.randint(0,300)
        self.y = random.randint(0,50)

