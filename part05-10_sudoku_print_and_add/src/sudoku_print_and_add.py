# Write your solution here

def sudoku_grid_correct(sudoku: list):
    def row_correct(sudoku: list, row_no: int):
        seen_once = []
        for num in sudoku[row_no]:
            if num > 0 and num in seen_once:
                return False
            seen_once.append(num)
        return True

    def column_correct(sudoku: list, column_no: int):
        seen_once = []
        for row in sudoku:
            num = row[column_no]
            if num > 0 and num in seen_once:
                return False
            seen_once.append(num)
        return True

    def block_correct(sudoku: list, row_no: int, column_no: int):
        numbers = []
        for r in range(row_no, row_no + 3):
            for s in range(column_no, column_no + 3):
                num = sudoku[r][s]
                if num > 0 and num in numbers:
                    return False
                numbers.append(num)
        return True

    # Check each row
    for row_no in range(9):
        if not row_correct(sudoku, row_no):
            return False

    # Check each column
    for col_no in range(9):
        if not column_correct(sudoku, col_no):
            return False

    # Check each 3x3 block
    for row_no in range(0, 9, 3):
        for col_no in range(0, 9, 3):
            if not block_correct(sudoku, row_no, col_no):
                return False
    return True

def print_sudoku(sudoku: list):
    """
    Takes a two-dimensional array representing a sudoku grid as its argument.
    The function prints out the grid in the specified format.
    """
    count_for_space = 0
    count_for_newline = 0
    count_for_horizontal_space = 0
    
    for row in sudoku:
        for num in row:
            if num == 0:
                print("_", end=" ")
            else:
                print(num, end=" ")
            
            count_for_space += 1
            if count_for_space == 3:  # Making side to side space
                count_for_space = 0
                count_for_newline += 1
                print(" ", end="")
        
        print()
        count_for_horizontal_space += 1  # Making space up and down
        if count_for_horizontal_space == 3:
            count_for_horizontal_space = 0
            print()


    
def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    
    sudoku[row_no][column_no] = number

