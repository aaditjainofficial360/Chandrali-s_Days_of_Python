'''
********DAY 18********
Python coding question:

Given an integer n, return True if n is within 10 of either 100 or 200.
abs(90)--True
abs(220)--False
'''

def abs(number):
    if number<100 or number<200:
        if number%10==0:
            return True
        else:
            return False
    else:
        return False

# Test-case 1
print(abs(90))

# Test-case 2
print(abs(220))