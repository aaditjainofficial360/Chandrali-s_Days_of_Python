'''
********DAY 4********
Python coding question:
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)
Note:A pangram is a sentence containing every letter of the alphabet.
Example:
A quick brown fox jumps over the lazy dog.
'''

def pangram_string(string):
    string_dump=''
    alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in string_dump.split():
        string_dump+=i
    for character in alphabets:
        if character not in string_dump.lower():
            return False
    else:
        return True

sample_string='A quick brown fox jumps over the lazy dog'
print(pangram_string(sample_string))