import random
import Algorithm.HuntingMode as HuntingMode

def surrounding(grid, coordinate, ship_length):
    """
    Finds the surrounding coordinates for placing a ship.

    Args:
        grid (dict): A dictionary representing the game grid.
        coordinate (tuple): The coordinate around which the ship will be placed.
        ship_length (int): The length of the ship to be placed.

    Returns:
        list: A list of coordinates representing the surrounding positions for placing the ship.

    """
    possible = HuntingMode.get_all_possibilities(coordinate, grid)
    ship_coords = []
    for row in possible[0].values():
        if ship_length <= len(row):
            ship_coords = row[:ship_length]
            break
    return ship_coords

def Ship_placement(grid2):
    """
    Places ships of various lengths on the game grid in random positions.

    Args:
        grid2 (dict): A dictionary representing the game grid.

    Returns:
        tuple: A tuple containing the ship coordinates and an updated second grid.

    """
    ship_length = [5, 4, 3, 3, 2, 1]
    ship_coordinates = {}
    
    for count in range(1, 7):
        coordinate = random.choice(list(grid2.keys()))
        ship_coords = surrounding(grid2, coordinate, ship_length[0])
        ship_length.pop(0)
        for coord in ship_coords:
            grid2[coord] = (0, 0, 225)

        ship_coordinates[f"ship{count}"] = ship_coords
    return ship_coordinates, grid2