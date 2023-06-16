import numpy as np
from collections import Counter

def get_positions(grid, ships):
    max_length = max(ships.values())
    positions = []
    #kijk van waar naar waar het schip geplaatst kan worden. Pak vervolgens de meest overeenkomende.
    for lst_number in range(len(grid)):
        row = grid[lst_number]
        for position in row:
            if (row.index(position) + max_length) < len(row) and '-' not in row[row.index(position) : row.index(position) + max_length]: #or 'x' not in row[row.index(position) : row.index(position) + max_length]:
                positions.append(row[row.index(position) : row.index(position) + max_length])
    return positions

def guess(grid, ships, previous):
    transposed_grid = np.array(grid).T
    reversed_grid = [list(row) for row in transposed_grid]
    horizontal = get_positions(grid, ships)
    vertical = get_positions(reversed_grid, ships)
    [horizontal.append(pos) for pos in vertical]

    flat = list(np.array(horizontal).flatten())
    for coord in flat:
        if coord in previous:
            flat.remove(coord)

    most_common = Counter(list(np.array(flat))).most_common(1)
    return most_common[0][0]
