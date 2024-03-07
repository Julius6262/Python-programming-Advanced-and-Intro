# Write your solution here:
def sort_by_remaining_stock(items: list):  # List of tuples
    def order_by_stock (item: tuple):  # Helper function
        return item[2]
    
    return sorted(items, key=order_by_stock)

