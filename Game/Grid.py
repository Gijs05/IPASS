import pygame

def check_hit(coordinate, grid_colors):
    if grid_colors[coordinate] == (0, 0, 225) or grid_colors[coordinate] == (225, 0, 0):
        return True
    else:
        return False

def get_position(square_size):
    position = pygame.mouse.get_pos()
    column = position[0] // square_size
    row = position[1] // square_size
    return row, column

def check_mine(coordinate, grid_colors):
    if grid_colors[coordinate] == (0, 0, 0):
        return True
    else:
        return False


