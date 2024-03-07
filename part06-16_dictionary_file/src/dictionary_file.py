def add_word(dictionary_file):
    finnish_word = input("The word in Finnish: ")
    english_word = input("The word in English: ")
    entry = f"{finnish_word} - {english_word}\n"

    with open(dictionary_file, "a") as file:
        file.write(entry)

    print("Dictionary entry added")


def search_word(dictionary_file):
    search_term = input("Search term: ")

    with open(dictionary_file) as file:
        for line in file:
            finnish, english = line.strip().split(" - ")
            if search_term in finnish or search_term in english:
                print(f"{finnish} - {english}")


def main():
    dictionary_file = "dictionary.txt"

    while True:
        print("1 - Add word, 2 - Search, 3 - Quit")
        user_function = input("Function: ")

        if user_function == "1":
            add_word(dictionary_file)
        elif user_function == "2":
            search_word(dictionary_file)
        elif user_function == "3":
            print("Bye!")
            break
        else:
            print("Invalid input. Please enter 1, 2, or 3.")


main()
