# Copy here code of line function from previous exercise

def box_of_hashes(height):
    count = 0
    while height > count:
        line(10, "#")
        count +=
    return

def line(inter,string):
    if inter != "" and string != "":
        print(string[0]*inter)
    else:
        print("*"*inter)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
