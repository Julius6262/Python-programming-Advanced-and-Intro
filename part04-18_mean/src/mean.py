# Write your solution here
# You can test your function by calling it within the following block
def mean(lis:list):
    ar_mean = sum(lis)/len(lis)
    return ar_mean


if __name__ == "__main__":
    my_list = [3, 6, -4]
    result = mean(my_list)
    print(result)