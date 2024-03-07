# Write your solution here
phone_book = {}
while True:
    user_command = int(input("command (1 search, 2 add, 3 quit): "))
    
    if user_command == 1:  # Search
        user_name = input("name: ")
        
        if user_name in phone_book:
            print(phone_book[user_name])
        
        else:
            print("no number")
    
    elif user_command == 2:  # Add
        user_name = input("name: ")
        user_number = input("number: ")
        
        phone_book[user_name] = user_number
    
        print("ok!")
    
    elif user_command == 3:  # Quit
        print("quitting...")
        break
