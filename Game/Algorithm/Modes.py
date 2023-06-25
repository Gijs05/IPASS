
# Kijk naar alles er om heen. Kan een schip links van het schot liggen. Zo niet dan is de kans veel minder dat het daar links zit dus kan je beter ergens ander proberen.
# Doe dit elke keer en maak dan steeds een betere gok.
# Als het een hit is ga in hunting mode. Kijk dan wat kan en ga zo verder.
# Het algoritme heeft een target mode voor als het geen hit is. 
# Kijk naar de lengte van het langste schip. Probeer dan een inschatting te maken wat de beste plek is om te gokken waar de meeste mogelijkheden zouden liggen voor een hit. 
# Elke keer als er een schip zinkt haal een schip uit de dict

import HuntingMode
import TargetMode
import copy

POSSIBLE = None
PREVIOUS_WAY = None
HIT = False
SINKING = False

def choose_mode(result, grid_colors, ships, previous):
    global POSSIBLE, HIT, SINKING

    if result or SINKING:
        SINKING = True
        if HIT == False:
            POSSIBLE = HuntingMode.get_all_possibilities(previous[-1], grid_colors)
            HIT = True
        print(POSSIBLE)
        # if result:
        #     HuntingMode.guess(POSSIBLE)

        


    # if sinking:
    #    if result:
    #         new_guess = HuntingMode.guess(previous, grid_colors, result, possible)
    #         new_possible = new_guess[1]
    #         [possible.append(new) for new in new_possible]
    #         return new_guess[0], possible
       
    #    else:
    #        new_guess = HuntingMode.guess(previous, grid_colors, result, possible)
    #        return new_guess[0], new_guess[1]

    elif SINKING == False:
       return TargetMode.guess(grid_colors, ships, previous)

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
    return old_ships, sink

