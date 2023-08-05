'''
********DAY 26********
Python coding question:

Write a program to print the Fibonacci series.
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation
Fn = Fn-1 + Fn-2
with seed values
F0 = 0 and F1 = 1
'''

def fibonacci_series(N):
    if N==1:
        return 0
    elif N==2:
        return 1
    else:
        return fibonacci_series(N-1)+fibonacci_series(N-2)

# Test-case 1
# 13th Term is 144
print(fibonacci_series(13))

# Test-case 2
# 10th term is 34
print(fibonacci_series(10))
