limit = int(input("Type the limit: "))
num = 0
current_sum = 0

while current_sum < limit:
    num += 1
    current_sum += num

print(current_sum)
