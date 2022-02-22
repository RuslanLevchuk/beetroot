import random

score = 0
lives = 5
coocrdinates_symb = 'abcdefghijklmnopqrstuvwxyz'
symbol_flag = '✓'
user_matrix = []
matrix = []
#temporary
matrix_size = 5
bombs = 10
bombs_found = 0
mark_bomb = False
empty_cells = 0
detected_bombs = 0
game_started_flag = False


def start_settings():
    global score
    global lives
    global empty_cells
    global detected_bombs
    global user_matrix
    global matrix
    global matrix_size
    global matrix_len
    global game_started_flag
    global bombs
    global bombs_found

    print("Type size of map (min: 5 | max: 20). \nIf your input will be out of range, "
              "size of map will be selected automatically.")
    #Input map size
    while True:
        matrix_size = input("Map size: ")
        try:
            matrix_size = int(matrix_size)

            if matrix_size < 5:
                matrix_size = 5
                print("You have selected a map size less than 5, so it is automatically selected as the smallest size 5")
            elif matrix_size > 20:
                matrix_size = 20
                print("You have selected a map size more than 20, so it is automatically selected as the biggest size 20")
            #reset all values after previous game
            bombs = matrix_size * 2
            bombs_found = 0
            score = 0
            lives = 5
            empty_cells = 0
            detected_bombs = 0
            user_matrix = []
            matrix = []
            matrix_len = matrix_size - 1

            break
        except ValueError:
            print("Your input must have only digits, try again!")
    #after getting mapsize from user game_started_flag becomes "True", it means game is able to start
    game_started_flag = True
    #generate maps
    prepare_maps(matrix)


