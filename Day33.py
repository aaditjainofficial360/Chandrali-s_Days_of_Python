'''
********DAY 33********
Python coding question:

Write a function in Python to check duplicate letters. It must accept a string, i.e., a sentence.
The function should return True if the sentence has any word with duplicate letters, else return False.
'''

def check_duplicate(string):
    string_dump=''.join(string.split())
    for i in string_dump:
        if string_dump.count(i)>1:
            return True
    else:
        return False

# Test-case 1
print(check_duplicate('Rahul won 10 medals in bodybuilding championships.'))

# Test-case 2
print(check_duplicate('I am yet to prepare for bodybuilding championships occurring next year'))