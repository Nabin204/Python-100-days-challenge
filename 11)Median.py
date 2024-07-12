# First Method
def median1(nums : list[int]) -> float:
    nums.sort()
    length = len(nums)
    if(length%2==0):
        median = (nums[length//2]+nums[length//2-1])/2
    else:
        median = nums[(length-1)//2]
    return median

# Second Method
from statistics import median

# Takes input from user
lst = input("Emter space seperated numbers : ").split()
lst1 = [int(i) for i in lst]
print(median1(lst1))
print(median(lst1))