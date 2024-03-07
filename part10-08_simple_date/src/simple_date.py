class SimpleDate:
    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year
        
    def __str__(self):
        return f"{self.day}.{self.month}.{self.year}"

    def __eq__(self, another):
        return (
            self.day == another.day and
            self.month == another.month and
            self.year == another.year
        )

    def __gt__(self, another):
        if self.year > another.year:
            return True
        elif self.year == another.year and self.month > another.month:
            return True
        elif (
            self.year == another.year and
            self.month == another.month and
            self.day > another.day
        ):
            return True
        else:
            return False

    def __lt__(self, another):
        return not self.__gt__(another) and not self.__eq__(another)

    def __ne__(self, another):
        return not self.__eq__(another)
    
    def __add__(self, num_days: int):
        new_date = SimpleDate(self.day, self.month, self.year)
        
        # Calculate the total days from the current date
        total_num_days = (self.year * 12 * 30) + (self.month * 30) + self.day

        # Add the given number of days
        total_num_days += num_days

        # Calculate the new year, month, and day
        new_date.year = total_num_days // (12 * 30)
        remaining_num_days = total_num_days % (12 * 30)
        new_date.month = remaining_num_days // 30
        new_date.day = remaining_num_days % 30

        return new_date

    
    def __sub__(self, another):
        
        total_num_days = (self.year * 12 * 30) + (self.month * 30) + self.day
        another_total_num_days =(another.year * 12 * 30) + (another.month * 30) + another.day

        return abs(total_num_days - another_total_num_days)
    
