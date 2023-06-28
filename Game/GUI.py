import pygame 
import os

def get_info():
    """
    Retrieves information about the game window.

    Returns:
        tuple: The game window, resolution, grid size, and line width.
    """
    pygame.init()

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    screen = pygame.display.Info()
    screen_width, screen_height = screen.current_w, screen.current_h - 50
    window = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Battleship")

    resolution = (screen_width, screen_height)
    grid_size = (21, 12)  
    line_width = 1
    return window, resolution, grid_size, line_width

def get_square_size(resolution, grid_size, line_width):
    """
    Calculates the size of the squares in the grid.

    Args:
        resolution (tuple): The resolution of the game window.
        grid_size (tuple): The size of the grid.
        line_width (int): The width of the grid lines.

    Returns:
        tuple: The width and height of the squares in the grid.
    """
    square_width = (resolution[0] / grid_size[0]) - line_width * ((grid_size[0] + 1) / grid_size[0])
    square_height = (resolution[1] / grid_size[1]) - line_width * ((grid_size[1] + 1) / grid_size[1])
    return (square_width, square_height)

def conversion(column_row, width_height, line_width):
    """
    Converts grid column or row to pixel coordinate.

    Args:
        column_row (int): The grid column or row.
        width_height (float): The width or height of each square in the grid.
        line_width (int): The width of the grid lines.

    Returns:
        float: The pixel coordinate.
    """
    convert = line_width * (column_row + 1) + width_height * column_row
    return convert

def draw_grid(grid_size, window, resolution, line_width, grid_color):
    """
    Draws the grid on the game window.

    Args:
        grid_size (tuple): The size of the grid.
        window: The game window surface.
        resolution (tuple): The resolution of the game window.
        line_width (int): The width of the grid lines.
        grid_color (dict): The dictionary of grid colors.
    """
    square_size = get_square_size(resolution, grid_size, line_width)
    for coordinate, color in grid_color.items():
        row, column = coordinate
        width = conversion(column, square_size[0], line_width)
        height = conversion(row, square_size[1], line_width)
        geometry = (width, height, square_size[0], square_size[1])
        pygame.draw.rect(window, color, geometry)

