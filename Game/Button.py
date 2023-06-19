import pygame

class Button:
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = pygame.font.Font(None, 32)

    def place_button(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        text = self.font.render(self.text, True, (10, 10, 10))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
    
    def button_event(self, event, ships):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos):
                # for ship in ships:
                #     ship.check_location()
                print("button")