'''
********DAY 3********
Python coding question:
Write a Python function that takes a list and returns a new list with unique elements of the first list.
Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
Unique List : [1, 2, 3, 4, 5]
'''

def unique_list(lst):
    return list(set(lst))

Sample_List =[1,1,1,1,2,2,3,3,3,3,4,5]
print(unique_list(Sample_List))