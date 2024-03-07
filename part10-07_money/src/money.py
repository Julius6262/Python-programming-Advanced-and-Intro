class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents

    def __str__(self):
        if len(str(self.__cents)) >= 2:
            return f"{self.__euros}.{self.__cents} eur"
        else:
            return f"{self.__euros}.0{self.__cents} eur"

    def __eq__(self, another):
        return (self.__euros + self.__cents) == (another.__euros + another.__cents)

    def __gt__(self, another):
        return (self.__euros + self.__cents) > (another.__euros + another.__cents)

    def __lt__(self, another):
        return (self.__euros + self.__cents) < (another.__euros + another.__cents)

    def __ne__(self, another):
        return (self.__euros + self.__cents) != (another.__euros + another.__cents)

    def __add__(self, another):
        total_cents_self = self.__euros * 100 + self.__cents
        total_cents_another = another.__euros * 100 + another.__cents

        result_cents = total_cents_self + total_cents_another

        if result_cents >= 0:
            euros_result = result_cents // 100
            cents_result = result_cents % 100

            return Money(euros_result, cents_result)
        else:
            raise ValueError("A negative result is not allowed")

    def __sub__(self, another):
        total_cents_self = self.__euros * 100 + self.__cents
        total_cents_another = another.__euros * 100 + another.__cents

        result_cents = total_cents_self - total_cents_another

        if result_cents >= 0:
            euros_result = result_cents // 100
            cents_result = result_cents % 100

            return Money(euros_result, cents_result)
        else:
            raise ValueError("A negative result is not allowed")

