import Algorithm.TargetMode as Target
import Algorithm.HuntingMode as Hunting
import Game.Board as Board
import Game.Ships as Ship
import numpy as np
import copy

def run_game(grid, ships, ship_locations, guesses):
    old_ships = copy.deepcopy(ship_locations)
    previous_guesses = []
    guess = Target.guess(grid, ships, previous_guesses)
    count = 0
    while ships != {}:
        possible = []
        previous_guesses.append(guess)
        print(guess)
        sunk = True
        check = Ship.check_hit(guess, ship_locations)
        if check:
            sunk = False

        while sunk == False and ships != {}:
            print(f"g: {guess}, {count}")
            

            if guess in possible:
                possible.remove(guess)
            
            if Ship.check_hit(guess, ship_locations):
                possible = [possible, Hunting.get_possibilities(guess, Board.get_grid(guesses))]
                possible = [coord for x in possible for coord in x]
                guesses[guesses.index(guess)] = 'x'
                
            else: 
                guesses[guesses.index(guess)] = '-'
                
            
            sunk, new_ships = Ship.check_sink(guess, ship_locations)    
            if sunk == True:
                ships = Ship.remove_ship(ships, new_ships, old_ships)

            guess = Hunting.guess(possible, previous_guesses)
            previous_guesses.append(guess)
            count += 1
            
        guesses[guesses.index(guess)] = '-'
        guess = Target.guess(Board.get_grid(guesses), ships, previous_guesses)
        print(np.array(Board.get_grid(guesses)))
        print(ships)
    
      
    
custom_ship_placement = [["i6", "i7"], ["e1", "e2", "e3"], ["f4", "f5", "f6", "f7"], ["d7", "d8", "d9"], ["a10", "b10", "c10", "d10", "e10"]]
run_game(Board.get_grid(Board.get_guesses()), Board.get_ships(), custom_ship_placement, Board.get_guesses())

