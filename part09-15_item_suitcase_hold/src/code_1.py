class Item:
    def __init__(self, name: str, weight: int):
        self.__name = name
        self.__weight = weight

    def name(self):
        return self.__name

    def weight(self):
        return self.__weight

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg)"


class Suitcase:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__items = []

    def add_item(self, item: Item):
        if self.weight() + item.weight() <= self.__max_weight:
            self.__items.append(item)
            

    def __str__(self):
        item_count = len(self.__items)
        return f"{item_count} {'item' if item_count == 1 else 'items'} ({self.weight()} kg)"

    def print_items(self):
        for item in self.__items:
            print(item)

    def weight(self):
        return sum(item.weight() for item in self.__items)

    def heaviest_item (self):
        if len(self.__items) >= 1:
            max_weight = max(item.weight() for item in self.__items)
            for item in self.__items:
                if item.weight() == max_weight:
                    return item
    
        return None
    

class CargoHold:
    def __init__(self, max_weight: int):
        self.__max_weight = max_weight
        self.__current_weight = 0
        self.__suitcase_list = []

    def add_suitcase(self, suitcase: Suitcase):
        if (self.__current_weight  + suitcase.weight()) <= self.__max_weight:
            self.__suitcase_list.append(suitcase)
            self.__current_weight += suitcase.weight()


    def __str__ (self):
        item_count = len(self.__suitcase_list)
        return f"{item_count} {'suitcase' if item_count == 1 else 'suitcases'}, space for {self.__max_weight - self.__current_weight} kg"

    def print_items(self):
        for suitcase in self.__suitcase_list:
            if suitcase is not None:
                suitcase.print_items()


