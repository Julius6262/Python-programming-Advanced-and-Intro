# Write your solution here
import random

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    number_pool = list(range(lower,upper + 1))
    numbers = random.sample(number_pool, amount)
    numbers.sort()
    return numbers