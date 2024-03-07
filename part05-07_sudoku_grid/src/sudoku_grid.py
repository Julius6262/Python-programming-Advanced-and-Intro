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
