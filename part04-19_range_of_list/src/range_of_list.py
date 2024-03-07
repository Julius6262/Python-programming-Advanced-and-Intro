# Write your solution here
# You can test your function by calling it within the following block
def range_of_list(arg_1 : list):
    return max(arg_1)-min(arg_1)
if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = range_of_list(my_list)
    print(result)