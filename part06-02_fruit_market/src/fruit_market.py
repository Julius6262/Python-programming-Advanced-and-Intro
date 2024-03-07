# write your solution here
def read_fruits() -> dict:
    with open("fruits.csv") as file:
        fruits_dict = {}
        for line in file:
            line = line.replace("\n","")
            line = line.split(";")
            fruits_dict[line[0]] = float(line[1])
    return fruits_dict