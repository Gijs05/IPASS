# Kijk naar alles er om heen. Kan een schip links van het schot liggen. Zo niet dan is de kans veel minder dat het daar links zit dus kan je beter ergens ander proberen.
# Doe dit elke keer en maak dan steeds een betere gok.
# Als het een hit is ga in hunting mode. Kijk dan wat kan en ga zo verder.
import Board
import numpy as np

guesses = Board.get_guesses()
# Elke keer als er een schip zinkt haal een schip uit de dict
ships = Board.get_ships()
grid = Board.get_grid()

def get_horizontal_positions():
    max_length = max(ships.values())
    pos_hor = {}
    #kijk van waar naar waar het schip geplaatst kan worden. Pak vervolgens de meest overeenkomende.
    for lst_number in range(len(grid)):
        row_length = len(grid[lst_number])
        for position in range(row_length):
            if (position + max_length) < row_length:
                pos_hor[position] = position + max_length
    return pos_hor

def get_vertical_positions():
    max_length = max(ships.values())
    pos_ver = {}
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# Het algoritme heeft een target mode voor als er nog geen hits zijn. 
# Kijk naar de lengte van het langste schip. Probeer dan een inschatting te maken wat de beste plek is om te gokken waar de meeste mogelijkheden zouden liggen voor een hit. 
def target_mode(ships, guesses, grid):
    return get_horizontal_positions()

# Eerst horizontaal daarna verticaal


print(target_mode(ships, guesses, grid))
