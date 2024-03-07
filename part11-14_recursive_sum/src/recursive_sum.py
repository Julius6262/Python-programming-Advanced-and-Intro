def recursive_sum(number: int):
    # Base case: if the number is 1, return 1
    if number <= 1:
        return number
    
    # Recursive case: sum the current number with the sum of the previous numbers
    return number + recursive_sum(number - 1)