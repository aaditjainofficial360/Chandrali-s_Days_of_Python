'''
********DAY 22********
Python coding question:

Write a function in Python that accepts a list of any length that contains a mix of non-negative integers and strings.
The function should return a list with only the integers in the original list in the same order.
'''

def filter_numbers(lst):
    result_list=[x for x in lst if str(x).isdigit()]
    return result_list

# Test-case 1
print(filter_numbers([1,5,8,2,'Aadit','Jain','Official',67,82,98,100,'AJ','I Love You']))

# Test-case 2
print(filter_numbers([1,3,2,4,6,9,12,21,2020,2017,'Shreyaadi','Shreya','I',26,'Love',8,'You']))