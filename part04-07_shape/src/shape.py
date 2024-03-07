# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
# Copy here code of line function from previous exercise

def shape(height_1,cara_1,height_2,cara_2):
    count = 0

    while height_1 > count:
        count += 1
        line(count, cara_1)

    count = 0
    while height_2 > count:
        line(height_1,cara_2)
        count += 1    
    return

def line(inter,string):
    if inter != "" and string != "":
        print(string[0]*inter)
    else:
        print("*"*inter)



if __name__ == "__main__":
    shape(5, "X", 3, "*")