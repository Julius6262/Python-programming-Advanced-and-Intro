# Write your solution here
def sum_of_positives(arg_1:list):
    sum_1 = 0
    for num in arg_1:
        if num > 0:
            sum_1 += num
    return sum_1
