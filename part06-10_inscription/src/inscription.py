# Write your solution here

user_sign = input("Whom should I sign this to:" )
user_file_name = input("Where shall I save it: ")

with open(user_file_name, "w") as file:
    file_sentence = f"Hi {user_sign}, we hope you enjoy learning Python with us! Best, Mooc.fi Team"

    file.write(file_sentence)