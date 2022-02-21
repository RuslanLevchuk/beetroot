matrix = [
    ['*', 0, '*', 0, '*'],
    [0, 0, 0, 0, 0],
    ['*', 0, 0, '*', 0],
    [0, 0, 0, 0, '*'],
    ['*', 0, '*', 0, '*'],

]

print(matrix)
matrix_len = len(matrix) -1
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


print('')
for row in matrix:
    for symbol in row:
        print(symbol, end=' ')
    print('')


print('')
print(matrix)


