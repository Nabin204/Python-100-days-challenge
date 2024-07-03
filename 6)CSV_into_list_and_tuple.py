# Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number
numbers = input("Enter comma seperated numbers:")
num_list = numbers.split(",")
print(num_list)
print(type(num_list))
num_tuple = tuple(num_list)
print(num_tuple)
print(type(num_tuple))