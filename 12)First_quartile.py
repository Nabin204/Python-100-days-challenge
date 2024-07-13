# Since first quartile is the median of lower half of the data so we first make the function to calculate median
def median1(nums : list[int]) -> float:
    length = len(nums)
    if(length%2==0):
        median = (nums[length//2]+nums[length//2-1])/2
    else:
        median = nums[(length-1)//2]
    return median

def Q1(nums : list[int]) ->float:
    nums.sort()
    length = len(nums)
    first_half = nums[:length//2]
    first_quartile = median1(first_half)
    return first_quartile

list1 = [1,2,4,5]
print(Q1(list1))
