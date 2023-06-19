import numpy as np
from collections import Counter

grid_colors = {(col, row): (50, 50, 50) for row in range(10) for col in range(10)}
previous = [(4, 4)]
# grid_colors[(4, 6)] = (225, 0, 0)

def get_surrounding(coordinate, grid):
    surrounding_hor = [row[coord] for row in grid for coord in range(len(row) - 1) if row[coord - 1] == coordinate or row[coord + 1] == coordinate]
   
    surrounding_ver = [collumn[coord] for collumn in list(map(list, zip(*grid))) for coord in range(len(list(collumn)) - 1) if list(collumn)[coord - 1] == coordinate or list(collumn)[coord + 1] == coordinate]
    surrounding_coordinates = [coord for coordinates in [surrounding_hor, surrounding_ver] for coord in coordinates]

    viable_coordinates = [surround for surround in surrounding_coordinates for coord in grid if surround in coord]
    return viable_coordinates
    
def get_possibilities(coordinate, grid, grid_colors):
    hits = [coord for row in grid for coord in row if grid_colors[coord] == (225, 0, 0)]
    possible = [get_surrounding(coordinate, grid)]
    for possibility in hits:
        possible.append(get_surrounding(possibility, grid))

    flat = []
    for row in possible:
        [flat.append(coord) for coord in row]
    return flat


def guess(previous, grid_colors, coordinate):
    coords = [coord for coord in grid_colors.keys()]
    grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]
    possible = get_possibilities(coordinate, grid, grid_colors)
    possible.remove(previous[-1]) 

    print(possible)
    most_common = Counter(possible).most_common(1)[0][0]
    return most_common, possible


coords = [coord for coord in grid_colors.keys()]
grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]

print(guess(previous, grid_colors, (4, 5)))


