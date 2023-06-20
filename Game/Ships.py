import copy
import pygame


class Ship:
    def __init__(self, x, y, width, height, color, name):  
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.name = name
        self.drag = False

    def place_ship(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def rotate(self, square_size):
        self.rect.width, self.rect.height = self.rect.height, self.rect.width
        max_x = 10 * square_size - self.rect.width
        max_y = 10 * square_size - self.rect.height
        self.rect.x = max(0, min(self.rect.x, max_x) + 10)
        self.rect.y = max(0, min(self.rect.y, max_y) + 10)
        
    
    def get_coordinates(self, square_size):
        start_col = round(self.rect.x / square_size)
        start_row = round(self.rect.y / square_size)
        end_col = round((self.rect.x + self.rect.width - 1) / square_size)
        end_row = round((self.rect.y + self.rect.height - 1) / square_size)
        new_coords = [(row, col) for row in range(start_row, end_row) for col in range(start_col, end_col)]
        return new_coords
    
    def move_ship(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = (mouse_pos[0]// 10) * 10
        self.rect.y = (mouse_pos[1]// 10) * 10
    
    def change_color(self, new_coords, coordinates):
        coordinates[self.name] = new_coords
        return coordinates

    def snap(self, coordinates, square_size):
        start_col, start_row = coordinates
        start = int(start_col), int(start_row)
        self.rect.x = start[0] * square_size + 10
        self.rect.y = start[1] * square_size + 10
           
    def ship_event(self, event, square_size, coordinates):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if event.button == 1:
                self.drag = True
                self.offset_width = event.pos[0] - self.rect.x
                self.offset_height = event.pos[1] - self.rect.y

            elif event.button == 3:
                self.rotate(square_size)
                new_coords = self.get_coordinates(square_size)
                self.change_color(new_coords, coordinates)
          
        
        elif event.type == pygame.MOUSEBUTTONUP and self.drag:
            if event.button == 1:
                self.drag = False
                new_coords = self.get_coordinates(square_size)

                start_col = round(self.rect.x / square_size)
                start_row = round(self.rect.y / square_size)
                self.snap((start_col, start_row), square_size)
                self.change_color(new_coords, coordinates)
                            
        elif event.type == pygame.MOUSEMOTION:
            if self.drag:
                self.rect.x = event.pos[0] - self.offset_width
                self.rect.y = event.pos[1] - self.offset_height
            
                # Beperkt de positie
                max_x = 10 * square_size - self.rect.width
                max_y = 10 * square_size - self.rect.height
                self.rect.x = max(0, min(self.rect.x, max_x) + 10)
                self.rect.y = max(0, min(self.rect.y, max_y) + 10)
        
