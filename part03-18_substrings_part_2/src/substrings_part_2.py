# Write your solution here
user_str = input("Please type in a string:")

index = -1

while index >= -len(user_str):
    print(user_str[index:])
    index+= -1