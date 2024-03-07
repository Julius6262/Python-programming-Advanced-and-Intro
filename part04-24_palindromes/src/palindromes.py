# Write your solution here
# Note, that at this time the main program should not be written inside
def palindromes(arg_1:str):
    my_list = []
    for letter in arg_1:
        my_list.append(letter)
    if my_list == my_list[::-1]:
        print(f"{arg_1} is a palindrome!")
        return True
    print("that wasn't a palindrome")
    return False

def get_palindrome():
    state = False
    while not state:
        user_pal = input("Please type in a palindrome:")
        state = palindromes(user_pal)
    return
get_palindrome()
# block!
