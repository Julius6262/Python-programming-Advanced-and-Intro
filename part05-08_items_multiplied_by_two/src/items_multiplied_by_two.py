# Write your solution here
def double_items(numbers: list):
    double_list = []
    for number in numbers:
        number *= 2
        double_list.append(number)
    return double_list
