# Write your solution here

def squared(string,inter):
    h = string * inter * inter
    
    count = inter
    while count > 0:
        print(h[:inter])
        h = h[inter:]
        count -= 1
    

# Testing the function
if __name__ == "__main__":
    squared("hej",5)