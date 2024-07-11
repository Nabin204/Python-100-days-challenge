# First Method
def mean1(nums : list[int])-> float:
    length = len(nums)
    sum1 = sum(nums)
    average = sum1/length
    return average

list1 = input("Enter space seperated numbers:").split()
lst = [int(i) for i in list1]
avg = mean1(lst)
print(avg)

# Second Method
from statistics import mean
print(mean(lst))