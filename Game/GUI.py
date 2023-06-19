import pygame 
import os

def get_info():
    pygame.init()

    # Get screen info
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.Info()
    screen_width, screen_height = screen.current_w, screen.current_h - 70
    window = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Battleship")

    resolution = (screen_width, screen_height)
    grid_size = 10  
    line_width = 1
    return window, resolution, grid_size, line_width

def get_square_size(resolution, grid_size, line_width):
    square_width = ((resolution[0] - 400) / grid_size) - line_width * ((grid_size + 1) / grid_size)
    square_height = (resolution[1] / grid_size) - line_width * ((grid_size + 1) / grid_size)
    return (square_width, square_height)

def conversion(column_row, width_height, line_width):
    convert = line_width * (column_row + 1) + width_height * column_row
    return convert

def draw_grid(grid_size, window, resolution, line_width, grid_color, coordinates):
    square_size = get_square_size(resolution, grid_size, line_width)
    for coordinate, color in grid_color.items():
        row, column = coordinate
        width = conversion(column, square_size[1], line_width)
        height = conversion(row, square_size[1], line_width)
        geometry = (width, height, square_size[1], square_size[1])
        pygame.draw.rect(window, color, geometry)

