'''
********DAY 24********
Python coding question:

Write a program to find the sum of squares of first 'n' natural numbers.
Input : N = 4
Output : 30
'''

def sum_of_squares():
    N = int(input())
    sum_of_squares=0
    for i in range(N+1):
        sum_of_squares+=i**2
    return sum_of_squares

# Test-case 1
# N = 4
result = sum_of_squares()
print(result)

