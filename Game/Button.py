import pygame
from Ships import Ship

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.start = False
        self.reset = False
        self.font = pygame.font.Font(None, 32)

    def place_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text = self.font.render(self.text, True, (225,225,225))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def button_event(self, event, coordinates):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos) and self.text == "start game" and len(coordinates.keys()) == 6:
                self.start = True
                self.reset = True
            elif event.button == 1 and self.rect.collidepoint(event.pos) and self.text == "reset game":
                self.reset = True
    
