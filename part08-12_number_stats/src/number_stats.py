# Write your solution here!
class  NumberStats:
    
    def __init__(self):
        self.numbers = 0
        self.counter = 0


    def add_number(self, number:int):
        self.numbers += number
        self.counter += 1

        
    def count_numbers(self):
        return self.counter

    def get_sum(self):
        if self.numbers > 0:
            return self.numbers
        else: return 0
    
    def average(self):
        if self.numbers > 0:
            return self.numbers/self.counter
        else: return 0

all_stats = NumberStats()
even_stats = NumberStats()
odd_stats = NumberStats()
while True:
    user_int = int(input("Please type in integer numbers: "))

    if user_int == -1:
        print(f"Sum of numbers: {all_stats.get_sum()}\nMean of numbers: {all_stats.average()}")
        print(f"Sum of even numbers: {even_stats.get_sum()}")
        print(f"Sum of odd numbers: {odd_stats.get_sum()}")
        break

    if user_int % 2 == 0:
        even_stats.add_number(user_int)
    else: odd_stats.add_number(user_int)

    all_stats.add_number(user_int)
   
    
    
