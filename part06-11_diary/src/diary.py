# Write your solution here

while True:
    print("1 - add an entry, 2 - read entries, 0 - quit")
    user_function = input("Function: ")

    if user_function == "1":
        diary_entry = input("Diary entry: ")

        with open("diary.txt", "a") as file:
            file.write(diary_entry + "\n")

            print("Diary saved")

    elif user_function == "2":
        print("Entries: ")

        with open("diary.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Empty string = False and string with content = True. Thereby skipping empty lines.
                    print(line)  # Print the non-empty line

    elif user_function == "0":
        print("Bye now!")
        break