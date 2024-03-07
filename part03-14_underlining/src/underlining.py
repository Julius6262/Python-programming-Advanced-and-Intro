# Write your solution here



while  True:
    user_str = input("Please type in a string: ")

    if len(user_str) < 1:
        break
    
    print(user_str)
    print(len(user_str)*"-")