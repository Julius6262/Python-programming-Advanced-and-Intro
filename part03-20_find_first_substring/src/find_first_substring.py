word = input("Please type in a word: ")
char = input("Please type in a character: ")

index = word.find(char)

if index != -1 and index+3 <= len(word):
    print(word[index:index+3])
