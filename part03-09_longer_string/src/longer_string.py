str_1 = input("Please type in string 1:")
str_2 = input("Please type in string 2:")

if len(str_1) == len(str_2):
    print("The strings are equally long")

elif len(str_1) > len(str_2):
    print(str_1 , "is longer")
else:
    print(str_2 , "is longer")
