from collections import Counter
import random

def get_positions(grid, ships, previous):
    """
    Retrieves valid positions to get guesses.

    Args:
        grid (list): A list representing the game grid.
        ships (dict): A dictionary containing the information about the ships.
        previous (list): A list of previously occupied positions.

    Returns:
        list: A list of valid positions to get guesses.

    """
    ship_values = [len(value) for value in ships.values()]
    max_length = max(ship_values)
    positions = []
    for lst_number in range(len(grid)):
        row = grid[lst_number]
        for position in row:
            if (row.index(position) + max_length) < len(row) + 1 and all(item not in previous for item in row[row.index(position):row.index(position) + max_length]) and\
                (225, 0, 0) not in row[row.index(position):row.index(position) + max_length]: 
                positions.append(row[row.index(position) : row.index(position) + max_length])
    flat_positions = [pos for i in positions for pos in i]
    return flat_positions

def guess(grid_colors, ships, previous):
    """
    Selects a position to guess based on the other guesses.

    Args:
        grid_colors (dict): A dictionary representing the colors of each position on the game grid.
        ships (dict): A dictionary containing the information about the ships on the grid.
        previous (list): A list of previously guessed positions.

    Returns:
        tuple: Coordinates of the guess and an updated version of previous.

    """
    coords = [coord for coord in grid_colors.keys()]
    grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]

    transposed_grid = list(map(list, zip(*grid)))
    horizontal = get_positions(grid, ships, previous)
    vertical = get_positions(transposed_grid, ships, previous)
    [horizontal.append(pos) for pos in vertical]

    for coord in horizontal:
        if coord in previous:
            horizontal.remove(coord)
    most_common = Counter(horizontal)
    max_value = max(most_common.values())
    guess = random.choice([(coord, value) for coord, value in most_common.items() if value == max_value])
    previous.append(guess[0])
    return guess[0], previous


