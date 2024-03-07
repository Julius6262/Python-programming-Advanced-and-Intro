# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self,):
        self.persons = []
        

    def add(self, person: Person):
        self.persons.append((person))

    def is_empty(self):
        return len(self.persons) == 0

    def print_contents(self):
        combined_height = 0
        for person in self.persons:
            combined_height = sum(person.height for person in self.persons)
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {combined_height} cm")
        for person in self.persons:
            print(f"{person.name} ({person.height} cm)")

    def shortest(self):
        shortest_person = None
        height_of_shortest = 0
        for person in self.persons:
            if shortest_person is None or person.height < height_of_shortest:
                shortest_person = person
                height_of_shortest = person.height
 
        return shortest_person

    def remove_shortest(self):
        if len(self.persons) >= 1:
            shortest_person = self.shortest()
            self.persons.remove(shortest_person)
            return shortest_person
        else:
            return None