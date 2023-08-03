'''
********DAY 1********
Python coding question:
Given a list of integers, return True if the array contains a 3 next to a 3 somewhere.
Desired output:
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
has_33([3,3,1]) → True
'''

def has_33(lst):
    for i in range(len(lst)-1):
        if lst[i:i+2]==[3,3]:
            return True
    else:
        return False

print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))
print(has_33([3,3,1]) )