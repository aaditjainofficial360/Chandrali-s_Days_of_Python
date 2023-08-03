'''
********DAY 2********
Python coding question:
LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
Desired output:
lesser_of_two_evens(2,4)---> 2
lesser_of_two_evens(2,3)---> 3
lesser_of_two_evens(3,4)---> 4
'''

def lesser_of_two_evens(num1,num2):
    if num1%2==0 and num2%2==0:
        return min(num1,num2)
    else:
        return max(num1,num2)

print(lesser_of_two_evens(2,4))
print(lesser_of_two_evens(2,3))
print(lesser_of_two_evens(3,4))