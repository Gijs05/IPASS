
# Kijk naar alles er om heen. Kan een schip links van het schot liggen. Zo niet dan is de kans veel minder dat het daar links zit dus kan je beter ergens ander proberen.
# Doe dit elke keer en maak dan steeds een betere gok.
# Als het een hit is ga in hunting mode. Kijk dan wat kan en ga zo verder.
# Het algoritme heeft een target mode voor als het geen hit is. 
# Kijk naar de lengte van het langste schip. Probeer dan een inschatting te maken wat de beste plek is om te gokken waar de meeste mogelijkheden zouden liggen voor een hit. 
# Elke keer als er een schip zinkt haal een schip uit de dict

import HuntingMode as Hunting
import TargetMode as Target

def choose_mode(result, grid_colors, ships, previous):
    sinking = False
    if result:
        sinking = True

    if sinking:
       return Hunting.guess(previous, grid_colors, previous[-1])
    
    elif sinking == False:
       return Target.guess(grid_colors, ships, previous)
    
grid_colors = {(col, row): (50, 50, 50) for row in range(10) for col in range(10)}
grid_colors[(4, 4)] = (225, 0, 0)
ships = {"ship1" : 5, 
            "ship2" : 4, 
            "ship3" : 3,
            "ship4" : 3,
            "ship5" : 2}
print(choose_mode(True, grid_colors, ships, [(4, 4)]))
    
