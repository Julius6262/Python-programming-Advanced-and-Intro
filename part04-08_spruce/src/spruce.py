# Write your solution here
# You can test your function by calling it within the following block
def spruce(height):
    print("a spruce!")
    count = 0
    increse = 0
    width = -1
    while height > count:
        print(" " * (height+width) + "*"*(1+increse))
        count += 1
        increse += 2
        width -= 1
    print(" " * (height - 1) + "*")

if __name__ == "__main__":
    spruce(5)