# Write your solution here

# Write your solution here
def shortest(arg_list):
    best_so_far = arg_list[0]
    for word in arg_list:
        if len(word) < len(best_so_far):
            best_so_far = word
    return best_so_far