'''
********DAY 9********
Python coding question:

Write a Python function that checks whether a word or phrase is palindrome or not.
Example of Palindrome:
Hannah
Anna
'''

def palindrome(string):
    return string.lower()==string[::-1].lower()

print(palindrome('Hannah'))
print(palindrome('Anna'))