# Define a function to spell out a number in words
def spell_out(number):
    units = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    if 0 <= number <= 9:
        return units[number]
    elif 11 <= number <= 19:
        return teens[number - 10]
    elif number % 10 == 0:
        return tens[number // 10]  # Calculate the tens place
    else:
        return tens[number // 10] + "-" + units[number % 10]  # Calculate the tens place and the reminder

def dict_of_numbers():

    # Generate the dictionary for numbers 0 to 99
    numbers_dict = {}
    for i in range(100):
        numbers_dict[i] = spell_out(i)

    return numbers_dict


numbers = dict_of_numbers()
print(numbers[2])
print(numbers[11])
print(numbers[45])
print(numbers[99])
print(numbers[0])