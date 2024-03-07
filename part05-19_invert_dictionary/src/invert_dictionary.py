# Write your solution here

def invert(dictionary: dict) -> dict:
    inverted_dict = {}

    for key , value in dictionary.items():
        inverted_dict[value] = key
    dictionary.clear()
    dictionary.update(inverted_dict)
