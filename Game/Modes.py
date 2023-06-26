
# Kijk naar alles er om heen. Kan een schip links van het schot liggen. Zo niet dan is de kans veel minder dat het daar links zit dus kan je beter ergens ander proberen.
# Doe dit elke keer en maak dan steeds een betere gok.
# Als het een hit is ga in hunting mode. Kijk dan wat kan en ga zo verder.
# Het algoritme heeft een target mode voor als het geen hit is. 
# Kijk naar de lengte van het langste schip. Probeer dan een inschatting te maken wat de beste plek is om te gokken waar de meeste mogelijkheden zouden liggen voor een hit. 
# Elke keer als er een schip zinkt haal een schip uit de dict

import TargetMode as Target
import HuntingMode as Hunting
import copy

POSSIBLE = None
ORIGINAL_WAY = None
RESERVE_WAY = None
INDEX = None
HIT = False
SINKING = False
PREVIOUS = []

def choose_mode(result, grid_colors, previous, ships):
    if result or SINKING:
        SINKING = True
        if HIT == False:
            POSSIBLE = Hunting.get_all_possibilities(previous[-1], grid_colors)
            HIT = True
            max_value = len(max(POSSIBLE[0].values()))

            for name, value in POSSIBLE[0].items():
                if len(value) == max_value:
                    if name[0] == 0:
                        ORIGINAL_WAY = POSSIBLE[1]
                        RESERVE_WAY = POSSIBLE[2]
                    elif name[1] == 0:
                        ORIGINAL_WAY = POSSIBLE[2]
                        RESERVE_WAY = POSSIBLE[1]
        guess_info = Hunting.guess(ORIGINAL_WAY, RESERVE_WAY, INDEX, previous, result)  
        guess, ORIGINAL_WAY, previous, INDEX = guess_info
        return guess, previous
    
    elif SINKING == False:
       return Target.guess(grid_colors, ships, previous)  

def remove_ships(old_ships, coordinate):
    sink = False
    copy_ships = copy.deepcopy(old_ships)
    for name, coordinates in old_ships.items():
        if coordinate in coordinates:
            coordinates.remove(coordinate)
            old_ships[name] = coordinates
    
    for name in old_ships.keys():
        if len(copy_ships[name]) != len(old_ships[name]) and len(old_ships[name]) == 0:
            sink = True
    for ending in old_ships.values():
        if len(ending) != 0:
            end = False
            break
        else:
            end = True
    return old_ships, sink, end
