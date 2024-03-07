# Write your solution here

def longest(strings: list):
    longest_string = 0
    word_in_longest_string = ""
    for string in strings:
        if len(string) > len(word_in_longest_string):
            word_in_longest_string = string
    return word_in_longest_string