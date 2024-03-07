# Write your solution here
import datetime

def get_age() -> int:
    user_day = int(input("Day: "))
    user_month = int(input("Month: "))
    user_year = int(input("Year: "))

    user_age = datetime.datetime(user_year, user_month, user_day)
    millennium = datetime.datetime(1999, 12, 31)

    difference = millennium-user_age
    
    if difference.days >= 0:
        print(f"You were {difference.days} days old on the eve of the new millennium.")
    
    else:
        print("You weren't born yet on the eve of the new millennium.")

get_age()