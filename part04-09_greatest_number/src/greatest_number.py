# Write your solution here
def greatest_number(num_1,num_2,num_3):
    num_list = [num_1,num_2,num_3]
    num_list.sort()

    return num_list[-1]


if __name__ == "__main__":
    greatest = greatest_number(5, 9, 8)
    print(greatest)