#generate user map and map with bombs
def prepare_maps(matrix):
    global empty_cells
    global matrix_size
    global bombs


    # prepare hiden empty infomap with 0 in each cell
    for i in range(matrix_size):
        matrix.append([])
        for j in range(matrix_size):
            matrix[i].append(0)


    #adding bombs in empty infomap (matrix)
    bomb_added = 0
    while 1:
        row_random = random.randint(0, matrix_len)
        col_random = random.randint(0, matrix_len)
        if matrix[row_random][col_random] == 0:
            matrix[row_random][col_random] = '*'
            bomb_added += 1
        if bomb_added == bombs:
            break


    for row in matrix:
        for cell in row:
            if cell == 0:
                empty_cells += 1

    #prepareu user map
    for i in range(matrix_size):
        user_matrix.append([])
        for j in range(matrix_size):
            user_matrix[i].append('x')

    for row_number, row_matrix in enumerate(matrix):
        for row_position, row_symbol in enumerate(row_matrix):
            if row_symbol == '*':#Check if current symbol in matrix is equal '*' (bomb)
    #↓↓↓↓↓↓↓↓↓↓ below we check adjacent positions for each current position of bomb '*'
    #  and add incremention (+1) to all adjacent empty positions (← → ↑ ↓ ↖ ↗ ↘ ↙)
    #######################################################################  ↓↓↓  check each horyzontal adjacent pos.
                if row_position == 0 and row_matrix[row_position+1] != '*': # ✓ |0→| (check relative to the 0 pos on the right)
                    matrix[row_number][row_position + 1] += 1
                elif row_position == matrix_len and row_matrix[row_position-1] != '*': # ✓ |←last|
                    matrix[row_number][row_position - 1] += 1
                elif row_position > 0 and row_position < matrix_len:# ✓ |0←→last| (check each between 1st and last pos)
                    if row_matrix[row_position+1] != '*':       # ✓ |x→| 1іе & last pos are not included
                        matrix[row_number][row_position + 1] += 1
                    if row_matrix[row_position-1] != '*':       # ✓ |←x| f1st & last pos are not included
                        matrix[row_number][row_position - 1] += 1
    ####################################################################### ↓↓↓  check each vertical adjacent pos.

                if row_number == 0 and matrix[row_number+1][row_position] != '*': # ✓ 0 pos to adjacent pos ↓
                    matrix[row_number+1][row_position] += 1
                elif row_number == matrix_len and matrix[row_number-1][row_position] != '*': # ✓ last pos to adjacent pos ↑
                    matrix[row_number-1][row_position] += 1
                elif row_number > 0 and row_number < matrix_len:  # ✓ other pos to adjacent pos ↑↓ (1st and last are mot included)
                    if matrix[row_number-1][row_position] != '*':# ✓  ↑
                        matrix[row_number-1][row_position] += 1
                    if matrix[row_number+1][row_position] != '*': # ✓  ↓
                        matrix[row_number+1][row_position] += 1

    ####################################################################### ↓↓↓  check each diagonal adjacent pos.
                if row_number == 0:         #zero row corners
                    if row_position == 0 and matrix[row_number+1][row_position+1] != '*': # ✓ ↘ adjacent to left top corner
                        matrix[row_number + 1][row_position+1] += 1
                    elif row_position == matrix_len and matrix[row_number+1][row_position-1] != '*': # ✓ ↙ adjacent to left bottom corner
                        matrix[row_number + 1][row_position-1] += 1
                    elif row_position > 0 and row_position < matrix_len: # ↘ ↙ between left top and lebt bootom corners
                        if matrix[row_number+1][row_position-1] != '*':
                            matrix[row_number + 1][row_position - 1] += 1
                        if matrix[row_number+1][row_position+1] != '*':
                            matrix[row_number + 1][row_position + 1] += 1

                elif row_number == matrix_len:      #last row corners
                    if row_position == 0 and matrix[row_number-1][row_position+1] != '*': # ✓ ↗ adjacent to left bottom corner
                        matrix[row_number - 1][row_position + 1] += 1
                    elif row_position == matrix_len and matrix[row_number-1][row_position-1] != '*':  # ✓ ↖ adjacent to reight bottom corner
                        matrix[row_number - 1][row_position - 1] += 1
                    elif row_position > 0 and row_position < matrix_len: # ✓ ↖ ↗ adjacent to left bottom corner
                        if matrix[row_number-1][row_position-1] != '*':
                            matrix[row_number - 1][row_position - 1] += 1
                        if matrix[row_number-1][row_position+1] != '*':
                            matrix[row_number - 1][row_position + 1] += 1

                elif row_number > 0 and row_number < matrix_len: #between zero and last corners:
                    if row_position == 0: #first row
                        if matrix[row_number - 1][row_position + 1] != '*':
                            matrix[row_number - 1][row_position + 1] += 1
                        if matrix[row_number + 1][row_position + 1] != '*':
                            matrix[row_number + 1][row_position + 1] += 1
                    elif row_position == matrix_len: #last row
                        if matrix[row_number - 1][row_position - 1] != '*':
                            matrix[row_number - 1][row_position - 1] += 1
                        if matrix[row_number + 1][row_position - 1] != '*':
                            matrix[row_number + 1][row_position - 1] += 1
                    elif row_position > 0 and row_position < matrix_len: # between first and last
                        if matrix[row_number-1][row_position-1] != '*':
                            matrix[row_number - 1][row_position - 1] += 1
                        if matrix[row_number-1][row_position+1] != '*':
                            matrix[row_number - 1][row_position + 1] += 1
                        if matrix[row_number+1][row_position-1] != '*':
                            matrix[row_number + 1][row_position - 1] += 1
                        if matrix[row_number+1][row_position+1] != '*':
                            matrix[row_number + 1][row_position + 1] += 1


def print_map(map_size, mtrx):
    global matrix_len
    borders = ['╔', '╚', '╗', '╝', '═', '║'] # define borders for drawing maps
    coordinates_digit = list(range(1, 26)) # define list of numbers for draw row titles of map (1, 2, 3..)


    print('    ', end='')
    for i in range(map_size): #draw coordinete signs (a, b, c, d ...)
        print(f"{coocrdinates_symb[i]}  ", end='')
    print('')
    print(f"  {borders[0]}", end='') # draw left top corner symbol

    for i in range(map_size*3): # draw top border
        print(borders[4], end='')
    print(borders[2]) # draw left right corner symbol

    for r_num, row in enumerate(mtrx):
        if r_num<9:
            # if left coordinate digits are double-symbols: whitespace  is single end (else is double)
            print(coordinates_digit[r_num], end=' ') #print left coordinates digits
        else:
            print(coordinates_digit[r_num], end='')
        print(borders[5], end=' ')  # prin left border
        for num, symbol in enumerate(row): # print map content
            if num == matrix_len:
                print(symbol, end=' ') # pint whitespaces between each cell
            else:
                print(symbol, end='  ') # print longer whitespace before right border
        print(borders[5], end='')  #print right border
        if r_num == 0:   #printing game statistics
            print(f" {coordinates_digit[r_num]}    | LIVES: {lives}")
        elif r_num == 1:
            print(f" {coordinates_digit[r_num]}    | SCORE: {score}")
        elif r_num == 2:
            print(f" {coordinates_digit[r_num]}    | EMPTY CELLS TO OPEN: {empty_cells}")
        elif r_num == 3:
            print(f" {coordinates_digit[r_num]}    | BOMBS FOUND: {bombs_found}/{bombs}")
        else:
            print(f" {coordinates_digit[r_num]} ")

