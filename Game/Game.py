import pygame 
import copy
import Game.GUI as GUI
from Game.Button import Button
from Game.Ships import Ship
import Game.Grid as Grid
import Algorithm.ShipPlacement as ShipPlacement
import Algorithm.Modes as Modes

def on_screen(resolution, grid_size, line_width):
    """
    Calculates the size of the game grid and creates the buttons and ships on the screen.

    Args:
        resolution (tuple): The resolution of the game window.
        grid_size (tuple): The size of the game grid.
        line_width (int): The width of the grid lines.

    Returns:
        tuple: A tuple containing the square size of each grid cell and the game objects on the screen.
    """
    square_size = GUI.get_square_size(resolution, grid_size, line_width)[0]
    start_button = Button(square_size * 9, 0, 150, 50, (100, 100, 100), "start game")
    reset_button = Button(square_size * 12, 0, 150, 50, (100, 100, 100), "reset game")

    mine = Ship(square_size * 5 + 6, square_size * 5 + 5, square_size, square_size, (0, 0, 0), "mine") 
    ship1 = Ship(0, square_size,   square_size * 5, square_size, (0, 0, 225), "ship1")
    ship2 = Ship(0, square_size * 3 + 1,  (square_size + 1) * 4, square_size + 1, (0, 0, 225), "ship2")
    ship3 = Ship(0, square_size * 5 + 5,  (square_size + 1) * 3, square_size + 1, (0, 0, 225), "ship3")
    ship4 = Ship(0, square_size * 7 + 6,  (square_size + 1) * 3, square_size + 1, (0, 0, 225), "ship4")
    ship5 = Ship(0, square_size * 9 + 8,  (square_size + 1) * 2, square_size + 1, (0, 0, 225), "ship5")
    return square_size, (start_button, reset_button, mine, ship1, ship2, ship3, ship4, ship5)

def Human(grid_colors, grid2, previous, pos, human_ships, alg_mine, original_ships, var_modes):
    """
    Executes players turn.

    Args:
        grid_colors (dict): The colors of the cells on the game grid.
        grid2 (dict): The game grid.
        previous (list): The previous positions chosen by the human player.
        pos (tuple): The current position chosen by the human player.
        human_ships (dict): The human player's ships and their coordinates.
        alg_mine (tuple): The position of the AI's mine.
        original_ships (dict): The original coordinates of the ships.
        var_modes (dict): Various game mode information.

    Returns:
        tuple: Updated game.
    """
    end = False
    changed_coords = []
    previous.append(pos)  
    if Grid.check_hit(pos, grid2):
        grid_colors[pos] = (225, 0, 0)
        human_ships, _, end, _, changed_coords = Modes.remove_ships(human_ships, pos, original_ships, var_modes)
    else:
        grid_colors[pos] = (225, 225, 225)

    if pos == alg_mine:
        grid_colors[pos] = (0, 0, 0)
    return previous, grid_colors, grid2, human_ships, end, changed_coords

def Algorithm(var_modes, coordinates, grid_colors, grid2, human_previous, alg_previous, alg_ships, result, original_ships):
    """
    Executes AI's turn.

    Args:
        var_modes (dict): Various game mode information.
        coordinates (dict): The AI's ship coordinates.
        grid_colors (dict): The colors of the cells on the game grid.
        grid2 (dict): The game grid.
        human_previous (list): The previous positions chosen by the human player.
        alg_previous (list): The previous positions chosen by the AI.
        alg_ships (dict): The AI's ships and their coordinates.
        result (bool): The result of the previous AI's guess.
        original_ships (dict): The original coordinates of the ships.

    Returns:
        tuple: Updated game.
    """
    hits = var_modes["hits"]
    grid1 = {coord: value for coord, value in grid_colors.items() if coord[0] < 10 and coord[1] < 10}
    if len(alg_previous) == 0:
        guess_data, var_modes = Modes.choose_mode(False, grid1, alg_previous, coordinates, var_modes)
        guess, alg_previous = guess_data

    else:
        guess_data, var_modes = Modes.choose_mode(result, grid1, alg_previous, coordinates, var_modes)   
        guess, alg_previous = guess_data
        result = Grid.check_hit(guess, grid_colors)
    alg_ships, sink, end, hits, changed_coords = Modes.remove_ships(alg_ships, guess, original_ships, hits)
    var_modes["hits"] = hits
    grid_colors = change_color(guess, grid_colors)
    turn = True
    if grid2[human_previous[-1]] == (0,0,0):
        turn = False
   
    if sink:
        var_modes = {"possible": None, "original_way": None, "reserve_way": None, "index": None, "hit": False, "sinking": False, "hits": None}
        var_modes["hits"] = hits
        result = False
    return var_modes, alg_previous, turn, alg_ships, result, end, changed_coords

def change_color(coordinate, grid):
    """
    Updates the color of a grid cell based on a hit or miss.

    Args:
        coordinate (tuple): The coordinate of the grid cell.
        grid (dict): The colors of the cells on the game grid.

    Returns:
        dict: Changed grid colors.
    """
    if Grid.check_hit(coordinate, grid):
        grid[coordinate] = (225, 0, 0)
    elif Grid.check_mine(coordinate, grid):
        grid[coordinate] = (0, 0, 0)
    else:
        grid[coordinate] = (225, 225, 225)
    return grid

