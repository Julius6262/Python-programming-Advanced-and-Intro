# Write your solution here

my_list = []

count = 1
user_in = 0
while user_in != "x":
    print(f"The list is now {my_list}")

    user_in = input("a(d)d, (r)emove or e(x)it: ")

    if user_in == "d":
        my_list.append(count)
        count += 1
        
    
    if user_in == "r":
        my_list.pop(-1)
        count -= 1
print("Bye!")        