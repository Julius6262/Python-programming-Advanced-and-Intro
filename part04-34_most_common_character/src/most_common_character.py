# Write your solution here
def most_common_character(arg_1 : str):
    most_times = 0
    common_letter = ""
    for letter in arg_1:
        num_appearance = arg_1.count(letter)
        if num_appearance > most_times:
            most_times = num_appearance
            common_letter = letter
    return common_letter
