# Write your solution here
def smallest_average(person1: dict, person2: dict, person3: dict):
    persons = [person1, person2, person3]
    person_placeholder = None
    avg = None
    
    for person in persons:
        person_sum = 0
        for n in range(1,4):
            person_sum += person[f"result{n}"]

        
        avg_loop = person_sum/(len(persons)-1)  # subtract the name
        
        if avg is None or avg_loop < avg:
            avg = avg_loop
            person_placeholder = person
    
    return person_placeholder
        