import pygame 
import GUI
from Button import Button
from Ships import Ship
from Scanner import Scanner
from Label import Label
import Grid
import Algorithm.ShipPlacement as ShipPlacement
import Algorithm.Modes as Modes

def on_screen():
    window, resolution, grid_size, line_width = GUI.get_info()
    square_size = GUI.get_square_size(resolution, grid_size, line_width)[0]
    test_text = Label(square_size * 10 + (square_size / 2), square_size * 6, (75, 75, 75), "test text")
    start_button = Button(square_size * 9, 0, 150, 50, (100, 100, 100), "start game")
    reset_button = Button(square_size * 12, 0, 150, 50, (100, 100, 100), "reset game")

    scanner = Scanner(square_size * 12, square_size * 5, square_size, square_size, (0, 200, 0))
    mine = Ship(square_size * 5 + 6, square_size * 5 + 5, square_size, square_size, (0, 0, 0), "mine")
 
    ship1 = Ship(0, square_size,   square_size * 5, square_size, (0, 0, 225), "ship1")
    ship2 = Ship(0, square_size * 3 + 1,  (square_size + 1) * 4, square_size + 1, (0, 0, 225), "ship2")
    ship3 = Ship(0, square_size * 5 + 5,  (square_size + 1) * 3, square_size + 1, (0, 0, 225), "ship3")
    ship4 = Ship(0, square_size * 7 + 6,  (square_size + 1) * 3, square_size + 1, (0, 0, 225), "ship4")
    ship5 = Ship(0, square_size * 9 + 8,  (square_size + 1) * 2, square_size + 1, (0, 0, 225), "ship5")
    return (window, resolution, grid_size, line_width, square_size), (test_text, start_button, reset_button, scanner, mine, ship1, ship2, ship3, ship4, ship5)

def end_game(reset_button, event, ships, coordinates, grid_size, window, resolution, line_width, grid_colors):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), quit()
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)
        reset_button.button_event(event, ships, coordinates)                
        pygame.display.flip()         
        print("test")

def Human(grid_colors, grid2, previous, turn, pos, human_ships, alg_mine, alg_previous):
    if pos not in previous:
        previous.append(pos)
        if pos in grid2 and turn == True:         
            if Grid.check_hit(pos, grid2):
                grid_colors[pos] = (225, 0, 0)
                human_ships, _, end = Modes.remove_ships(human_ships, pos)
                if end:
                    end_game()
            else:
                grid_colors[pos] = (225, 225, 225)

            if pos == alg_mine:
                grid_colors[pos] = (0, 0, 0)
    turn = False
    # if len(alg_previous) != 0 and grid_colors[alg_previous[-1]] == (0, 0, 0):
    #     turn = True
    return previous, turn, grid_colors, grid2, human_ships

def Algorithm(var_modes, coordinates, grid_colors, grid2, human_previous, alg_previous, alg_ships, result):
    grid1 = {coord: value for coord, value in grid_colors.items() if coord[0] < 10 and coord[1] < 10}
    if len(alg_previous) == 0:
        guess_data, var_modes = Modes.choose_mode(False, grid1, alg_previous, coordinates, var_modes)
        guess, alg_previous = guess_data

    else:
        guess_data, var_modes = Modes.choose_mode(result, grid1, alg_previous, coordinates, var_modes)   
        guess, alg_previous = guess_data
        result = Grid.check_hit(guess, grid_colors)
    alg_ships, sink, end = Modes.remove_ships(alg_ships, guess)
    grid_colors = change_color(guess, grid_colors)
    turn = True
    if grid2[human_previous[-1]] == (0,0,0):
        turn = False
   
    if sink:
        var_modes = {"possible": None, "original_way": None, "reserve_way": None, "index": None, "hit": False, "sinking": False, "hits": None}
        result = False
  
    if end:
        end_game()
    return var_modes, alg_previous, turn, alg_ships, result

def change_color(coordinate, grid):
    if Grid.check_hit(coordinate, grid):
        grid[coordinate] = (225, 0, 0)
    elif Grid.check_mine(coordinate, grid):
        grid[coordinate] = (0, 0, 0)
    else:
        grid[coordinate] = (225, 225, 225)
    return grid

def start_game():
    human_previous = []
    alg_previous = []
    turn = True
    result = False
    turn_count = 0

    coordinates = {}
    grid_colors = {}

    window, resolution, grid_size, line_width, square_size = on_screen()[0]
    test_text, start_button, reset_button, scanner, mine, ship1, ship2, ship3, ship4, ship5 = on_screen()[1]

    var_modes = {"possible": None, "original_way": None, "reserve_way": None, "index": None, "hit": False, "sinking": False, "hits": None}
    grid2 = {(col, row): (50, 50, 50) for row in range(11, 21) for col in range(3, grid_size[1])}
    ships = [ship1, ship2, ship3, ship4, ship5]
    alg_ships = coordinates
    human_ships, grid2 = ShipPlacement.Ship_placement(grid2)
    alg_mine = [value for name, value in human_ships.items() if name == "ship6"][0][0]
    del human_ships["ship6"]
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), quit()

            pos = Grid.get_position(square_size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start_button.start == True:
                if turn and pos in grid2:
                    human_previous, turn, grid_colors, grid2, human_ships = Human(grid_colors, grid2, human_previous, turn, pos, human_ships, alg_mine, alg_previous)
                
            if turn == False:
                var_modes, alg_previous, turn, alg_ships, result = Algorithm(var_modes, coordinates, grid_colors, grid2, human_previous, alg_previous, alg_ships, result)
            
                turn = True
                if grid2[human_previous[-1]] == (0,0,0):
                    turn = False
                     
        window.fill((225,225,225))  
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)

        mine.ship_event(event, square_size, coordinates)
        start_button.button_event(event, coordinates)
        reset_button.button_event(event, coordinates)
        
        for ship in ships:
            ship.ship_event(event, square_size, coordinates)
        
        start_button.place_button(window)
        reset_button.place_button(window)
        test_text.place_label()

        if start_button.start == False:
            for ship in ships:
                ship.place_ship(window)
            mine.place_ship(window)

            grid_colors = {(col, row): (50, 50, 50) for row in range(21) for col in range(grid_size[1])}
            for coordinate in grid_colors.keys():
                if coordinate[1] == 11 or coordinate[0] == 0 or coordinate[0] == 11:
                    grid_colors[coordinate] = (225, 225, 225)

            for name, coordinate in coordinates.items():
                for coord in coordinate:
                    if name == "mine":
                        grid_colors[coord] = (0, 0, 0)
                    else:
                        grid_colors[coord] = (0, 0, 225)
        pygame.display.flip()  
start_game()