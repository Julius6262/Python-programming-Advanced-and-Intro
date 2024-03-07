# Write your solution here
my_list = [1,2,3,4,5]

while True:
    index = int(input("index"))
    if index == -1: break
    
    value = int(input("value"))
    
    my_list[index] = value
    print(my_list)