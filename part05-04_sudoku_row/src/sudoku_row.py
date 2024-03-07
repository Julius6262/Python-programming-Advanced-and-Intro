# Write your solution here
def row_correct(sudoku: list, row_no: int):
    sudoku[row_no]
    for num in range(1,10):
        count = sudoku[row_no].count(num)
        if count > 1:
            return False
    return True