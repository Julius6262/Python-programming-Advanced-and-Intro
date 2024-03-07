# Write your solution here
user_str = input("Please type a string")

vowels = "aeo"
index = 0

while index < len(vowels):
    vowel = vowels[index]
    if vowel in user_str:
        print(f"{vowel} found")
    else: print(f"{vowel} not found")
    index +=1