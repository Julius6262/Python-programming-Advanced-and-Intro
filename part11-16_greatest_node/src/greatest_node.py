# WRITE YOUR SOLUTION HERE:
from ucb import trace
class Node:
    def __init__(self, value, left_child=None, right_child=None):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

def greatest_node(root):
    
    if root is None:
        return float('-inf')

    max_self = root.value
    max_left = greatest_node(root.left_child)
    max_right = greatest_node(root.right_child)

    return max(max_self, max_left, max_right)

