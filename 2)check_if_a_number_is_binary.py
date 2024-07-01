# First Method
def binary_check(num : int)->bool:
    binary_digit = [0,1]
    while(num!=0):
        remainder = num%10
        if(remainder not in binary_digit):
            return False
            break
        num //= 10
    return True
number = int(input("Enter a number:"))
if(binary_check(number)):
    print(f"The number {number} is binary.")
else:
    print(f"The number {number} is not binary.")
    
# Second Method
string1 = str(number)
if(string1.count('1')+string1.count('0')==len(string1)):
    print(f"The number {number} is binary.")
else:
    print(f"The number {number} is not binary.")    