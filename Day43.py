'''
********DAY 43********
Python coding question:

This is a common easy interview question but asked quite often.

Write a function that converts hours into seconds.
Examples
how_many_seconds(2) ➞ 7200

how_many_seconds(10) ➞ 36000

how_many_seconds(24) ➞ 86400
Notes
60 seconds in a minute, 60 minutes in an hour
Don't forget to return your answer.
'''

def how_many_seconds(hours):
    return hours*3600

# Test-case 1
print(how_many_seconds(2))

# Test-case 2
print(how_many_seconds(10))

# Test-case 3
print(how_many_seconds(24))