def reset_variables(grid_size, resolution, line_width):
    """
    Resets the game variables to their initial state.

    Args:
        grid_size (tuple): The size of the game grid.
        resolution (tuple): The resolution of the game window.
        line_width (int): The width of the grid lines.

    Returns:
        tuple: Resetted game variables.
    """
    human_previous = []
    alg_previous = []
    changed_coords_hum = []
    changed_coords_alg = []
    turn = True
    result = False
    end = False

    coordinates = {}
    start_button, reset_button, mine, ship1, ship2, ship3, ship4, ship5 = on_screen(resolution, grid_size, line_width)[1]

    var_modes = {"possible": None, "original_way": None, "reserve_way": None, "index": None, "hit": False, "sinking": False, "hits": []}
    grid2 = {(col, row): (50, 50, 50) for row in range(11, 21) for col in range(1, grid_size[1] - 1)}
    ships = [ship1, ship2, ship3, ship4, ship5]
    alg_ships = coordinates
    human_ships, grid2 = ShipPlacement.Ship_placement(grid2)
    alg_mine = [value for name, value in human_ships.items() if name == "ship6"][0][0]
    del human_ships["ship6"]
    return (human_previous, alg_previous, turn, result, end, coordinates, changed_coords_hum, changed_coords_alg,
            start_button, reset_button, mine, var_modes, grid2, ships, alg_ships, human_ships, alg_mine)

def start_game():
    """
    Starts the game and handles the main game loop.
    """
    window, resolution, grid_size, line_width = GUI.get_info()
    square_size = on_screen(resolution, grid_size, line_width)[0]
    (human_previous, alg_previous, turn, result, end, coordinates, changed_coords_hum, changed_coords_alg,
    start_button, reset_button, mine, var_modes, grid2, ships, alg_ships, human_ships, alg_mine) = reset_variables(grid_size, resolution, line_width)
    grid_colors = {(col, row): (50, 50, 50) for row in range(21) for col in range(grid_size[1])}
    while True:
        if end:
            while end:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit(), quit()
                GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)
                reset_button.place_button(window)
                reset_button.button_event(event, coordinates)
                if reset_button.reset:
                    reset_variables(grid_size, resolution, line_width)
                    end = False

        if start_button.reset:
            original_ships_hum = copy.deepcopy(human_ships)
            original_ships_alg = copy.deepcopy(alg_ships)
            del coordinates["mine"]
            start_button.reset = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(), quit()

            pos = Grid.get_position(square_size)
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and start_button.start == True:
                if turn and pos in grid2 and pos not in human_previous:
                    human_previous, grid_colors, grid2, human_ships, end, changed_coords_hum = Human(grid_colors, grid2, human_previous, pos, human_ships, alg_mine, original_ships_hum, var_modes)
                    turn = False
                    if end:
                        turn = True

                    if len(alg_previous) != 0 and grid_colors[alg_previous[-1]] == (0, 0, 0):
                        turn = True
                        grid_colors[alg_previous[-1]] = (125, 125, 125)
        changed_coords = [coords for row in [changed_coords_alg, changed_coords_hum] for coords in row]
        for location in changed_coords:
            for coord in location:
                grid_colors[coord] = (125, 125, 0)
        if turn == False:
            var_modes, alg_previous, turn, alg_ships, result, end, changed_coords_alg = Algorithm(var_modes, coordinates, grid_colors, grid2, human_previous, alg_previous, alg_ships, result, original_ships_alg)
            turn = True

            if human_previous[-1] == alg_mine:
                grid_colors[human_previous[-1]] = (125, 125, 125)
                alg_mine = None
                turn = False

        window.fill((225,225,225))  
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)

        mine.ship_event(event, square_size, coordinates)
        start_button.button_event(event, coordinates)
        reset_button.button_event(event, coordinates)

        if reset_button.reset:
            (human_previous, alg_previous, turn, result, end, coordinates, changed_coords_hum, changed_coords_alg,
            start_button, reset_button, mine, var_modes, grid2, ships, alg_ships, human_ships, alg_mine) = reset_variables(grid_size, resolution, line_width)
            grid_colors = {(col, row): (50, 50, 50) for row in range(21) for col in range(grid_size[1])}
        
        for ship in ships:
            ship.ship_event(event, square_size, coordinates)
        
        start_button.place_button(window)
        reset_button.place_button(window)

        if start_button.start == False:
            for ship in ships:
                ship.place_ship(window)
            mine.place_ship(window)

            grid_colors = {(col, row): (50, 50, 50) for row in range(21) for col in range(grid_size[1])}
            for coordinate in grid_colors.keys():
                if coordinate[1] == 10 or coordinate[0] == 0 or coordinate[0] == 11:
                    grid_colors[coordinate] = (225, 225, 225)

            for name, coordinate in coordinates.items():
                for coord in coordinate:
                    if name == "mine":
                        grid_colors[coord] = (0, 0, 0)
                    else:
                        grid_colors[coord] = (0, 0, 225)   
        pygame.display.flip()  
