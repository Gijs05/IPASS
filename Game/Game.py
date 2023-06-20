import pygame 
import GUI
from Button import Button
from Ships import Ship
import Grid
# import Algorithm

def start_game():
    turn = True
    previous = []
    possible = []

    
    coordinates = {}
    grid_colors = {(col, row): (50, 50, 50) for row in range(10) for col in range(10)}

    window, resolution, grid_size, line_width = GUI.get_info()
    square_width, square_height = GUI.get_square_size(resolution, grid_size, line_width)
    
    button = Button(resolution[0] - 275, 100, 150, 50, (200, 200, 200), "start game")
    ship1 = Ship(300, 300,  (square_height + 1) * 5, square_height + 1, (0, 0, 225), "ship1")
    ship2 = Ship(300, 400,  (square_height + 1) * 4, square_height + 1, (0, 0, 225), "ship2")
    ship3 = Ship(300, 500,  (square_height + 1) * 3, square_height + 1, (0, 0, 225), "ship3")
    ship4 = Ship(300, 600,  (square_height + 1) * 3, square_height + 1, (0, 0, 225), "ship4")
    ship5 = Ship(300, 700,  (square_height + 1) * 2, square_height + 1, (0, 0, 225), "ship5")

    ships = [ship1, ship2, ship3, ship4, ship5]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button.start == True and turn == True:
                    pos = Grid.get_position(square_height)
                    print(pos)
                   
                    if Grid.check_hit(pos, grid_colors):
                        grid_colors[pos] = (225, 0, 0)
                    else:
                        grid_colors[pos] = (225, 225, 225)

                    previous.append(pos)
                    # turn = False
                
                elif event.button == 1 and button.start == True and turn == False:
                    result = Grid.check_hit(previous[-1])
                    # guess = Algorithm.choose_mode(result, grid_colors, ships, previous)

                    
        window.fill((225,225,225))  
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors)

        button.button_event(event, ships, coordinates)
        for ship in ships:
            ship.ship_event(event, square_height, coordinates)
        
        button.place_button(window) 

        if button.start == False:
            for ship in ships:
                ship.place_ship(window)

            grid_colors = {(col, row): (50, 50, 50) for row in range(10) for col in range(10)}
            for coordinate_list in coordinates.values():
                for coord in coordinate_list:
                    grid_colors[coord] = (0, 0, 225)
        pygame.display.flip()  
        
start_game()