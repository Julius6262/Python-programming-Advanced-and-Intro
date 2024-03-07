# Write your solution here
def everything_reversed(arg:list):
    new_list = []
    arg = arg[::-1]
    for word in arg:
        new_list.append(word[::-1])
    return new_list