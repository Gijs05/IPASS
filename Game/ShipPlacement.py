import random
import HuntingMode


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
            grid2[coord] = (225, 225, 225)

        ship_coordinates[f"ship{count}"] = ship_coords
        if "ship6" in ship_coordinates:
            ship_coordinates["mine"] = ship_coordinates["ship6"]
            del ship_coordinates["ship6"]
            grid2[ship_coordinates["mine"]] = (0, 0, 0)
            
    return ship_coordinates
