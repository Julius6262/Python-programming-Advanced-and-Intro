# write your solution here
def largest() -> int:
    with open("numbers.txt") as file:
        biggest_num = 0
        for line in file:
            line = line.replace("\n","")
            line = int(line)
            if line > biggest_num:
                biggest_num = line
    return biggest_num
