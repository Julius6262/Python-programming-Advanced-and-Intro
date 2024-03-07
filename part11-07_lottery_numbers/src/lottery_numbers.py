# WRITE YOUR SOLUTION HERE:
class LotteryNumbers:
    def __init__(self, week_num: int, list7: list):
        self.week_num = week_num
        self.list7 = list7
    
    def number_of_hits(self, numbers: list):
        return len([number for number in numbers if number in self.list7])

    def hits_in_place(self, numbers: list):
        return [number if number in self.list7 else -1 for number in numbers]

