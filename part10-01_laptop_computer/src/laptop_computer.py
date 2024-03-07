# Write your solution here:
class Computer:
    def __init__(self, model: str, speed: int):
        self.__model = model
        self.__speed = speed

    @property  # Getter
    def model(self):
        return self.__model

    @property  # Getter
    def speed(self):
        return self.__speed

class LaptopComputer(Computer):
    def __init__(self, model: str, speed: str, weight: int):
        super().__init__(model, speed)
        self.weight = weight
    
    def __str__(self):
        return f"{self.model}, {self.speed} MHz, {self.weight} kg"
