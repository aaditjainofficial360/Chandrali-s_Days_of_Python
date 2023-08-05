'''
********DAY 32********
Python coding question:

Python got drunk and the built-in functions str() and int() are acting odd:
str(4) ➞ 4

str("4") ➞ 4

int("4") ➞ "4"

int(4) ➞ "4"
You need to create two functions to substitute str() and int(). A function called int_to_str() that converts integers into strings and a function called str_to_int() that converts strings into integers.
Examples:
int_to_str(4) ➞ "4"

str_to_int("4") ➞ 4

int_to_str(29348) ➞ "29348"
'''

def int_to_str(number):
    return '"'+str(number)+'"'

def str_to_int(string):
    return int(string)

# Test-case 1
print(int_to_str(4))

# Test-case 2
print(str_to_int("4"))

# Test-case 3
print(int_to_str(29348))
