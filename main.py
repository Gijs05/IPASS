import Algorithm.TargetMode as Target
import Algorithm.HuntingMode as Hunting
import Game.Board as Board
import numpy as np
import copy

# def run_game(guesses, ships, grid, ship_placement):
#     sunk = True
#     count = 1
#     guess = Target.guess(grid, ships)
#     grid = Board.get_grid(guesses)
#     print(np.array(grid))
#     flat = []
#     for f in ship_placement:
#         for n in f:
#             flat.append(n)
#     while count != 100:
#         print(guess)
#         if guess in flat:
#             sunk = False
#         while sunk == False:
#             print("hit")
#             guesses[guesses.index(guess)] = "X"
#             guess = Hunting.guess(guess, Board.get_grid(guesses), guesses)
#             print(guess)
#             grid = Board.get_grid(guesses)
#             flat_grid = list(np.array(grid).flatten())
           



#         guesses[guesses.index(guess)] = "-"
#         grid = Board.get_grid(guesses)
#         guess = Target.guess(Board.get_grid(guesses), ships)
#         print(np.array(grid))
#         count += 1
#         print(count)

def run_game(grid, ships, ship_locations, guesses):
    old_ships = copy.deepcopy(ship_locations)
    guess = Target.guess(grid, ships)

    while ships != {}:
        sunk = True
        check = Board.check_hit(guess, ship_locations)
        if check:
            sunk = False

        while sunk == False:
            # print(guess, Board.check_hit(guess, ship_locations))
            guesses[guesses.index(guess)] = 'x'
            sunk, new_ships = Board.check_sink(guess, ship_locations)
            print(sunk)
            guess = Hunting.guess(guess, Board.get_grid(guesses), guesses)
            if sunk == True:
                ships = Board.remove_ship(ships, new_ships, old_ships)
                
        guesses[guesses.index(guess)] = '-'
        guess = Target.guess(Board.get_grid(guesses), ships)

custom_ship_placement = [["b2", "b3"], ["c2", "d2", "e2", "f2", "g2"], ["j7", "j8", "j9", "j10"], ["g6", "h6", "i6"]]
run_game(Board.get_grid(Board.get_guesses()), Board.get_ships(), custom_ship_placement, Board.get_guesses())

# run_game(Board.get_guesses(letters, numbers), Board.get_ships(), Board.get_grid(Board.get_guesses(letters, numbers)), Board.place_ships(Board.get_grid(Board.get_guesses(letters, numbers)), Board.get_ships()))

# custom_grid = [['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9', 'a10'], 
#                ['b1', '=', '=', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 'b10'], 
#                ['c1', '=', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9', 'c10'], 
#                ['d1', '=', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9', 'd10'], 
#                ['e1', '=', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9', 'e10'], 
#                ['f1', '=', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10'], 
#                ['g1', '=', 'g3', 'g4', 'g5', '=', 'g7', 'g8', 'g9', 'g10'], 
#                ['h1', 'h2', 'h3', 'h4', 'h5', '=', 'h7', 'h8', 'h9', 'h10'], 
#                ['i1', 'i2', 'i3', 'i4', 'i5', '=', 'i7', 'i8', 'i9', 'i10'], 
#                ['j1', 'j2', 'j3', 'j4', 'j5', 'j6', '=', '=', '=', '=']]
# custom_grid = Board.get_grid(Board.get_guesses())
# custom_ship_placement = [["b2", "b3"], ["c2", "d2", "e2", "f2", "g2"], ["j7", "j8", "j9", "j10"], ["g6", "h6", "i6"]]
# custom_guesses = Board.get_guesses()
# custom_ships = Board.get_ships()
# run_game(custom_guesses, custom_ships, custom_ship_placement)


# a = Hunting.guess('b1', custom_grid, Board.get_guesses(letters, numbers))
# print(a)
# print(np.array(custom_grid))
# Board.place_ships(Board.get_grid(Board.get_guesses(letters, numbers)), Board.get_ships())