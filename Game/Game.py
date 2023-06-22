import pygame 
import GUI
from Button import Button
from Ships import Ship
from Scanner import Scanner
import Grid
import Algorithm.Algorithm as Algorithm

def start_game():
    human_previous = []
    alg_previous = []
    possible = []
    result = False
    sinking = False
    turn = True

    coordinates = {}
    grid_colors = {}
    second_grid = [(col, row) for row in range(13, 23) for col in range(10)]

    window, resolution, grid_size, line_width = GUI.get_info()
    square_width, square_height = GUI.get_square_size(resolution, grid_size, line_width)
    
    
    button = Button(square_width * 10 + ((square_width) / 2), square_width, 150, 50, (100, 100, 100), "start game")
    scanner = Scanner(square_width * 12, square_width * 5, square_width, square_width, (0, 200, 0))
    mine = Ship(square_width * 5 + 6, square_width * 5 + 5, square_width, square_width, (0, 0, 0), "mine")
 
    ship1 = Ship(0, 0,  (square_width + 1) * 5, square_width + 1, (0, 0, 225), "ship1")
    ship2 = Ship(0, square_width * 2 + 1,  (square_width + 1) * 4, square_width + 1, (0, 0, 225), "ship2")
    ship3 = Ship(0, square_width * 4 + 5,  (square_width + 1) * 3, square_width + 1, (0, 0, 225), "ship3")
    ship4 = Ship(0, square_width * 6 + 6,  (square_width + 1) * 3, square_width + 1, (0, 0, 225), "ship4")
    ship5 = Ship(0, square_width * 8 + 8,  (square_width + 1) * 2, square_width + 1, (0, 0, 225), "ship5")

    ships = [ship1, ship2, ship3, ship4, ship5]
    old_ships = coordinates
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = Grid.get_position(square_width)
                scanner.scanner_event(event, square_width)

                if scanner.place == False:
                    scanner.place_scanner(window)

                # if scanner.drag:
                #     while scanner.drag
                #     turn = False

                if event.button == 1 and button.start == True and pos in second_grid:
                    if pos in second_grid and turn == True:                   
                        if Grid.check_hit(pos, grid_colors):
                            grid_colors[pos] = (225, 0, 0)
                        else:
                            grid_colors[pos] = (225, 225, 225)
                        human_previous.append(pos)
                    turn = False
                    
                    if len(alg_previous) != 0:
                        result = Grid.check_hit(alg_previous[-1], grid_colors)
                        print(grid_colors[alg_previous[-1]])
                        if grid_colors[alg_previous[-1]] == (225, 225, 0):
                            grid_colors[alg_previous[-1]] = (225, 225, 225)
                            turn = True

                if turn == False:
                    guess = Algorithm.choose_mode(result, grid_colors, coordinates, alg_previous, sinking, possible)
                    possible = guess[1]
                    guess_coord = guess[0]
                    
                    if Grid.check_hit(guess_coord, grid_colors):
                        grid_colors[guess_coord] = (225, 0, 0)
                        new_ships = Algorithm.remove_ships(old_ships, guess_coord)
                        old_ships = new_ships[0]
                        if new_ships[1]:
                            sinking = False
                            possible = []
                        else:
                            sinking = True
                    elif Grid.check_mine(guess_coord, grid_colors):
                        grid_colors[guess_coord] = (225, 225, 0)
                        # creeer een message voor turn overslaan

                    else:
                        grid_colors[guess_coord] = (225, 225, 225)

                    possible = [i for i in possible if i not in alg_previous]
                    alg_previous.append(guess_coord)
                    print(alg_previous)
                    turn = True
                    
                     
        window.fill((225,225,225))  
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)

        mine.ship_event(event, square_width, coordinates)
        button.button_event(event, ships, coordinates)
        
        for ship in ships:
            ship.ship_event(event, square_width, coordinates)
        
        button.place_button(window)

        if button.start == False:
            for ship in ships:
                ship.place_ship(window)
            mine.place_ship(window)

            grid_colors = {(col, row): (50, 50, 50) for row in range(23) for col in range(10)}
            for coordinate in grid_colors.keys():
                if 10 <= coordinate[1] <= 12:
                    grid_colors[coordinate] = (225, 225, 225)

            for name, coordinate in coordinates.items():
                for coord in coordinate:
                    if name == "mine":
                        grid_colors[coord] = (0, 0, 0)
                    else:
                        grid_colors[coord] = (0, 0, 225)
        pygame.display.flip()  
start_game()