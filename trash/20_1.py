import random
score = 0
lives = 5

"""
print("Type size of map (min: 5 max: 20). \nIf you input will be out of range, "
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
        break
    except ValueError:
        print("Your input must have only digits, try again!")
"""
matrix = []
#temporary
matrix_size = 5
bombs = 10

for i in range(matrix_size):
    matrix.append([])
    for j in range(matrix_size):
        matrix[i].append(0)
matrix_len = matrix_size-1

for i in range(bombs):
    matrix[random.randint(0, matrix_len)][random.randint(0, matrix_len)] = '*'


def prepare_hiden_infomap(matrix, matrix_size):
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
    borders = ['╔', '╚', '╗', '╝', '═', '║']
    coocrdinates_symb = 'abcdefghijklmnopqrstuvwxyz'
    coordinates_digit = list(range(1, 26))
    print('')
    print('    ', end='')
    for i in range(map_size):
        print(f"{coocrdinates_symb[i]}  ", end='')
    print('')

    print(f"  {borders[0]}", end='')
    for i in range(map_size*3):
        print(borders[4], end='')
    print(borders[2])

    for r_num, row in enumerate(mtrx):
        if r_num<9:
            print(coordinates_digit[r_num], end=' ')
        else:
            print(coordinates_digit[r_num], end='')
        print(borders[5], end=' ')
        for num, symbol in enumerate(row):
            if num == matrix_len:
                print(symbol, end=' ')
            else:
                print(symbol, end='  ')
        print(borders[5], end='')
        print(f" {coordinates_digit[r_num]}")

    print(f"  {borders[1]}", end='')
    for i in range(map_size*3):
        print(borders[4], end='')
    print(borders[3])
    print('    ', end='')
    for i in range(map_size):
        print(f"{coocrdinates_symb[i]}  ", end='')
    print('')

def make_shot(coordinate):
    coordinate = list(coordinate)
    if len(coordinate)>3 or len(coordinate)<2:
        return 'incorrect'
prepare_hiden_infomap(matrix, matrix_size)
print_map(matrix_size, matrix)

user_matrix = []

for i in range(matrix_size):
    user_matrix.append([])
    for j in range(matrix_size):
        user_matrix[i].append('x')
while True:

    print_map(matrix_size, user_matrix)
    user_coordinate = input("\nInput coordinate (for example '2c') to make a shot: ")
    if make_shot(user_coordinate) == "incorrect":
        print('Input is not correct')
