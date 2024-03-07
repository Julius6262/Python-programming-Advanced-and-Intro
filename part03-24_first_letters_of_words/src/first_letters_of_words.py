# Write your solution here
user_sen = input("Please type in a sentence: ")

word_list = user_sen.split()
for word in word_list:
    print(word[0])