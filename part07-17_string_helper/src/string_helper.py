# Write your solution here

def change_case(orig_string: str) -> str:
    converted_string = ""
    for char in orig_string:
        if char.isupper():
            converted_string += char.lower()
    
        elif char.islower() or char == " ":
            converted_string += char.upper()
    
    return converted_string


def split_in_half(orig_string: str) -> tuple:
    if len(orig_string) % 2 == 1:
        first_half = int((len(orig_string) + -1 )/2)

        string_tup = (orig_string[:first_half], orig_string[first_half:])
    else:
        string_tup = (orig_string[:(int((len(orig_string)/2)))], orig_string[(int(len(orig_string)/2)):])
    return string_tup

def remove_special_characters(orig_string: str):
    import string

    selected_string =""
    for char in orig_string:
        if char.isupper() or char.islower() or char == " " or char in string.digits:
            selected_string += char
    
    return selected_string
    
if __name__ == "__main__":
    print(split_in_half("abcd"))
