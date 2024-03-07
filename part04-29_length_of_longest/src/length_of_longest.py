# Write your solution here
def length_of_longest(arg_list):
    best_so_far = " "
    for word in arg_list:
        if len(word) > len(best_so_far):
            best_so_far = word
    return len(best_so_far)