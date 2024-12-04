# #Write a Python program to find the largest number in a list.
numbers = [100,400,600,700,200,800]
larger_numbers = max(numbers)
print("The largest in list is :" ,larger_numbers )

# Second method
number = [10,40,60,70,20,80]
largest_numbers = number[0]
for num in number:
    if num > largest_numbers :
        largest_numbers = num
print("The largest number in the list is:", largest_numbers)