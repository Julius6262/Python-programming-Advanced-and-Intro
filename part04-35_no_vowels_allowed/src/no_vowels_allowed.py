# Write your solution here

def no_vowels(arg:str):
    vowels = "aeiou"

    for letter in arg:
        if letter in vowels:
          arg = arg.replace(letter, "")  
    return arg