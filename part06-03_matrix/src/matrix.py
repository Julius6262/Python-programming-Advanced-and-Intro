# write your solution here
def matrix_sum ():
    sum_of_row = []
    
    with open("matrix.txt") as file:
        for line in file:
            sum_one_row = 0  
            line = line.replace("\n","")
            line = line.split(",")
            for num in line:
                sum_one_row += int(num)
            sum_of_row.append(sum_one_row)
    
    matrix_sum = sum(sum_of_row)
    
    return matrix_sum


def matrix_max():
    all_num = []
    
    with open("matrix.txt") as file:
        for line in file: 
            line = line.replace("\n","")
            line = line.split(",")
            for num in line:
                num = int(num)
                all_num.append(num)
    
    greates = max(all_num)
    
    return greates


def row_sums():
    sum_of_row = []
    
    with open("matrix.txt") as file:
        for line in file:
            sum_one_row = 0  
            line = line.replace("\n","")
            line = line.split(",")
            for num in line:
                sum_one_row += int(num)
            sum_of_row.append(sum_one_row)
    
    return sum_of_row
