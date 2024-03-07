# Write your solution here

user_str = input("Please type in a string: ")

if user_str[1] == user_str[-2]:
    print(f"The second and the second to last characters are {user_str[1]}")
else:
    print("The second and the second to last characters are different")