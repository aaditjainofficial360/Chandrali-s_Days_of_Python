'''
********DAY 14********
Python coding question:

Print the list of integers from through as a string, without spaces.
Sample Input
3
Sample Output
123
'''

def print_strings_from_1(number):
    result=''.join(list(map(str,[x for x in range(1,number+1)])))
    return result

# Test-case 1
num=3
print(print_strings_from_1(num))

# Test-case 2
num_=5
print(print_strings_from_1(num_))