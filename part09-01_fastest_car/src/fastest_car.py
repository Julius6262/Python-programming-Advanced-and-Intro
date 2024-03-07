class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (make: {self.make}, top speed: {self.top_speed})"

# Move the fastest_car function outside the Car class
def fastest_car(cars: list):
    fastest_make = None
    fastest_speed = 0

    for car in cars:
        if car.top_speed > fastest_speed:
            fastest_make = car.make
            fastest_speed = car.top_speed
    
    return fastest_make
