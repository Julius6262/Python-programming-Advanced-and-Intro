
def handle_word_file() -> list:

    all_words = []

    with open ("wordlist.txt") as word_file:
        for word in word_file:
            word = word.strip()
            all_words.append(word)

    return all_words

user_text = input("Write text: ")
user_text = user_text.strip(".,!?()[]{}':; ")
user_text = user_text.split()


all_words = handle_word_file()

output_word = ""

for word in user_text:
    if word.lower() in all_words:
        output_word += word + " "

    else:
        output_word += "*" + word + "*" + " "

print(output_word)



