# Write your solution here
from difflib import get_close_matches

def spell_checker():
    wordslist = []
    sentence = input("Write text: ")
    
    with open("wordlist.txt") as file:
        for line in file:
            line = line.strip()
            wordslist.append(line)

    
    words = sentence.split()
    corrected_sentence = []

    for word in words:
        lower_word = word.lower()
        close_matches = get_close_matches(lower_word, wordslist)
        if close_matches and close_matches[0] != lower_word:
            corrected_sentence.append(f"*{word}*")
            print(f"*{word}*", end= " ")
        else:
            corrected_sentence.append(word)
            print(f"{word}", end= " ")

    print()
    print("suggestions:")
    for word in words:
        lower_word = word.lower()
        close_matches = get_close_matches(lower_word, wordslist)
        if close_matches and close_matches[0] != lower_word:
            corrected_sentence.append(f"*{word}*")
            print(f"{word}: {', '.join(close_matches)}")
        else:
            corrected_sentence.append(word)

    result = ' '.join(corrected_sentence)
    return result

# Example usage:

spell_checker()