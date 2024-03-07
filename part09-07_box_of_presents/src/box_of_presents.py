# WRITE YOUR SOLUTION HERE:
class Present:

    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight  #kg
    
    def __str__(self):
        return f"{self.name} ({self.weight}kg)"

class Box: 
    def __init__(self):
        self.total_present = []

    def add_present(self, present: Present):
        self.total_present.append((present.name, present.weight))
        return
        
        
    def total_weight(self):
        total_weight = 0
        for present in self.total_present:
            total_weight += present[1]
        return total_weight


