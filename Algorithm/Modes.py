import Algorithm.TargetMode as Target
import Algorithm.HuntingMode as Hunting
import copy

def choose_mode(result, grid_colors, previous, ships, var_modes):
    """
    Chooses the algorithm mode and makes a guess based on it.

    Args:
        result (bool): The result of the previous guess.
        grid_colors (dict): A dictionary mapping coordinates to color.
        previous (list): A list of previously guessed coordinates.
        ships (dict): A dictionary containing information about the ships.
        var_modes (dict): A dictionary containing various game mode-related variables.

    Returns:
        tuple: A tuple containing the following elements:
            - guess (tuple): The selected guess coordinate.
            - previous (list): The updated list of previously guessed coordinates.
            - var_modes (dict): The updated dictionary of variables.
    """
    if result or var_modes["sinking"] or len(var_modes["hits"]) != 0:
        if result == False and var_modes["sinking"] == False:
            previous.remove(var_modes["hits"][0])
            previous.append(var_modes["hits"][0])
            result = True

        if var_modes["hit"] == False:
            var_modes["possible"] = Hunting.get_all_possibilities(previous[-1], grid_colors)
            var_modes["hit"] = True
            max_value = len(max(var_modes["possible"][0].values()))

            for name, value in var_modes["possible"][0].items():
                if len(value) == max_value:
                    if name[0] == 0:
                        var_modes["original_way"] = var_modes["possible"][1]
                        var_modes["reserve_way"] = var_modes["possible"][2]
                    elif name[1] == 0:
                        var_modes["original_way"] = var_modes["possible"][2]
                        var_modes["reserve_way"] = var_modes["possible"][1]

        var_modes["sinking"] = True
        guess_info = Hunting.guess(var_modes["original_way"], var_modes["reserve_way"], var_modes["index"], previous, result)  
        guess, var_modes["original_way"], previous, var_modes["index"] = guess_info
        return (guess, previous), var_modes
    
    elif var_modes["sinking"] == False:
       return Target.guess(grid_colors, ships, previous), var_modes
    
def remove_ships(old_ships, coordinate, original_ships, hits):
    """
    Updates the ship information after a coordinate has been hit.

    Args:
        old_ships (dict): The current ship coordinates dictionary.
        coordinate (tuple): The coordinate that has been hit.
        original_ships (dict): The original ship coordinates dictionary.
        hits (list): A list of previously hit coordinates.

    Returns:
        tuple: A tuple containing the following elements:
            - old_ships (dict): The updated ship coordinates dictionary.
            - sink (bool): True if a ship has sunk, False otherwise.
            - end (bool): True if all ships have been sunk, False otherwise.
            - hits (list): The updated list of hit coordinates.
            - changed_coords (list): A list of coordinates that have changed status.
    """
    changed_coords = []
    sink = False
    copy_ships = copy.deepcopy(old_ships)
    for name, coordinates in old_ships.items():
        if coordinate in coordinates:
            coordinates.remove(coordinate)
            old_ships[name] = coordinates
    
    for name in old_ships.keys():
        if len(copy_ships[name]) != len(old_ships[name]) and len(old_ships[name]) == 0:
            sink = True
            changed_coords.append(original_ships[name])
            for name, length in old_ships.items():
                if len(length) == 0:
                    for hit in original_ships[name]:
                        if hit in hits:
                            hits.remove(hit)
                

    for ending in old_ships.values():
        if len(ending) != 0:
            end = False
            break
        else:
            end = True
    return old_ships, sink, end, hits, changed_coords
