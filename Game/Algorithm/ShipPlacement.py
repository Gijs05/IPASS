import random
import Algorithm.HuntingMode as HuntingMode

def surrounding(grid, coordinate, ship_length):
    possible = HuntingMode.get_all_possibilities(coordinate, grid)
    ship_coords = []
    for row in possible[0].values():
        if ship_length <= len(row):
            ship_coords = row[:ship_length]
            break
    return ship_coords

def Ship_placement(grid2):
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
