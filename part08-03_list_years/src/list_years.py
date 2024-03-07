# Write your solution here
# Remember the import statement
from datetime import date

def list_years(dates: list):
    year_list = []
    for value in dates:
        year = value.year
        year_list.append(year)
    
    year_list.sort()

    return year_list