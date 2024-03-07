user_num = int(input("Please type in a number: "))

second_count = 2

while second_count <= user_num:
    print(second_count)
    print(second_count - 1)
    
    
    second_count += 2

if user_num % 2 != 0:
    print(user_num)
