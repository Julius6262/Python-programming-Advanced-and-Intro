import string
from datetime import datetime

def is_it_valid(pic: str) -> bool:
    number_string_digits = string.digits
    char_string = "0123456789ABCDEFHJKLMNPRSTUVWXY"
    
    # Ensure the length is correct
    if len(pic) != 11:
        return False
    
    date_of_birth = pic[:6]
    
    
    for num in date_of_birth:
        if num not in number_string_digits:
            return False

    # Adjust the date string based on the century marker
    century_marker = pic[6]
    if century_marker == '+':
        full_birth = date_of_birth[:4] +'18' + date_of_birth[4:]
    elif century_marker == '-':
        full_birth = date_of_birth[:4] +'19' + date_of_birth[4:]
    elif century_marker == 'A':
        full_birth = date_of_birth[:4] +'20' + date_of_birth[4:]
    else:
        return False
    
    
    personal_identifier = pic[7:10]
    
    nine_digit_number = date_of_birth + personal_identifier
    
    num_control_char = int(nine_digit_number) % 31
    
    control_charater = char_string[num_control_char]
    

    if num_control_char >= len(char_string) or num_control_char < 0 or control_charater != pic[-1]:
        return False

    # Validate the date using the datetime module
    
    try:
        datetime(int(full_birth[4:8]), int(full_birth[2:4]), int(full_birth[0:2]))
        return True
    except ValueError:
        return False
    
    return True

