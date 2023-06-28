import pygame

class Button:
    def __init__(self, x, y, width, height, color, text):
        """
        Represents a button object in a GUI.

        Args:
            x (int): The x-coordinate of the button's top-left corner.
            y (int): The y-coordinate of the button's top-left corner.
            width (int): The width of the button.
            height (int): The height of the button.
            color (tuple): The color of the button in RGB format.
            text (str): The text displayed on the button.

        Attributes:
            rect (pygame.Rect): The rectangular area occupied by the button.
            color (tuple): The color of the button in RGB format.
            text (str): The text displayed on the button.
            start (bool): Indicates if the button represents the "start game" button and has been clicked.
            reset (bool): Indicates if the button represents the "reset game" button and has been clicked.
            font (pygame.font.Font): The font used for rendering the button text.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.start = False
        self.reset = False
        self.font = pygame.font.Font(None, 32)

    def place_button(self, surface):
        """
        Renders and displays the button.

        Args:
            surface: The surface on which to display the button.
        """
        pygame.draw.rect(surface, self.color, self.rect)
        text = self.font.render(self.text, True, (225,225,225))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

    def button_event(self, event, coordinates):
        """
        Handles button events when there is a mouse click.

        Args:
            event: The event object representing the button event.
            coordinates (dict): The dictionary of coordinates.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.rect.collidepoint(event.pos) and self.text == "start game" and len(coordinates.keys()) == 6:
                self.start = True
                self.reset = True
            elif event.button == 1 and self.rect.collidepoint(event.pos) and self.text == "reset game":
                self.reset = True
    
