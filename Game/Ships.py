import copy

def check_hit(coordinate, ship_locations):
    locations = [coord for ship in ship_locations for coord in ship]
    if str(coordinate) in locations:
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