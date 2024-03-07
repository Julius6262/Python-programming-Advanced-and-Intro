import math
# Write your solution here
def factorials(n: int) -> dict:
    new_dict = {}
    for num in range(1,n + 1):
        result = math.factorial(num)
        new_dict[num] = result
    return new_dict
