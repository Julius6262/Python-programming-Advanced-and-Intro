# Write your solution here

user_num = int(input("Please type in a number: "))

l_num = 1

while l_num <= user_num:
    r_num = 1

    while r_num <= user_num:
        print(f"{l_num} x {r_num} = {l_num*r_num}")
        r_num += 1
    
    l_num += 1