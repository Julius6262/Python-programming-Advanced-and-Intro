# Write your solution here


def filter_incorrect():
    
    def read_file() -> dict:
        all_words = {}

        with open("lottery_numbers.csv","r") as file:
            for row in file:
                row = row.replace("\n","")
                row = row.split(";")
                all_words[row[0]] = row[1:]

        return all_words

    # The week number is incorrect
    incorrect_words = {}
    correct_so_far = {}
    all_nums = "1234567890"
    
    all_words = read_file()

    for key,value in all_words.items():
        if len(key) == 6 and key[5] in all_nums:
            correct_so_far[key] = value
            

        elif len(key)  == 7 and key[5] in all_nums and key[6] in all_nums and int(key[5:7]) < 53:
            correct_so_far[key] = value
            
        else:
            incorrect_words[key] = value
        
    for key,value in correct_so_far.items():
        value = value[0].split(",")
        if len(value) != 7:  # sorting out the weeks with the incorrect amount of numbers
            incorrect_words[key] = value
    
    for key in incorrect_words:  # Keeping the correct_so_far updated
        if key in correct_so_far:
            correct_so_far.pop(key)




    for key, value in correct_so_far.items():
        numbers = value[0].split(",")
        for num in numbers:
            for single in num:
                if single not in all_nums:
                    incorrect_words[key] = value
                    break  # Exit the inner loop if an incorrect character is found
    
    for key in incorrect_words:  # Keeping the correct_so_far updated
        if key in correct_so_far:
            correct_so_far.pop(key)
    
    for key, value in correct_so_far.items():
        numbers = value[0].split(",")
        for num in numbers:
            if  not (0 < int(num) < 40):  # Sorting out the numbers that fall out of the range
                incorrect_words[key] = value

    for key in incorrect_words:  # Keeping the correct_so_far updated
        if key in correct_so_far:
            correct_so_far.pop(key)
                
    
    for key, value in correct_so_far.items():
        numbers = value[0].split(",")
        copy_of_list = numbers
        
        for num in numbers:  
            if numbers.count(num) > 1:  # To screen for the same value appearing twice.
                incorrect_words[key] = value
                


    for key in incorrect_words:  # Keeping the correct_so_far updated
        if key in correct_so_far:
            correct_so_far.pop(key)
    
    def correct_format(correct_so_far: dict) -> list:
        final_list = []
        for key, value in correct_so_far.items():
            final = value
            key = key + ";"
            final.insert(0, key)
            final_list.append(final)
        
        return final_list

    final_list = correct_format(correct_so_far)

    def create_file(final_list: list):
        with open("correct_numbers.csv","w") as correct_file:
            for element in final_list:
                for line in element:
                    correct_file.write(f"{line}")
                correct_file.write("\n")
        return

    make_file = create_file(final_list)

    return  # Outer function

