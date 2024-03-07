# Write your solution here
def even_numbers(arg_1:list):
    func_list = []
    for num in arg_1:
        if num %2 == 0:
            func_list.append(num)
    return func_list
