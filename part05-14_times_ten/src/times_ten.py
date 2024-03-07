# Write your solution here
def times_ten(start_index: int, end_index: int) -> dict:
    new_dict = {}
    for i in range(start_index,end_index + 1):
        new_dict[i] = i*10
    return new_dict
