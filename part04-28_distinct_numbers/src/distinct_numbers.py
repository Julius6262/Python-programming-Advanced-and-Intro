# Write your solution here
def distinct_numbers(list_1):
    new_list =[]
    for number in list_1:
        if number not in new_list:
            new_list.append(number)
    return sorted(new_list)

  