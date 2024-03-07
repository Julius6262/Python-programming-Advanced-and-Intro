# Write your solution here
import random
def generate_password(length: int):
    password_string = ""
    start_char = "a"
    end_char = "z"

    # ord convert to ascii, and there by we can make a range. chr make it back to characters
    alphabet = [chr(i) for i in range(ord(start_char), ord(end_char) +1)]
    password_list = random.sample(alphabet, length)  # Sample makes sure we dont use the same character twice
    for letter in password_list:
        password_string += letter
    return password_string


import string
import random

def generate_password(length: int, sec: bool, third: bool):
    password_string = ""
    choose_list =[]

    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    password_string += alphabet[0]
    choose_list = alphabet

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

    password_string += ''.join(password_list)

    return password_string
