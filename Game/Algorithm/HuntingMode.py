# from collections import Counter

    
# def get_possibilities(grid, grid_colors):
#     hits = [coord for row in grid for coord in row if grid_colors[coord] == (225, 0, 0)]
#     possible = []
#     for possibility in hits:
#         possible.append(get_surrounding(possibility, grid))

#     flat = []
#     for row in possible:
#         [flat.append(coord) for coord in row]
#     return flat

# # def get_most_common(possible):
# #     x_list = []
# #     y_list = []
# #     new_possible = []
# #     for coord in possible:
# #         x_list.append(coord[0])
# #         y_list.append(coord[1])
# #     best_x = Counter(x_list).most_common(1)[0][0]
# #     best_y = Counter(y_list).most_common(1)[0][0]

# #     most_common_coord = x_list
# #     if len(x_list) < len(y_list):
# #         most_common_coord = y_list

# #     for i in most_common_coord:
# #         print(best_x)
# #         if i[0] == best_x:
# #             new_possible.append(i)
# #     print(new_possible)

# def guess(previous, grid_colors, result, possible):
#     coords = [coord for coord in grid_colors.keys()]
#     grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]

#     if result:
#         new_possible = get_possibilities(grid, grid_colors)
#         new_possible = [new for new in new_possible if new not in previous]
#         most_common = Counter(new_possible).most_common(1)[0][0]
#         return most_common, new_possible
    
#     if len(previous) != 0:
#         possible.remove(previous[-1])
#     print(possible)

#     most_common = Counter(possible).most_common(1)[0][0]
#     return most_common, possible

# def check_hit(coordinate, grid_colors):
#     if grid_colors[coordinate] == (0, 0, 225) or grid_colors[coordinate] == (225, 0, 0):
#         return True
#     else:
#         return False

# def get_possibilities(coordinate, ships):
#     max_length = max(ships.values())
    
#     max_x, min_x, max_y, min_y = coordinate[0], coordinate[0], coordinate[1], coordinate[1]
#     for _ in range(max_length - 1):
#         max_x, max_y = max_x + 1, max_y + 1
#         min_x, min_y = min_x - 1, min_y - 1

#     coords = {"max_x": max_x, "max_y": max_y, "min_x": min_x, "min_y": min_y}
#     p = {name: value for name, value in coords.items() if value >= 0}
#     return p

# def check_other_ships(grid):
#     other_ships = []
#     for name, value in grid.items():
#         if value == (225, 0, 0) or value == (0, 0, 0):
#             other_ships.append(name)
#     return other_ships

# def guess(ships, grid1, grid2, previous, original):
#     others = check_other_ships(grid1)
#     if check_hit(previous[-1], grid_colors):
#         possible = get_possibilitie(previous[-1], ships)
#     else:
#         possible = get_possibilities(original, ships)
#     if check_hit(previous[-1], grid1):
#         for name, value in possible.items():
#             if name == "max_x" and (previous[-1][0] + 1, previous[-1][1]) not in others:
#                 guess = (previous[-1][0] + 1, previous[-1][1])
#                 break
#             elif name == "max_y" and (previous[-1][0], previous[-1][1] + 1) not in others:
#                 guess = (previous[-1][0], previous[-1][1] + 1)
#                 break
#             elif name == "min_x" and (previous[-1][0] - 1, previous[-1][1]) not in others:
#                 guess = (previous[-1][0] - 1, previous[-1][1])
#                 break
#             elif name == "min_y" and (previous[-1][0], previous[-1][1] - 1) not in others:
#                 guess = (previous[-1][0], previous[-1][1] - 1)
#                 break
        
#     return guess
#@NODE: kijk naar het totale aantal van de schepen dat nog over zijn. 
# reken dat bij elkaar op en kijk dan wat de meest waarschijnlijke kant is om op te gaan.
        


def get_surrounding(coordinate, grid):
    surrounding_hor = [row[coord] for row in grid for coord in range(len(row) - 1) if row[coord - 1] == coordinate or row[coord + 1] == coordinate]
   
    surrounding_ver = [collumn[coord] for collumn in list(map(list, zip(*grid))) for coord in range(len(list(collumn)) - 1) if list(collumn)[coord - 1] == coordinate or list(collumn)[coord + 1] == coordinate]
    surrounding_coordinates = [coord for coordinates in [surrounding_hor, surrounding_ver] for coord in coordinates]

    viable_coordinates = [surround for surround in surrounding_coordinates for coord in grid if surround in coord]
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
    
    [row.remove(coord) for row in all_coords.values() for coord in row if coord not in grid_colors or grid_colors[coord] == (225,0,0) or grid_colors[coord] == (225,225,225)]
    ver = {name: row for name, row in all_coords.items() if name[0] == 0}
    hor = {name: row for name, row in all_coords.items() if name[1] == 0}  
    print(all_coords)
    return all_coords, ver, hor

def guess(possibilities, previous, result, reserve, grid_colors):
    if len(previous) == 0:
        max_value = max(possibilities[0].values())
        for row in possibilities[0].values():
            if len(row) == max_value and grid_colors[row[0]] != (225, 0, 0):
                guess = row[0]
        

# grid_colors = {(col, row): (50, 50, 50) for row in range(10) for col in range(10)}
# grid_colors[(0,4)] = (225,225,225)
# grid_colors[(0,6)] = (225,225,225)
# grid_colors[(0,1)] = (225, 0, 0)

# coordinate = (0,0)

# coords = [coord for coord in grid_colors.keys()]
# grid = [list(coords[i:i+10]) for i in range(0, 100, 10)]


# get_all_possibilities(coordinate, grid, grid_colors)