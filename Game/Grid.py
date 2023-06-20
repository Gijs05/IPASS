import pygame

def check_hit(coordinate, grid_colors):
    if grid_colors[coordinate] == (0, 0, 225):
        return True
    else:
        return False

def draw_cross(window, coordinate):
    pygame.draw.line(window, (0, 0, 0), coordinate, (coordinate[0] + 10, coordinate[1] + 100), 2)
    pygame.draw.line(window, (0, 0, 0), (coordinate[0], coordinate[1] + 10), (coordinate[0] + 10, coordinate[1]), 2)

def get_position(square_size):
    position = pygame.mouse.get_pos()
    column = position[0] // square_size
    row = position[1] // square_size
    return row, column

