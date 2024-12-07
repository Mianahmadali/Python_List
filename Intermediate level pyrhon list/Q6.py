#Given the list nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], write a loop to print each element in the sublists.
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for sub_list in nested_list:
    for elements in sub_list:
        print(elements)