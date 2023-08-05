'''
********DAY 23********
Python coding question:

Write a program to find how many times substring “Emma” appears in the given string.
input:
str = "Emma is good developer. Emma is a writer"
Output:
Emma appeared 2 times
'''

def find_Emma(string):
    count=0
    for i in string.split():
        if i=='Emma':
            count+=1
    print(f'Emma appeared {count} times')
    return ''

# Test-case 1
sample_string = "Emma is good developer. Emma is a writer"
print(find_Emma(sample_string))