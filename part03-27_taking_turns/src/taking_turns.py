# Write your solution here

number = int(input("Please type in a number: "))
count = 0
index = 0
while index+1 <= number:
    if count == number:
        break
    print(index+1)
    count += 1
    if count == number:
        break
    print(number - index)
    index += 1
    count += 1
 