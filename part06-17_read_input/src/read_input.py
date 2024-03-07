# Write your solution here
def read_input(sentence: str, num_1: int, num_2: int) -> int:
    while True:
        user_input = input("Please type in a number: ")

        try:
            user_input_as_int = int(user_input)
            if num_1 <= user_input_as_int <= num_2 or num_1 >= user_input_as_int >= num_2:
                return user_input_as_int

        
        except ValueError:
            pass
        print(f"You must type in an integer between {num_1} and {num_2}")

