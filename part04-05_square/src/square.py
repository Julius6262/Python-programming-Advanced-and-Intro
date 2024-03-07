# Copy here code of line function from previous exercise

def square(height,cara):
    count = 0
    while height > count:
        line(height, cara)
        count += 1
    return

def line(inter,string):
    if inter != "" and string != "":
        print(string[0]*inter)
    else:
        print("*"*inter)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")