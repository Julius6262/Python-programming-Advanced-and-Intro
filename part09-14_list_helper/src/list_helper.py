# WRITE YOUR SOLUTION HERE:

class ListHelper:

    def __init__(self):
        pass

    @classmethod
    def greatest_frequency(cls, my_list: list):
        counter = 0
        freq_num =""
        for num in my_list:
            num_in = my_list.count(num)
            if num_in > counter:
                counter = num_in
                freq_num = num
        return freq_num

    @classmethod
    def doubles(cls, my_list: list):
        counter = 0
        for num in my_list:
            num_in = my_list.count(num)
            if num_in >= 2:
                counter += 1
            my_list = [item for item in my_list if item != num]
        return counter

