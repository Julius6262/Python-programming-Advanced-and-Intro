# Write your solution here
import string

def separate_characters(my_string: str):
    lower_and_uppercase = ""
    punctuation = ""
    rest = ""
    for char in my_string:
        if char in string.ascii_letters:
            lower_and_uppercase += char

        elif char in string.punctuation:
            punctuation += char
        
        else:
            rest += char
    
    return lower_and_uppercase, punctuation, rest