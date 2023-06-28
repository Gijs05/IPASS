import pygame

class Scanner:
    def __init__(self, x, y, width, height, color):  
        """
        Initializes a scanner object.

        Args:
            x (int): The x-coordinate of the scanner's top-left corner.
            y (int): The y-coordinate of the scanner's top-left corner.
            width (int): The width of the scanner.
            height (int): The height of the scanner.
            color (tuple): The color of the scanner (RGB values).
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.drag = False
        self.place = False

    def place_scanner(self, surface):
        """
        Draws the scanner on the specified surface.

        Args:
            surface: The surface on which to draw the scanner.
        """
        pygame.draw.rect(surface, self.color, self.rect)
    
    def get_coordinates(self, square_size):
        """
        Retrieves the coordinates covered by the scanner.

        Args:
            square_size (int): The size of each square in the grid.

        Returns:
            list: The list of coordinates covered by the scanner.
        """
        start_col = round(self.rect.x / square_size)
        start_row = round(self.rect.y / square_size)
        end_col = round((self.rect.x + self.rect.width - 1) / square_size)
        end_row = round((self.rect.y + self.rect.height - 1) / square_size)
        new_coords = [(row, col) for row in range(start_row, end_row) for col in range(start_col, end_col)]
        return new_coords
    
    def move_scanner(self):
        """
        Moves the scanner based on the mouse position.
        """
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = (mouse_pos[0]// 10) * 10
        self.rect.y = (mouse_pos[1]// 10) * 10

    def snap(self, coordinates, square_size):
        """
        Snaps the scanner to the specified grid coordinates.

        Args:
            coordinates (tuple): The grid coordinates to snap the scanner to.
            square_size (int): The size of each square in the grid.
        """
        start_col, start_row = coordinates
        start = int(start_col), int(start_row)
        self.rect.x = start[0] * square_size + 10
        self.rect.y = start[1] * square_size + 10
           
    def scanner_event(self, event, square_size):
        """
        Handles scanner events such as mouse clicks and mouse motion.

        Args:
            event (pygame.event.Event): The pygame event object.
            square_size (int): The size of each square in the grid.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if event.button == 1:
                self.drag = True
                self.offset_width = event.pos[0] - self.rect.x
                self.offset_height = event.pos[1] - self.rect.y
        
        elif event.type == pygame.MOUSEBUTTONUP and self.drag:
            if event.button == 1:
                self.drag = False

                start_col = round(self.rect.x / square_size)
                start_row = round(self.rect.y / square_size)
                self.snap((start_col, start_row), square_size)
                            
        elif event.type == pygame.MOUSEMOTION:
            if self.drag:
                self.rect.x = event.pos[0] - self.offset_width
                self.rect.y = event.pos[1] - self.offset_height

                max_x = 23 * square_size - self.rect.width + 10
                max_y = 10 * square_size - self.rect.height
                self.rect.x = max(square_size * 10 + 10, min(self.rect.x, max_x) + 10)
                self.rect.y = max(0, min(self.rect.y, max_y) + 10)
