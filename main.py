# from random import randint

# Hidden_Pattern=[[' ']*8 for x in range(8)]
# print(Hidden_Pattern)
# Guess_Pattern=[[' ']*8 for x in range(8)]

# let_to_num={'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}


# def print_board(board):
#     print(' A B C D E F G H')
#     print(' ***************')
#     row_num=1
#     for row in board:
#         print("%d|%s|" % (row_num, "|".join(row)))
#         row_num +=1
# print_board(Hidden_Pattern)

# def get_ship_location():
#     row=input('Please enter a ship row 1-8 ').upper()
#     while row not in '12345678':
#         print("Please enter a valid row ")
#         row=input('Please enter a ship row 1-8 ')
#     column=input('Please enter a ship column A-H ').upper()
#     while column not in 'ABCDEFGH':
#         print("Please enter a valid column ")
#         column=input('Please enter a ship column A-H ')
#     return int(row)-1,let_to_num[column]

# #Function that creates the ships
# def create_ships(board):
#     for ship in range(5):
#         ship_r, ship_cl=randint(0,7), randint(0,7)
#         while board[ship_r][ship_cl] =='X':
#             ship_r, ship_cl = randint(0, 7), randint(0, 7)
#         board[ship_r][ship_cl] = 'X'


# def count_hit_ships(board):
#     count=0
#     for row in board:
#         for column in row:
#             if column=='X':
#                 count+=1
#     return count

# create_ships(Hidden_Pattern)
# print_board(Hidden_Pattern)
# turns = 10
# while turns > 0:
#     print('Welcome to Battleship')
#     print_board(Guess_Pattern)
#     row,column =get_ship_location()
#     if Guess_Pattern[row][column] == '-':
#         print(' You already guessed that ')
#     elif Hidden_Pattern[row][column] =='X':
#         print(' Congratulations you have hit the battleship ')
#         Guess_Pattern[row][column] = 'X'
#         turns -= 1
#     else:
#         print('Sorry,You missed')
#         Guess_Pattern[row][column] = '-'
#         turns -= 1
#     if  count_hit_ships(Guess_Pattern) == 5:
#         print("Congratulations you have sunk all the battleships ")
#         break
#     print(' You have ' +str(turns) + ' turns remaining ')
#     if turns == 0:
#         print('Game Over ')
#         break

import csv
# --- Function definition for generateStartMap ---
# Will take in the size of the map to be made and produce an empty starting map for the game.
def generateStartMap(size):
    startingMap = []
    for counter in range(size):
        currentLine = []
        for counter in range(size):
            currentLine.append("~")
        startingMap.append(currentLine)

    return startingMap

# --- Function definition for shotToNumbers ---
# Will take in a string of a letter and number and return a list of two numbers.
def shotToNumbers(coordinateString, headingsList):
    shotList = []
    shotList.append(int(coordinateString[1]))

    for column in headingsList:
        if coordinateString[0] == column:
            shotList.append(headingsList.index(column))

    return shotList

# --- Function definition for checkHit ---
# Will take in shotCoordinateList and shipMap and return whether the shot hit or missed.
def checkHit(shot, map):
    if map[shot[0]][shot[1]] == "O":
        return ["X", "Miss!"]
    elif map[shot[0]][shot[1]] == "B":
        return ["B", "You hit the BATTLESHIP!"]
    elif map[shot[0]][shot[1]] == "S":
        return ["S", "You hit the SUBMARINE!"]
    elif map[shot[0]][shot[1]] == "D":
        return ["D", "You hit the DESTROYER!"]
    elif map[shot[0]][shot[1]] == "C":
        return ["C", "You hit the CARRIER!"]

# --- Function definition for updateMap ---
# Takes in the current map and the last shot results and returns an updated map.
def updateMap(lastShotCell, lastShotResult, map):
    map[lastShotCell[0]][lastShotCell[1]] = lastShotResult
    return map

