#  With a given integral number n, write a program to generate a dictionary that contains (i, i*i)
num=int(input("Enter a number:"))
dictionary = {}
for i in range(1,num+1):
    dictionary[i] = i**2
print(dictionary)

# To print the key of dictionary
for i in dictionary:
    print(i)

# To print values of dictionary
for i in dictionary:
    print(dictionary[i])
    
# To print both keys and values 
print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
print(dictionary.get(8))     
    