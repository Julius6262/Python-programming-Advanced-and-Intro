# Write your solution here

def column_correct(sudoku: list, column_no: int):
    seen_once = []
    colum = []
    for row in sudoku:
        print(row[column_no])
        if row[column_no] > 0 and row[column_no] in seen_once:
            return False
        seen_once.append(row[column_no])
            
    return True
