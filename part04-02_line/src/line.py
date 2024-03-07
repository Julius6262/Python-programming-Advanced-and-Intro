# Write your solution here
def line(inter,string):
    if inter != "" and string != "":
        print(string[0]*inter)
    else:
        print("*"*inter)
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(2, "lol")