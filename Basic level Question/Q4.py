#Write a Python program to count how many times a specific element appears in a list.
Students = ["Ahmad","Ali","Amaila", "Laiba","Ahmad"]
Special_Student = "Ahmad"
count = 0
for Student in Students:
    if Student == Special_Student:
        count +=1
print(f"The element {Special_Student} appears {count} times in the list.")

# Second Method

num = [1,2,4,7,1,0,5,3,1,]
specific_element = 1
count = num.count(specific_element)
print(f"The element {specific_element } appears {count} times in the list.")
