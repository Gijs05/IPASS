import pygame

class Label():
    def __init__(self, x, y, color, text):
        self.x = x
        self.y = y
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 32)
    
    def place_label(self):
        self.font.render(self.text, True, self.color)
        self.center = (self.x, self.y)
        