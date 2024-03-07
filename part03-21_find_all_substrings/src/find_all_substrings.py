# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")


while True:
    index = word.find(char)

    if index != -1 and index+3 <= len(word):
        print(word[index:index+3])
        word = word[index+1:]
    else:
        break