# Write your solution here

def count_matching_elements(my_matrix: list, element: int):
    total = []
    for row in my_matrix:
        num_of_element_in_row = row.count(element)
        total.append(num_of_element_in_row)
    return sum(total)
