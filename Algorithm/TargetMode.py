import numpy as np
from collections import Counter

def get_positions(grid, ships, previous):
    max_length = max(ships.values())
    positions = []
    #kijk van waar naar waar het schip geplaatst kan worden. Pak vervolgens de meest overeenkomende.
    for lst_number in range(len(grid)):
        row = grid[lst_number]
        for position in row:
            if (row.index(position) + max_length) < len(row) + 1 and all(item not in previous for item in row[row.index(position):row.index(position) + max_length]): 
                positions.append(row[row.index(position) : row.index(position) + max_length])
    flat_positions = [pos for i in positions for pos in i]
    return flat_positions

def guess(grid_colors, ships, previous):
    coords = [coord for coord in grid_colors.keys()]
    grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]

    transposed_grid = list(map(list, zip(*grid)))
    horizontal = get_positions(grid, ships, previous)
    vertical = get_positions(transposed_grid, ships, previous)
    [horizontal.append(pos) for pos in vertical]

    for coord in horizontal:
        if coord in previous:
            horizontal.remove(coord)
    most_common = Counter(horizontal).most_common(1)[0][0]
    return most_common

