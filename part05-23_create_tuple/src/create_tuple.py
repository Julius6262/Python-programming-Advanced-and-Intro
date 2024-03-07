# Write your solution here
def create_tuple(x: int, y: int, z: int):
    my_list = [x,y,z]
    my_list.sort()
    sum_1 = sum(my_list)

    my_tuple = (my_list[0],my_list[2],sum_1)
    return my_tuple
