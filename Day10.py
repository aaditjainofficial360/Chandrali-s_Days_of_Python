'''
********DAY 10********
Python coding question:

Write a Python function to multiply all the numbers in a list.

Sample List : [1, 2, 3, -4]
Expected Output : -24

'''
from functools import reduce
def multiply_all(lst):
    product=reduce(lambda x,y:x*y,lst)
    return product

sample_list = [1, 2, 3, -4]
print(multiply_all(sample_list))