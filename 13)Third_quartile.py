# Since third quartile is the median of upper half of the data so we first make the function to calculate median
import math
def median1(nums : list[int]) -> float:
    length = len(nums)
    if(length%2==0):
        median = (nums[length//2]+nums[length//2-1])/2
    else:
        median = nums[(length-1)//2]
    return median

def Q3(nums : list[int]) ->float:
    nums.sort()
    length = len(nums)
    last_half = nums[math.ceil(length/2):]
    third_quartile = median1(last_half)
    return third_quartile

list1 = [1,2,3,4]
print(Q3(list1))
