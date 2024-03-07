# Write your solution here
def who_won(game_board: list):
    total_1 = 0
    total_2 = 0

    for row in game_board:
        for element in row:
            if element == 1:
                total_1 += 1
            elif element == 2:
                total_2 += 1

    if total_1 > total_2:
        return 1
    elif total_1 < total_2:
        return 2
    return 0
