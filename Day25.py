'''
********DAY 25********
Python coding question:

Write a program to print all the prime numbers between 0 to N.
N being any integer.

'''

def find_prime(N):
    for i in range(2,N+1):
        for j in range(2,i):
            if j%i==0:
                break
        else:
            continue
    return ''

print(find_prime(13))
