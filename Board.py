#board is 10x10. abcdefghij
# Board samenstelling  10x10
import numpy as np

def get_guesses():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    possible_guesses = [letter + number for letter in letters for number in numbers]
    return possible_guesses

def get_ships():
    ships = {"ship1" : 5, 
            "ship2" : 4, 
            "ship3" : 3,
            "ship4" : 3,
            "ship5" : 2}
    return ships

def get_grid():
    grid = []
    for _ in range(10):
        grid.append([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return np.array(grid)
