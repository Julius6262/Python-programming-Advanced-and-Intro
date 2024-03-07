# Write your solution here:
def sort_by_seasons(items: list):
    def get_order (item: dict):
        return item["seasons"]
    
    return sorted(items, key= get_order)
