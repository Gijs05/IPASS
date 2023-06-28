def get_surrounding(coordinate, grid):
    """
    Retrieves the viable surrounding coordinates for a given coordinate.

    Args:
        coordinate (tuple): The coordinate for which surrounding positions will be retrieved.
        grid (list): A list representing the game grid.

    Returns:
        list: A list of viable surrounding coordinates.

    """
    surrounding_hor = [row[coord] for row in grid for coord in range(len(row) - 1) if row[coord - 1] == coordinate and coord - 1 != - 1 or row[coord + 1] == coordinate]  
    surrounding_ver = [row[coord] for row in list(map(list, zip(*grid))) for coord in range(len(row) - 1) if row[coord - 1] == coordinate and coord - 1 != - 1 or row[coord + 1] == coordinate] 

    surrounding_coordinates = [coord for coordinates in [surrounding_hor, surrounding_ver] for coord in coordinates]
    viable_coordinates = [coord for coord in surrounding_coordinates for row in grid if coord in row]
    return viable_coordinates

def get_options(coordinate, grid):
    """
    Retrieves the available options around a coordinate.

    Args:
        coordinate (tuple): The coordinate for which options will be retrieved.
        grid (list): A list representing the game grid.

    Returns:
        dict: A dictionary of available options, where the keys represent the direction of the option
              (0, 1) for right, (0, -1) for left, (1, 0) for down, and (-1, 0) for up.

    """
    surrounding = get_surrounding(coordinate, grid)
    ways = [(coord[0] - coordinate[0], coord[1] - coordinate[1]) for coord in surrounding]

    sides = {}
    for option in ways:
        if option[0] != 0 and option[1] != 0:
            continue
        public_index = ways.index(option)
        if option[0] < 0:
            sides[option] = surrounding[public_index]
        elif option[1] < 0:
            sides[option] = surrounding[public_index]
        elif option[0] > 0:
            sides[option] = surrounding[public_index]
        elif option[1] > 0:
            sides[option] = surrounding[public_index]
    return sides

def get_possibility(side, grid):
    """
    Retrieves the possible coordinates along a given side in the grid.

    Args:
        side (tuple): A tuple representing the side, where the first element is the direction
                      and the second element is the starting coordinate.
        grid (dict): A dictionary representing the grid, where the keys are the coordinates and the values
                     are the corresponding colors.

    Returns:
        list: A list of possible coordinates along the given side.

    """
    x,y = side[1]
    possible_ways = []
    possible_ways.append((x, y))
    while (x,y) in grid:
        x += side[0][0]
        y += side[0][1]
        possible_ways.append((x, y))
    return possible_ways

def get_all_possibilities(coordinate, grid_colors):
    """
    Retrieves all possible coordinate possibilities for moving from the given coordinate in the grid.

    Args:
        coordinate (tuple): The coordinate from which the possibilities will be determined.
        grid_colors (dict): A dictionary representing the grid, where the keys are the coordinates
                            and the values are the corresponding colors.

    Returns:
        tuple: A tuple containing three elements:
            - A dictionary of all coordinate possibilities, where the keys represent the side
              and the values represent the corresponding coordinates.
            - A list of vertical coordinate possibilities.
            - A list of horizontal coordinate possibilities.

    """
    coords = [coord for coord in grid_colors.keys()]
    grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]
 
    options = get_options(coordinate, grid)
    all_coords = {i[0]: get_possibility(i, grid_colors) for i in options.items()}
    for row in all_coords.values():
        for coord in row:
            if coord not in grid_colors or grid_colors[coord] == (225,0,0):
                row.remove(coord)
            elif grid_colors[coord] == (225, 225, 225):
                del row[row.index(coord):]
    ver = [row for name, row in all_coords.items() if name[1] != 0]
    hor = [row for name, row in all_coords.items() if name[1] == 0]
    return all_coords, ver, hor

def guess(possibilities, reserve, index, previous, result):
    """
    Makes a guess based on the given possibilities.

    Args:
        possibilities (list): A list of possible guesses. 
        reserve (list): A backup list of possibilities to revert to if the current list becomes empty.
        index (int): The current index used for selecting a guess from the possibilities list.
        previous (list): A list of previously guessed coordinates.
        result (bool): The result of the previous guess. 

    Returns:
        tuple: A tuple containing the following elements:
            - guess (tuple): The selected guess coordinate.
            - possibilities (list): The updated list of possibilities after making the guess.
            - previous (list): The updated list of previously guessed coordinates.
            - index (int): The updated index for selecting the next guess.
    """
    possibilities = [row for row in possibilities if len(row) != 0]
    if index == None:
        max_value = max(possibilities)
        index = possibilities.index(max_value)  
    
    elif result == False:
        if len(possibilities) >= index + 1:
            possibilities.pop(index)
        if len(possibilities) == 0:
            possibilities = reserve
            max_value = max(possibilities)
            index = possibilities.index(max_value)
        
        else:
            index = 0
    if len(possibilities) <= index + 1:
        index = 0

    guess = possibilities[index][0]
    possibilities[index].remove(guess)
    previous.append(guess)
    return guess, possibilities, previous, index
