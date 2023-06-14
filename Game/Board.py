# Board samenstelling  10x10
import numpy as np
import copy

def get_guesses():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    possible_guesses = [letter + number for letter in letters for number in numbers]
    return possible_guesses

# Create the ships with the length of the ship
def get_ships():
    ships = {"ship1" : 5, 
            "ship2" : 4, 
            "ship3" : 3,
            "ship4" : 3,
            "ship5" : 2}
    return ships

def get_grid(guesses):
    all_guesses = np.array(guesses)
    coords = all_guesses.reshape(10,10)
    grid = [list(row) for row in coords]
    return grid

def place_ships(grid, ships):
    ship_placements = []
    custom_grid = grid
    for ship in ships.values():  
        # hor = input("hor or ver ")
        placement1 = input(f"place ship: {ship} begin ")
        placement2 = input("end ")
        # if hor == "ver":
        #     transposed_grid = np.array(grid).T
        #     grid = [list(row) for row in transposed_grid]

        for i in grid:
            sh = []
            if placement1 in i:
                for x in range(i.index(placement1), i.index(placement2) + 1):
                    sh.append(i[x])
                    grid[grid.index(i)][x] = '='
            ship_placements.append(sh)
        grid = custom_grid
    return grid, ship_placements

def check_hit(coordinate, ship_locations):
    locations = [coord for ship in ship_locations for coord in ship]
    if coordinate in locations:
        return True
    return False

def check_sink(coordinate, ship_locations):
    old_ships = copy.deepcopy(ship_locations)
    if check_hit(coordinate, ship_locations):
        for ships in ship_locations:
            if coordinate in ships:
                ships.remove(coordinate) 

    for i in range(len(old_ships)):
        if len(ship_locations[i]) < len(old_ships[i]) and len(ship_locations[i]) == 0:
            return True, ship_locations
    return False, ship_locations
    
def remove_ship(ships, new_locations, old_locations):
        for loc in range(len(new_locations)):
            if len(new_locations[loc]) == 0:
                length_ship = len(old_locations[loc])
                for key, length in ships.items():
                    if length == length_ship:
                        del ships[key]
                        break
        return ships
