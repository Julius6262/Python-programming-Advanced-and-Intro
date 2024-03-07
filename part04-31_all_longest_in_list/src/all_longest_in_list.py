# Write your solution here
def all_the_longest(arg_list):
    best_so_far = ""
    new_list = []
    for word in arg_list:
        if len(word) > len(best_so_far):
            best_so_far = word
    for w in arg_list:
        if len(best_so_far) == len(w) and w not in new_list:
            new_list.append(w)
    return new_list