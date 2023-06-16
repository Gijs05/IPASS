import numpy as np
from collections import Counter
import Game.Board as Board

def get_surrounding(coordinate, grid):
    surrounding_hor = [row[coord] for row in grid for coord in range(len(row) - 1) if row[coord - 1] == coordinate or row[coord + 1] == coordinate]
    surrounding_ver = [collumn[coord] for collumn in np.array(grid).T for coord in range(len(list(collumn)) - 1) if list(collumn)[coord - 1] == coordinate or list(collumn)[coord + 1] == coordinate]
    surrounding_coordinates = [coord for coordinates in [surrounding_hor, surrounding_ver] for coord in coordinates]

    viable_coordinates = []
    for i in surrounding_coordinates:
        for x in grid:
            if i in x:
                viable_coordinates.append(i)
    return viable_coordinates
    
def get_possibilities(coordinate, grid):
    flat_grid = list(np.array(grid).flatten())
    hits = [Board.get_guesses()[coord] for coord in range(len(flat_grid)) if flat_grid[coord] == 'x']
    possible = [get_surrounding(coordinate, Board.get_grid(Board.get_guesses()))]
    for possibility in hits:
        possible.append(get_surrounding(possibility, grid))
     
    flat = []
    for row in possible:
        [flat.append(coord) for coord in row]
    return flat


def guess(possible, previous):
    new_possible = []
    for coord in possible:
        if coord not in previous:
            new_possible.append(coord)
    most_common = Counter(list(np.array(new_possible))).most_common(1)        
    return most_common[0][0]
