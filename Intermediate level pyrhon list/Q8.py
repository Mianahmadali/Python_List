#Given two lists list1 = [1, 2, 3, 4] and list2 = [3, 4, 5, 6], find the intersection of both lists.
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
intersection = list(set(list1) & set(list2))
print(intersection)