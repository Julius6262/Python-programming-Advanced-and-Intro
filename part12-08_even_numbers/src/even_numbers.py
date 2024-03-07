# Write your solution here
def even_numbers(beginning: int, maximum: int):
    if not beginning % 2 == 0:
        beginning += 1
    while beginning <= maximum:
        yield beginning

        beginning += 2
