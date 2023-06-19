import copy
import pygame


class Ship:
    def __init__(self, x, y, width, height, color):  
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.drag = False

    def place_ship(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def rotate(self):
        self.rect.width, self.rect.height = self.rect.height, self.rect.width

    def move_ship(self):
        mouse_pos = pygame.mouse.get_pos()
        self.rect.x = (mouse_pos[0]// 10) * 10
        self.rect.y = (mouse_pos[1]// 10) * 10
                    
    def ship_event(self, event, square_size):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos):
            if event.button == 1:
                self.drag = True
                self.offset_width = event.pos[0] - self.rect.x
                self.offset_height = event.pos[1] - self.rect.y

            elif event.button == 3:
                self.rotate()
        
        # elif event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1 and self.drag == True:
        #         self.drag = False
        #         self.move_ship()
          
        
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.drag = False
                start_col = int(self.rect.x // square_size)
                start_row = int(self.rect.y // square_size)
                end_col = int((self.rect.x + self.rect.width - 1) // square_size)
                end_row = int((self.rect.y + self.rect.height - 1) // square_size)

                coordinates = []
                for row in range(start_row, end_row + 1):
                    for col in range(start_col, end_col + 1):
                        coordinates.append((col, row))
                
                            
        elif event.type == pygame.MOUSEMOTION:
            if self.drag:
                self.rect.x = event.pos[0] - self.offset_width
                self.rect.y = event.pos[1] - self.offset_height
            
                # Beperkt de positie
                max_x = 10 * square_size - self.rect.width
                max_y = 10 * square_size - self.rect.height
                self.rect.x = max(0, min(self.rect.x, max_x) + 10)
                self.rect.y = max(0, min(self.rect.y, max_y) + 10)
        
def check_hit(coordinate, ship_locations):
    locations = [coord for ship in ship_locations for coord in ship]
    if str(coordinate) in locations:
        return True
    return False

def check_sink(coordinate, ship_locations):
    old_ships = copy.deepcopy(ship_locations)

    if check_hit(coordinate, ship_locations):
        for ships in ship_locations:
            if coordinate in ships:
                ships.remove(coordinate) 

    for i in range(len(old_ships)):
        if len(ship_locations[i]) < len(old_ships[i]) and len(ship_locations[i]) == 0:
            return True, ship_locations
    return False, ship_locations
    
def remove_ship(ships, new_locations, old_locations):
    for loc in range(len(new_locations)):
        if len(new_locations[loc]) == 0:
            length_ship = len(old_locations[loc])
            for key, length in ships.items():
                if length == length_ship:
                    del ships[key]
                    break
    return ships