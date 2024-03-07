# Write your solution here
def new_person(name: str, age: int) -> tuple:
    if not (0 < len(name) <= 40 and name.count(" ") >= 1):
        raise ValueError   
    if not (-1 < age < 151):
        raise ValueError 
        
    return name, age

