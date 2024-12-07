#Given a list nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list that only contains the even numbers.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_number = [num for num in nums if num % 2 == 0] 
print(even_number)
  