# Write your solution here
def chessboard(size):
    tows = size
    num = size
    while num > 0:
        while tows > 0:
            print(1, end ="")
            tows-= 1
            
            if tows < 1: 
                break

            print(0, end="")
            tows -=1
        
        print()
        
        tows = size
        num -= 1
        
        if num < 1:
            break

        while tows > 0:
            print(0, end ="")
            tows-= 1
            
            if tows < 1: 
                break

            print(1, end="")
            tows -=1
        
        print()
        
        tows = size
        num -= 1
# Testing the function
if __name__ == "__main__":
    chessboard(6)
