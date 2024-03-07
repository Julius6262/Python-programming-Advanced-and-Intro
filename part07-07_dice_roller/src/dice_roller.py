import random

def roll(die: str) -> int:
    die_a = [3, 3, 3, 3, 3, 6]  # Die A
    die_b = [2, 2, 2, 5, 5, 5]  # Die B
    die_c = [1, 4, 4, 4, 4, 4]  # Die C

    if die == "A":
        result = random.choice(die_a)
    elif die == "B":
        result = random.choice(die_b)
    elif die == "C":
        result = random.choice(die_c)
    else:
        raise ValueError("Invalid die choice")

    return result


def play(die1: str, die2: str, times: int):
    die_1_highest = 0
    die_2_highest = 0
    draw = 0

    for i in range(times):
        result_die1 = roll(die1)
        result_die2 = roll(die2)

        if result_die1 > result_die2:
            die_1_highest += 1
        elif result_die1 < result_die2:
            die_2_highest += 1
        else:
            draw += 1

        print(result_die1, result_die2)

    return die_1_highest, die_2_highest, draw