# Write your solution here
def prime_numbers():
    num = 2
    while True:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num
        num += 1

