# Write your solution here
my_list = []
times = int(input("how many times?"))

for t in range(times):
    item = input(f"item {t+1}: ")
    my_list.append(int(item))
print(my_list)