import Board
import Algorithm.TargetMode as Target

def run_game(guesses, ships, grid):
    while guesses != []:
        guess = Target.guess(grid, ships)
        print(guess)
        guesses.remove(guess)

run_game(Board.get_guesses(), Board.get_ships(), Board.get_grid)