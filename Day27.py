'''
********DAY 27********
Python coding question:

Given an input by the user in the form of a positive integer, the program should print out a triangle-shaped pattern made of the star character (*). The input should be stored in a variable called N. N represents the number of rows in the pattern. The number of stars in each row increases by 2 each time.

For example:
If N = 3
*
***
*****
'''

def print_triangle_pattern(N):
    for i in range(1,N+1):
        for j in range(1,i+1):
            print('*',end='')
        print()
    return ''

print_triangle_pattern(3)