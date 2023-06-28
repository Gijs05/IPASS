import pygame


class Ship:
    def __init__(self, x, y, width, height, color, name):  
        """
        Initializes a ship object.

        Args:
            x (int): The x-coordinate of the ship's top-left corner.
            y (int): The y-coordinate of the ship's top-left corner.
            width (int): The width of the ship.
            height (int): The height of the ship.
            color (tuple): The color of the ship.
            name (str): The name of the ship.
        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.name = name
        self.drag = False
        self.old_x = x
        self.old_y = y

    def place_ship(self, surface):
        """
        Draws the ship on the specified surface.

        Args:
            surface: The surface on which to draw the ship.
        """
        pygame.draw.rect(surface, self.color, self.rect)

    def rotate(self, square_size, coordinates):
        """
        Rotates the ship and checks for collisions with other ships.

        Args:
            square_size (int): The size of each square in the grid.
            coordinates (dict): The dictionary of ship coordinates.

        Returns:
            bool: True if the ship collides with another ship after rotation, False otherwise.
        """
        self.rect.width, self.rect.height = self.rect.height, self.rect.width
        max_x = 10 * square_size - self.rect.width
        max_y = 10 * square_size - self.rect.height
        self.rect.x = max(0, min(self.rect.x, max_x) + 10)
        self.rect.y = max(0, min(self.rect.y, max_y) + 10)
        if self.collision(coordinates, square_size):
            self.rect.width, self.rect.height = self.rect.height, self.rect.width
            self.rect.x, self.rect.y = self.old_x, self.old_y
        else:
            self.old_x, self.old_y = self.rect.x, self.rect.y
        
    def get_coordinates(self, square_size):
        """
        Retrieves the coordinates covered by the ship.

        Args:
            square_size (int): The size of each square in the grid.

        Returns:
            list: The list of coordinates covered by the ship.
        """
        start_col = round(self.rect.x / square_size)
        start_row = round(self.rect.y / square_size)
        end_col = round((self.rect.x + self.rect.width - 1) / square_size)
        end_row = round((self.rect.y + self.rect.height - 1) / square_size)
        new_coords = [(row, col) for row in range(start_row, end_row) for col in range(start_col, end_col)]
        return new_coords
    
    def move_ship(self):
        """
        Moves the ship based on the mouse position.
        """
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = (mouse_pos[0]// 10) * 10
        self.rect.y = (mouse_pos[1]// 10) * 10
    
    def change_color(self, new_coords, coordinates):
        """
        Changes the color of the ship and updates the ship coordinates.

        Args:
            new_coords (list): The new coordinates covered by the ship.
            coordinates (dict): The dictionary of ship coordinates.

        Returns:
            dict: The updated dictionary of ship coordinates.
        """
        coordinates[self.name] = new_coords
        return coordinates

    def snap(self, coordinates, square_size):
        """
        Snaps the ships position to the nearest grid based on the provided coordinates and square size.

        Args:
            coordinates (tuple): The starting coordinates of the object.
            square_size (int): The size of each square on the grid.
        """
        start_col, start_row = coordinates
        start = int(start_col), int(start_row)
        self.rect.x = start[0] * square_size + 10
        self.rect.y = start[1] * (square_size /13 * 12)
    
    def collision(self, coordinates, square_size):
        """
        Checks for collision between the ship and other ships.

        Args:
            coordinates (dict): A dictionary of coordinates for different objects on the grid.
            square_size (int): The size of each square on the grid.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        for name, coords in coordinates.items():
            if name != self.name:
                if any(coord in coords for coord in self.get_coordinates(square_size)):
                    return True
        return False
           
    def ship_event(self, event, square_size, coordinates):
        """
        Handles ship events, such as dragging, rotating, and snapping.

        Args:
            event: The event object representing the user's input.
            square_size (int): The size of each square on the grid.
            coordinates (dict): A dictionary of coordinates for different objects on the grid.
        """
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if event.button == 1:
                self.drag = True
                self.offset_width = event.pos[0] - self.rect.x
                self.offset_height = event.pos[1] - self.rect.y

            elif event.button == 3:
                self.rotate(square_size, coordinates)
                new_coords = self.get_coordinates(square_size)
                self.change_color(new_coords, coordinates)
          
        
        elif event.type == pygame.MOUSEBUTTONUP and self.drag:
            if event.button == 1:
                self.drag = False
                new_coords = self.get_coordinates(square_size)

                start_col = round(self.rect.x / square_size)
                start_row = round(self.rect.y / square_size)
                if self.collision(coordinates, square_size):
                    self.rect.x, self.rect.y = self.old_x, self.old_y
                else:
                    self.old_x, self.old_y = self.rect.x, self.rect.y
                    self.snap((start_col, start_row), square_size)
                    self.change_color(new_coords, coordinates)
                            
        elif event.type == pygame.MOUSEMOTION:
            if self.drag:
                self.rect.x = event.pos[0] - self.offset_width
                self.rect.y = event.pos[1] - self.offset_height

                max_x = 10 * square_size - self.rect.width
                max_y = 10 * square_size - self.rect.height
                self.rect.x = max(0, min(self.rect.x, max_x) + 10)
                self.rect.y = max(square_size, min(self.rect.y, max_y) + 10)
        
