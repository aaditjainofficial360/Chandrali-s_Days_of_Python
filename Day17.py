'''
********DAY 17********
Python coding question:

Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
'''

def list_of_multiples_of_3():
    multiples_of_3=[x for x in range(1,51) if x%3==0]
    return multiples_of_3

print(list_of_multiples_of_3())