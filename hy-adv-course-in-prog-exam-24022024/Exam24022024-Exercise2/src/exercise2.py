# Write your solution to exercise 2 here
class ShoppingList:
    def __init__(self):
        self.products = {}

    def add_product(self, product_info):
        name, price_per_unit, unit, quantity = product_info
        if name in self.products:
            current_price_per_unit, current_unit, current_quantity = self.products[name]
            if unit == current_unit:
                self.products[name] = (price_per_unit, unit, current_quantity + quantity)
            else:
                raise ValueError("Cannot add product with different unit")
        else:
            self.products[name] = (price_per_unit, unit, quantity)

    def return_product(self, product_name):
        if product_name in self.products:
            return f"{product_name}: {self.products[product_name][0]:.2f}€/{self.products[product_name][1]}, Quantity: {self.products[product_name][2]:.2f}"
        else:
            raise ValueError("Product not found on the shopping list.")

    def remove_product(self, product_name, quantity=None):
        if product_name in self.products:
            if quantity is None or quantity >= self.products[product_name][2]:
                del self.products[product_name]
            else:
                self.products[product_name] = (self.products[product_name][0], self.products[product_name][1], self.products[product_name][2] - quantity)
        else:
            raise ValueError("Product not found on the shopping list.")

    def change_product_unit_price(self, product_name, new_unit_price):
        if product_name in self.products:
            self.products[product_name] = (new_unit_price, self.products[product_name][1], self.products[product_name][2])
        else:
            raise ValueError("Product not found on the shopping list.")

    def return_all_products(self):
        product_list = []
        for name, product_info in self.products.items():
            price_per_unit, unit, quantity = product_info
            total_price = price_per_unit * quantity
            product_info_str = f"name: {name}, unit price: {price_per_unit:.2f}€/{unit}, quantity: {quantity}{unit}, total price: {total_price:.2f}€"
            product_list.append(product_info_str)
        return product_list


    def return_total_price_of_shopping_list(self):
        total_price = 0
        for product_info in self.products.values():
            price_per_unit, _, quantity = product_info
            total_price += price_per_unit * quantity
        return total_price


#  Examples test
"""apple = ("apple", 1.60, "kg", 2.2)  # 2.2 kg of apples
potato = ("potato", 1.30, "kg", 5.0)  # 5 kg of potatoes
banana = ("banana", 0.95, "kg", 1.2)  # 1.2 kg of bananas
milk = ("milk", 1.25, "l", 2.0)  # 2 liters of milk
bread = ("sourdough bread", 2.50, "piece", 3.0)  # 3 pieces of bread

shopping_list = ShoppingList()

shopping_list.add_product(apple)
shopping_list.add_product(potato)
shopping_list.add_product(banana)
shopping_list.add_product(milk)
shopping_list.add_product(bread)

print("Product information at the beginning:")
all_products = shopping_list.return_all_products()
for product in all_products:
    print(product)

# Notice that inflation has raised the price of bread
shopping_list.change_product_unit_price("sourdough bread", 4.00)

# There's a promotion at the store, and apples are on sale
shopping_list.change_product_unit_price("apple", 1)

print()
print("After the changes:")
all_products = shopping_list.return_all_products()
for product in all_products:
    print(product)

print()
print("Removing 2 loaves of bread, all bananas, and more milk than available:")
shopping_list.remove_product("sourdough bread", 2)
shopping_list.remove_product("banana")
shopping_list.remove_product("milk", 3)
all_products = shopping_list.return_all_products()
for product in all_products:
    print(product)

print("Total price of the shopping list:",
        shopping_list.return_total_price_of_shopping_list())"""