'''
********DAY 7********
Python coding question:

Define a function called myfunc that takes in a string,
and returns a matching string where every even letter is uppercase, and every odd letter is lowercase.
Desired output:
myfunc('aNiMaL')-->True
'''

def myfunc(string):
    return string[1::2].isupper()

print(myfunc('aNiMaL'))