'''
*******DAY 46********
Python coding question:

A number is said to be Harshad if it's exactly divisible by the sum of its digits. Create a function that determines whether a number is a Harshad or not.
Examples
is_harshad(75) ➞ False
# 7 + 5 = 12
# 75 is not exactly divisible by 12

is_harshad(171) ➞ True
# 1 + 7 + 1 = 9
# 9 exactly divides 171

is_harshad(481) ➞ True

is_harshad(89) ➞ False
'''

def is_harshad(number):
    sum_of_digits=0
    for i in str(number):
        sum_of_digits+=int(i)
    return number%sum_of_digits==0

# Test-case 1
print(is_harshad(75))

# Test-case 2
print(is_harshad(171))

# Test-case 3
print(is_harshad(481))

# Test-case 4
print(is_harshad(89))