# --- Function definition for checkShipStatus ---
# Will check the ship layout to check which ships have been sunk.
def checkShipStatus(shipList, shipMap):
    shipStatus = []
    for index in range(len(shipList)):
        shipStatus.append(False)
    for index in range(len(shipList)):
        for list in shipMap:
            if shipList[index] in list:
                shipStatus[index] = True
    return shipStatus

# --- Game variables ---
gridSize = 10
validRows = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
validColumns = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
shipSymbols = ["B", "S", "D", "C"]
shipNames = ["BATTLESHIP", "SUBMARINE", "DESTROYER", "CARRIER"]
playing = True

# ----------- Starting the Game. Code will need to loop until the user quits. -----------
while playing:
    # --- Initializing the ship locations ---
    fileName = "battleshipMap.txt"      # file where the ship layout is kept
    accessMode = "r"                    # access mode r to read the file
    shipMap = []

    try:
        with open(fileName, accessMode) as fileData:
            shipLocations = csv.reader(fileData)
            for row in shipLocations:
                shipMap.append(row)
    except FileNotFoundError:
        print("Sorry, there was an error loading a required file.")

    # --- Difficulty select. Loop created to ensure valid input entered. ---
    while True:
        difficulty = input("What difficulty would you like to play? (easy/hard) ").lower()
        if difficulty == "easy":
            missileCount = 50  # missileCount used to limit the players guess total
            break
        elif difficulty == "hard":
            missileCount = 35  # missileCount used to limit the players guess total
            break
        else:
            print("Please enter a valid difficulty setting.")

    # --- Variables to be set before each round ---
    currentMap = generateStartMap(gridSize)
    previousShots = []

    # ------ Starting the round. Code will need to loop until the user runs out of guesses or wins. ------
    while missileCount > 0:
        # --- Display currentMap to the user ---
        print("---------------------------")
        print("  " + " ".join(validColumns))
        for counter in range(gridSize):
            print(str(counter) + " " + " ".join(currentMap[counter]))

        print("---------------------------\n"
              "MISSILES REMAINING: " + str(missileCount))

        # --- Get location input from the user for their shot ---
        while True:
            userShot = input("Enter the coordinates you wish to shoot: ").upper()
            if len(userShot) != 2:
                print("Please enter a valid coordinate:")
            elif userShot in previousShots:
                print("You've already shot there, pick a different coordinate.")
            elif userShot[0] not in validColumns or userShot[1] not in validRows:
                print("Please choose a coordinate in range.")
            else:
                previousShots.append(userShot)
                shotCoordinateList = shotToNumbers(userShot, validColumns)
                break

        print("---------------------------")

        # --- Check the shot vs. shipMap to verify a hit or miss ---
        shotResult = checkHit(shotCoordinateList, shipMap)
        print(shotResult[1])

        # --- Update the  game map to refer to when checking ship status ---
        shipMap = updateMap(shotCoordinateList, "X", shipMap)

        # - Check the status of the ships to check win condition -
        shipsStillAlive = checkShipStatus(shipSymbols, shipMap)
        for index in range(len(shipsStillAlive)):
            if shipsStillAlive[index]:
                print("The " + shipNames[index] + " still sails!")
            else:
                print("You have sunk the " + shipNames[index] + "!")

        # --- Update currentMap ---
        currentMap = updateMap(shotCoordinateList, shotResult[0], currentMap)

        # - Check win condition. If not ships remain end the game. ---
        if True not in shipsStillAlive:
            print("Good shooting! You have destroyed the enemy fleet!")
            break

        # - Check lose condition. Modify the missile count then check if the user has shots remaining. -
        missileCount -= 1
        if missileCount == 0:
            print("Looks like the enemy fleet has escaped the harbour! You had better get your crew in order Admiral!")

        # ------ End of the Round. ------
    print("---------------------------")
    userContinue = input("Would you like to play again? (Y/N) ").upper()
    while True:
        if userContinue == "Y":
            playing = True
            break
        elif userContinue == "N":
            playing = False
            break
        else:
            print("Unknown inout, please enter Y or N")

    # ----------- End of the Game. -----------

print("\nThanks for playing!")