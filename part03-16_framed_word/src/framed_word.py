# Write your solution here
user_str = input("Word")

mid_1 = (28-len(user_str))//2
mid_2 = (28-len(user_str))-mid_1

print(30 * "*")
print("*"+mid_1*" "+user_str+mid_2*" "+"*")
print(30 * "*")