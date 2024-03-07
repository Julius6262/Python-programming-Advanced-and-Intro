# Write your solution here


start_num = 0
while True:
    user_num = int(input("Please type in a number"))
    if user_num <= 0:
        print("Thanks and bye!")
        break
    start_num = 0
    factor_num = 1
    while start_num < user_num:
        start_num += 1
        factor_num *= start_num
    print(f"The factorial of the number {user_num} is {factor_num}")
    start_num = 0
    