#printing bootom borders and coordinete signs
    print(f"  {borders[1]}", end='')
    for i in range(map_size*3):
        print(borders[4], end='')
    print(borders[3])
    print('    ', end='')
    for i in range(map_size):
        print(f"{coocrdinates_symb[i]}  ", end='')


#command deploy and command reactions
def make_shot(coordinate):
    global lives
    global score
    global matrix
    global user_matrix
    global mark_bomb
    global detected_bombs
    global bombs_found
    user_row = 0
    #get coodinate in fomat "1a" etc or "1a*" ets
    coordinate = list(coordinate)
    #if coommand length is shorter or longer, function returns 'incorrect'
    if len(coordinate)>4 or len(coordinate)<2:
        return 'incorrect'

    if coordinate[len(coordinate)-1] == '*': #check if symbol * available in command
        mark_bomb = True #value True means we mark flag on map
        coordinate.pop(len(coordinate)-1) #delete symbol * in end of comand
    # check if symbol is in coordinates alphabet
    if coordinate[len(coordinate)-1].lower() in coocrdinates_symb[0:matrix_size]:
        #define column coordinate in digit format
        user_col = coocrdinates_symb.index(coordinate[len(coordinate)-1].lower())
    else:
        return 'incorrect'
    #check if one or two symbols are digits and calculate row coordinate from them
    if coordinate[0].isdigit() and coordinate[1].isdigit():
        user_row = int(coordinate[0])*10 + int(coordinate[1])-1
    elif coordinate[0].isdigit():
        user_row = int(coordinate[0])-1
    if user_row > matrix_size:
        return 'incorrect'
    #return doubleshot if we have olready opened that coordinates
    if user_matrix[user_row][user_col] != 'x':
        return 'doubleshot'
    # if in chosen cell there is * (bomb), than checks other statements
    if matrix[user_row][user_col] == '*':
        #if user input has *, it means program must mark cell as cell with bomb
        # if there was a bomb, program congrads user and add's +5 to score
        if mark_bomb == True:
            user_matrix[user_row][user_col] = symbol_flag
            score += 5
            bombs_found += 1
            mark_bomb = False #reset bomb flag
            print('YOU FOUND A BOMB!')
        # if user input was without *, it means user lose, bomb explodes and lives become one less
        elif mark_bomb == False:
            user_matrix[user_row][user_col] = '◌' #bobmb exploding
            lives -= 1
            bombs_found += 1
            print('LOSE!')
    else:
        # if there no bomb in cell and user marks it as cell with bomb, than there nothing does
        if mark_bomb == True:
            user_matrix[user_row][user_col] = symbol_flag
            mark_bomb = False
            print('There no bomb...')
        #if command without * mark, and threre no bomb, than cell just opens and score increases on 1
        else:
            user_matrix[user_row][user_col] = matrix[user_row][user_col]
            score += 1
            print('HUH!')


while True:
    #if there no lives, user can restart or end game
    if lives == 0:
        while 1:
            choice = input("GAME OVER! Restart? (y/n): ")
            if choice.lower() == 'y':
                start_settings()
                break
            elif choice.lower() == 'n':
                break
            else:
                print('Incorrect input!')
                pass
    if bombs == bombs_found:
        while 1:
            choice = input(f"YOU WIN!! You fond {bombs_found - 5 - lives} bombs "
                           f"and Your score is {score} \nRestart? (y/n): ")
            if choice.lower() == 'y':
                start_settings()
                break
            elif choice.lower() == 'n':
                break
            else:
                print('Incorrect input!')
                pass

    # runs on the start of program when initial state of flag is False
    if game_started_flag == False:
        start_settings()
    #uncomment to see real map with bombs
    #print_map(matrix_size, matrix)
    #printing of map
    print_map(matrix_size, user_matrix)
    #asking for coordinates
    user_coordinate = input("\nType coordinate (for example '2c') to make a shot or add symbol '*'(for example '2c*') in the end "
                            "to mark a bomb. \nInput your data =>  ")
    # give coordinate command to make shot
    shot_request = make_shot(user_coordinate)
    #check requests from function "make_shot"
    if shot_request == "incorrect":
        print('Input is not correct')
    elif shot_request == 'doubleshot':
        print('These coordinates are already opened...')

