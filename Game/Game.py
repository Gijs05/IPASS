import pygame 
import GUI
from Button import Button
from Ships import Ship
import Grid

def start_game():
    window, resolution, grid_size, line_width = GUI.get_info()
    square_width, square_height = GUI.get_square_size(resolution, grid_size, line_width)
    
    button = Button(resolution[0] - 275, 100, 150, 50, (200, 200, 200), "start game")
    ship1 = Ship(300, 300,  square_height * 5, square_height - 10, (0, 0, 225))
    ship2 = Ship(300, 400,  square_height * 4, square_height - 10, (0, 0, 225))

    ships = [ship1, ship2]
    coordinates = []
    grid_colors = {(col, row): (50, 50, 50) for row in range(10) for col in range(10)}
    Turn = True
    # een lijst met keys
    previous = []
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and button.start == True:
                    pos = Grid.get_position(square_height)
                   
                    if Grid.check_hit(pos, grid_colors):
                        grid_colors[pos] = (225, 0, 0)
                    else:
                        grid_colors[pos] = (225, 225, 225)

                    previous.append(False)
                    Turn = False
                    
        window.fill((225,225,225))  
        GUI.draw_grid(grid_size, window, resolution, line_width, grid_colors, coordinates)

        button.button_event(event, ships)
        ship1.ship_event(event, square_height)
        ship2.ship_event(event, square_height)
        
        button.place_button(window) 
        ship1.place_ship(window)
        ship2.place_ship(window)


        # # print(int(ship1.rect.x // 10), int(ship1.rect.y // 10), int((ship1.rect.x + ship1.rect.width) // 10), int((ship1.rect.y + ship1.rect.height) // 10))
        # start_col = int(ship1.rect.x // 10)
        # start_row = int(ship1.rect.y // 10)
        # end_col = int((ship1.rect.x + ship1.rect.width) // 10)
        # end_row = int((ship1.rect.y + ship1.rect.height) // 10)

        # coordinates = []
        # for row in range(start_row, end_row + 1):
        #     for col in range(start_col, end_col + 1):
        #         coordinates.append((row, col))
        
        
        coordinates = [ship1, ship2]
        pygame.display.flip()  
        
start_game()