#Write a Python program to remove duplicates from a list.
num = [9.0,10.8,20.4,30.5,100.4,30.5,9.0]
unique_list = []
for item in num:
       if item not in unique_list:
        unique_list.append(item)
print("List after removing duplicates:", unique_list)