# Write your solution to exercise 1 here
#ready

class Product:
    def __init__(self, name, unit_price, unit, quantity=0):
        # Validate name
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string of at least 3 characters")
        self.name = name

        # Validate unit price
        if not isinstance(unit_price, (float)) or unit_price <= 0:
            raise ValueError("Unit price must be a positive number")
        self.unit_price = float(unit_price)

        # Validate unit
        if not isinstance(unit, str) or unit == "":
            raise ValueError("Unit must be a non-empty string")
        self.unit = unit.strip()

        """OBS the instruction says: 'The quantity is a floating-point number, but the user may also not provide quantity'
        But the examples has interger values"""
        # Validate quantity
        if quantity == 0:
            self.quantity = quantity 
        elif not isinstance(quantity, (float)) or quantity == 0:
            raise ValueError("Quantity must be a floatingpoint number")
        self.quantity = quantity

        # Calculate total price with this attribute
        self.total_price = self.unit_price * self.quantity


    def __str__(self):
        return f"{self.name}, unit price: {self.unit_price:.2f}€/{self.unit}, quantity: {self.quantity}{self.unit}, total price: {self.total_price:.2f}€"

    def __add__(self, other):
        if isinstance(other, Product):
            # Calculate the total price of the two products
            total_quantity = self.quantity + other.quantity
            total_price = self.total_price + other.total_price
            # Return a new Product object with the calculated total price
            return Product("Combined", total_price / total_quantity, "unit", total_quantity)
        else:
            raise ValueError("Can only add Product objects together")


#Test code with examples
"""
apple = Product("apple", 1.60, "kg", 1.0)
pear = Product("pear", 2.00, "kg")
print(apple)
print("After type conversion apple Product becomes a ", len(str(apple)), "characters long string")
print(pear)

apple = Product("apple", 1.60, "kg", 2.0)
potato = Product("potato", 1.30, "kg", 2.0)
banana = Product("banana", 0.90, "kg", 3.0)
bread = Product("sourdough bread", 2.70, "piece", 1.0)
print("Apple price", apple.total_price)
print("Total price:", (apple + potato + banana + bread).total_price)"""