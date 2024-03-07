# Write your solution here

def histogram(my_string: str):
    new_dict = {}
    for letter in my_string:
        if letter not in new_dict:
            new_dict[letter] = 1
        
        else:
            new_dict[letter] += 1
    
    for key,value in new_dict.items():
        stars = value * "*"
        print(f"{key} {stars}")
    return