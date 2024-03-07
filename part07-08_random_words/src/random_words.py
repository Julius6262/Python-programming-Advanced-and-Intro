# Write your solution here
import random

def words(n: int, beginning: str) -> list: 
    with open("words.txt") as file:
        words_list = [line.replace("\n", "") for line in file]

    word_startswith = [word for word in words_list if word.startswith(beginning)]
    
    if n > len(word_startswith):
        raise ValueError

    selected_words = random.sample(word_startswith, n)

    
    return selected_words

