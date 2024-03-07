import string
import random

def generate_strong_password(length: int, sec: bool, third: bool):
    password_string = ""
    choose_list =[]

    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    password_string += alphabet[0]
    choose_list = alphabet
    length -= 1

    if sec:
        numbers = [str(i) for i in range(1, 10)]
        random.shuffle(numbers)
        password_string += numbers[0]
        choose_list += numbers
        length -= 1

    if third:
        special_char = ["!", "?", "=", "+", "-", "(", ")", "#"]
        random.shuffle(special_char)
        password_string += special_char[0]
        choose_list += special_char
        length -= 1


    password_list = random.sample(choose_list, length)
    
    password_string += "".join(password_list)  # Creating the rest of the password by concatenate elements to a string.
    
    return password_string

print(generate_strong_password(2, False, False))