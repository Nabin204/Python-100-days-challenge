def add(x :int=10,y :int=9,z :int=4)->int:
    return x+y+z
def multiplication(x :int,y :int ,z :int=5):
    return x*y*z
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number"))

sum1=add(num1,num3)
sum2=add(num2)
sum3=add()
mul1=multiplication(num1,num2,num3)
mul2=multiplication(num3,num1)
print(sum1)
print(sum2)
print(sum3)
print(mul1)
print(mul2)