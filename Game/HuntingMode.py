def get_surrounding(coordinate, grid):
    surrounding_hor = [row[coord] for row in grid for coord in range(len(row) - 1) if row[coord - 1] == coordinate or row[coord + 1] == coordinate]  
    surrounding_ver = [collumn[coord] for collumn in list(map(list, zip(*grid))) for coord in range(len(collumn) - 1) if collumn[coord - 1] == coordinate or collumn[coord + 1] == coordinate] 
    surrounding_coordinates = [coord for coordinates in [surrounding_hor, surrounding_ver] for coord in coordinates]
    viable_coordinates = [coord for coord in surrounding_coordinates for row in grid if coord in row]
    return viable_coordinates

def get_options(coordinate, grid):
    surrounding = get_surrounding((coordinate), grid)
    ways = [(coord[0] - coordinate[0], coord[1] - coordinate[1]) for coord in surrounding]
    
    sides = {}
    for option in ways:
        public_index = ways.index(option)
        if option[0] < 0:
            sides[option] = surrounding[public_index]
        elif option[1] < 0:
            sides[option] = surrounding[public_index]
        elif option[0] > 0:
            sides[option] = surrounding[public_index]
        elif option[1] > 0:
            sides[option] = surrounding[public_index]
    return sides

def get_possibility(side, grid):
    x,y = side[1]
    possible_ways = []
    possible_ways.append((x, y))
    while (x,y) in grid:
        x += side[0][0]
        y += side[0][1]
        possible_ways.append((x, y))
    return possible_ways

def get_all_possibilities(coordinate, grid_colors):
    coords = [coord for coord in grid_colors.keys()]
    grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]

    options = get_options(coordinate, grid)
    all_coords = {i[0]: get_possibility(i, grid_colors) for i in options.items()}
    for row in all_coords.values():
        for coord in row:
            if coord not in grid_colors or grid_colors[coord] == (225,0,0):
                row.remove(coord)
            elif grid_colors[coord] == (225, 225, 225):
                del row[row.index(coord):]

    ver = [row for name, row in all_coords.items() if name[0] == 0]
    hor = [row for name, row in all_coords.items() if name[1] == 0]
    return all_coords, ver, hor

def guess(possibilities, reserve, index, previous, result):
    if index == None:
        max_value = max(possibilities)
        index = possibilities.index(max_value)  

    elif result == False:
        possibilities.pop(index)
        if len(possibilities) == 0:
            possibilities = reserve
            max_value = max(possibilities.values())
            index = possibilities.index(max_value)

        else:
            index = 0

    guess = possibilities[index][0]
    possibilities[index].remove(guess)
    previous.append(guess)
    return guess, possibilities, previous, index
