import pygame

def check_hit(coordinate, grid_colors):
    """
    Checks if a coordinate represents a hit.

    Args:
        coordinate (tuple): The coordinate to check.
        grid_colors (dict): The dictionary of grid colors.

    Returns:
        bool: True if the coordinate represents a hit, False otherwise.
    """
    if grid_colors[coordinate] == (0, 0, 225) or grid_colors[coordinate] == (225, 0, 0):
        return True
    else:
        return False

def get_position(square_size):
    """
    Retrieves the grid position based on the current mouse position.

    Args:
        square_size (int): The size of each square in the grid.

    Returns:
        tuple: The coordinate of the grid position.
    """
    position = pygame.mouse.get_pos()
    column = position[0] // square_size
    row = position[1] // square_size
    return row, column

def check_mine(coordinate, grid_colors):
    """
    Checks if a coordinate is a mine on the grid.

    Args:
        coordinate (tuple): The coordinate to check.
        grid_colors (dict): The dictionary of grid colors.

    Returns:
        bool: True if the coordinate represents a mine, False otherwise.
    """
    if grid_colors[coordinate] == (0, 0, 0):
        return True
    else:
        return False
    



