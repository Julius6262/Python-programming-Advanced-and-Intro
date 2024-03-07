# Write your solution here
import re

def is_dotw(my_string: str):
    expression = "Mon|Tue|Wed|Thu|Fri|Sat|Sun"

    if re.search(expression, my_string):
        return True
    return False

def all_vowels(my_string: str):
    expression = re.compile(r'^[aeiouAEIOU]+$')

    if re.search(expression, my_string):
        return True
    return False

def time_of_day(my_string: str):
    expression = re.compile(r'^([01]\d|2[0-3]):([0-5]\d):([0-5]\d)$')

    if re.search(expression, my_string):
        return True
    return False

print(time_of_day("12:43:01"))
print(time_of_day("AB:01:CD"))
print(time_of_day("17:59:59"))
print(time_of_day("33:66:77"))