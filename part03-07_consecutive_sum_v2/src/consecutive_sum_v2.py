# Write your solution here
limit = int(input("Type the limit: "))
num = 0
current_sum = 0
num_count =""

while current_sum < limit:
    num += 1
    current_sum += num
    num_count += str(num) + " + "
print(f"The consecutive sum: {num_count [:-2]} = {current_sum}")
