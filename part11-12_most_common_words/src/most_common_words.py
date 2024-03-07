# WRITE YOUR SOLUTION HERE:
def most_common_words(filename: str, lower_limit: int):
    with open(filename, "r") as file:
        all_words = [word for line in file for word in line.split()]

        word_counts = {}
        for word in all_words:
            word_counts[word] = word_counts.get(word, 0) + 1

    return {key: value for key, value in word_counts.items() if value >= lower_limit}




