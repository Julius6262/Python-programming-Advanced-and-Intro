# WRITE YOUR SOLUTION HERE:
class Employee:
    def __init__(self, name: str):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, employee: 'Employee'):
        self.subordinates.append(employee)

def count_subordinates(employee: Employee) -> int:
    # Base case: if the employee has no subordinates, return 0
    if not employee.subordinates:
        return 0
    
    # Recursive case: count subordinates of each subordinate and sum them up
    total_subordinates = len(employee.subordinates)
    for subordinate in employee.subordinates:
        total_subordinates += count_subordinates(subordinate)

    return total_subordinates