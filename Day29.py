'''
********DAY 29********
Python coding question:

Create a function called sumOfTwo(a, b, v) with 3 parameters.
a is a list of numbers values, such as [22, 341, 21, 5, 0, -5].
b is also a list of number values, just like a.
a and b can be anything; negative, a float, etc.
v is a single number value.
The function should check if it is possible to take one number from both list a and b, and add the numbers together to equal the number v.
If there are 2 numbers that can do this, print “True”. Otherwise, print “False”.
For example:
sumOfTwo([1, 2, 3], [10, 20, 30], 23)
The output would be “True” because 3 + 20 = 23.
'''

def sumOfTwo(a, b, v):
    for i in a:
        for j in b:
            if i+j==v:
                return True
    else:
        return False

# Test-case 1
print(sumOfTwo([1, 2, 3], [10, 20, 30], 23))