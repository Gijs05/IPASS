import numpy as np
from collections import Counter
import Game.Board as Board

def get_surrounding(coordinate, grid):
    flat_grid = list(np.array(grid).flatten())
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    surrounding_coordinates = []
    surrounding_letters = [letters[let] for let in range(len(letters) - 1) if letters[let + 1] == coordinate[0] or letters[let - 1] == coordinate[0]]
    surrounding_numbers = [numbers[num] for num in range(len(numbers) - 1) if numbers[num + 1] == coordinate[1] or numbers[num - 1] == coordinate[1]]
    [surrounding_letters.append(int(num)) for num in surrounding_numbers]
    for coord in surrounding_letters:
        if isinstance(coord, str) and coord + coordinate[1] in flat_grid:
            surrounding_coordinates.append(coord + coordinate[1])
        if isinstance(coord, int) and coordinate[0] + str(coord) in flat_grid:
            surrounding_coordinates.append(coordinate[0] + str(coord))
    return surrounding_coordinates
    
def get_possibilities(coordinate, grid, guesses):
    flat_grid = list(np.array(grid).flatten())
    hits = [Board.get_guesses()[coord] for coord in range(len(flat_grid)) if flat_grid[coord] == 'x']
    possible = [get_surrounding(coordinate, Board.get_grid(Board.get_guesses()))]
    for possibility in hits:
        possible.append(get_surrounding(possibility, grid))
    
    flat = []
    for row in possible:
        [flat.append(coord) for coord in row]
    return flat


def guess(coordinate, grid, guesses):
    possible = get_possibilities(coordinate, grid, guesses)
    possible_array = np.array(possible)
    most_common = Counter(list(possible_array)).most_common(1)
    return most_common[0][0]
