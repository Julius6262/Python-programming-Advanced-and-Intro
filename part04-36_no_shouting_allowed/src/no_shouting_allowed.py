# Write your solution here

def no_shouting(arg:list):
    lower_list = []

    for word in arg:
        if not word.isupper():
            lower_list.append(word)
    
    return lower_list
