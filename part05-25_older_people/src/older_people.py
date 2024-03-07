# Write your solution here
def older_people(people: list, year: int):
    born_before = []

    for tup in people:
        if tup[1] < year:
            born_before.append(tup[0])
    return born_before
