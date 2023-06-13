import Algorithm.TargetMode as Target
import Game.Board as Board
def run_game(guesses, ships, grid):
    count = 0
    while count != 100:
        guess = Target.guess(grid, ships)
        print(guess)
        guesses[guesses.index(guess)] = "X"
        grid = Board.get_grid(guesses)
        count += 1
        print(count)
run_game(Board.get_guesses(), Board.get_ships(), Board.get_grid(Board.get_guesses()))

