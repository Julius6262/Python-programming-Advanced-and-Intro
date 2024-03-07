# Write your solution here
def same_chars (word,index_1,index_2):
    if len(word) <= index_1 or len(word) <= index_2:
        return False

    elif word[index_1] != word[index_2]:
        return False

    if word[index_1] == word[index_2]:
        return True

if __name__ == "__main__":
    print(same_chars("abc", 0, 3))