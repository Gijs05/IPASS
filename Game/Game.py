import pygame 
import GUI
from Button import Button
from Ships import Ship
from Scanner import Scanner
from Label import Label
import Grid
import ShipPlacement
import Modes

def on_screen():
    window, resolution, grid_size, line_width = GUI.get_info()
    square_size = GUI.get_square_size(resolution, grid_size, line_width)[0]
    test_text = Label(square_size * 10 + (square_size / 2), square_size * 6, (75, 75, 75), "test text")
    button = Button(50, 50, 150, 50, (100, 100, 100), "start game")
    scanner = Scanner(square_size * 12, square_size * 5, square_size, square_size, (0, 200, 0))
    mine = Ship(square_size * 5 + 6, square_size * 5 + 5, square_size, square_size, (0, 0, 0), "mine")
 
    ship1 = Ship(0, square_size * 2,  square_size * 5, square_size, (0, 0, 225), "ship1")
    ship2 = Ship(0, square_size * 4 + 1,  (square_size + 1) * 4, square_size + 1, (0, 0, 225), "ship2")
    ship3 = Ship(0, square_size * 6 + 5,  (square_size + 1) * 3, square_size + 1, (0, 0, 225), "ship3")
    ship4 = Ship(0, square_size * 8 + 6,  (square_size + 1) * 3, square_size + 1, (0, 0, 225), "ship4")
    ship5 = Ship(0, square_size * 10 + 8,  (square_size + 1) * 2, square_size + 1, (0, 0, 225), "ship5")
    return (window, resolution, grid_size, line_width, square_size), (test_text, button, scanner, mine, ship1, ship2, ship3, ship4, ship5)

def end_game():
    print()

def Human(event, square_size, second_grid, button, grid_colors, human_previous):
    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = Grid.get_position(square_size)
            if event.button == 1 and button.start == True and pos in second_grid:
                if pos in second_grid and turn == True:                   
                    if Grid.check_hit(pos, grid_colors):
                        grid_colors[pos] = (225, 0, 0)
                        old_ships_human, sink , end = Modes.remove_ships(old_ships_human, pos)
                        if end:
                            turn = True
                            end_game()
                    else:
                        grid_colors[pos] = (225, 225, 225)
                    human_previous.append(pos)
                turn = False
    return human_previous, turn, grid_colors

def start_game():
    human_previous = []
    alg_previous = []
    possible = []
    result = False
    turn = True
    turn_count = 0

    coordinates = {}
    grid_colors = {}

    window, resolution, grid_size, line_width, square_size = on_screen()[0]
    test_text, button, scanner, mine, ship1, ship2, ship3, ship4, ship5 = on_screen()[1]

    second_grid = {(col, row): (50, 50, 50) for row in range(11, 21) for col in range(grid_size[1])}
    ships = [ship1, ship2, ship3, ship4, ship5]
    old_ships_alg = coordinates
    old_ships_human = ShipPlacement.Ship_placement(second_grid)

    while True:
        for event in pygame.event.get():
            Human(event, square_size, second_grid, button, grid_colors, human_previous)
                    
                    # if len(alg_previous) != 0:
                    #     result = Grid.check_hit(alg_previous[-1], grid_colors)
                    #     if grid_colors[alg_previous[-1]] == (225, 225, 0):
                    #         grid_colors[alg_previous[-1]] = (225, 225, 225)
                    #         turn = True

                # if turn == False:
                #     guess = choose_mode(result, grid_colors, coordinates, alg_previous, possible)
                #     possible = guess[1]
                #     guess_coord = guess[0]
                    
                #     if Grid.check_hit(guess_coord, grid_colors):
                #         grid_colors[guess_coord] = (225, 0, 0)
                #         new_ships = remove_ships(old_ships, guess_coord)
                #         old_ships = new_ships[0]
           
                #     elif Grid.check_mine(guess_coord, grid_colors):
                #         grid_colors[guess_coord] = (225, 225, 0)
                #         # creeer een message voor turn overslaan

                #     else:
                #         grid_colors[guess_coord] = (225, 225, 225)

                #     possible = [i for i in possible if i not in alg_previous]
                #     alg_previous.append(guess_coord)
                #     turn = True
                #     print(guess_coord)
                     
        window.fill((225,225,225))  
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)

        mine.ship_event(event, square_size, coordinates)
        button.button_event(event, ships, coordinates)
        
        for ship in ships:
            ship.ship_event(event, square_size, coordinates)
        
        button.place_button(window)
        test_text.place_label()

        if button.start == False:
            for ship in ships:
                ship.place_ship(window)
            mine.place_ship(window)

            grid_colors = {(col, row): (50, 50, 50) for row in range(21) for col in range(grid_size[1])}
            for coordinate in grid_colors.keys():
                if coordinate[1] == 11 or 0 <= coordinate[0] <= 1:
                    grid_colors[coordinate] = (225, 225, 225)

            for name, coordinate in coordinates.items():
                for coord in coordinate:
                    if name == "mine":
                        grid_colors[coord] = (0, 0, 0)
                    else:
                        grid_colors[coord] = (0, 0, 225)
        pygame.display.flip()  
start_game()