import pygame 
class rect:
    def __init__(self, cenx, ceny, width, height):
        # pygame.Rect(left, top, width, height)
        self.x = cenx-width/2
        self.y = ceny-height/2
        self.w = width 
        self.h = height
    def rec(self):
        return pygame.Rect(self.x, self.y, self.w, self.h)
# class player:
#     def __init__(self, x,y)