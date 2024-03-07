# Write your solution here

def list_sum(list_1,list_2):
    new_list = []
    for index in range(len(list_1)):
        result = sum([list_1[index],list_2[index]])
        new_list.append(result)
    return new_list
