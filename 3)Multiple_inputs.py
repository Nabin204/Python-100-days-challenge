#Accept a list of 5 float numbers as an input from the user
float_list = []
for i in range(5):
    item = float(input("Enter a number:"))
    float_list.append(item)
print(float_list)

# Accepting multiple finite inputs using split method
# While giving inputs there must be space between two numbers
# 1) For strings
first_name,middle_name,last_name=input("Enter your full name:").split()
print(f"First name : {first_name}")
print(f"Middle name : {middle_name}")
print(f"Last name : {last_name}")

# 2) For integers
a,b,c = map(int,input("Enter three numbers:").split())
print(f"First number : {a}")
print(f"Second number : {b}")
print(f"Third number : {c}")

# Accepting infinite number of inputs
list1 = list(map(int,input("Enter numbers:").split()))
print(list1)

list2 = [int(x) for x in input("Enter numbers seperated by comma:").split(",")]
print(list2)