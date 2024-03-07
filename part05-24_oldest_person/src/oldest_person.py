# Write your solution here
def oldest_person(people: list) -> str:
    age = 2023
    name = "hi"
    for tup in people:
        if tup[1] < age:
            age = tup[1]
            name = tup[0]
    return name

