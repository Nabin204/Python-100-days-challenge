n=int(input("Enter an integer:"))
reverse=0
m=n
while(n!=0):
    r=n%10
    reverse=reverse*10+r
    n=n//10
print(f"The reverse of {m} is {reverse}.")
    
# Additional code
if(reverse==m):
    print(f"The number {m} is palindrome.")
else:
    print(f"The number {m} is not palindrome.")