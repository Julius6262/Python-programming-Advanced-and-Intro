# Write your solution here
def remove_smallest(numbers: list):
    num_to_remove = numbers[0]
    for number in numbers:
        if number < num_to_remove:
            num_to_remove = number
    numbers.remove(num_to_remove)