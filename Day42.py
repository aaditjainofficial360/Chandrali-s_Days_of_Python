'''
********DAY 42********
Python coding question:

Given a name, return the letter with the highest index in alphabetical order, with its corresponding index, in the form of a string. You are prohibited to use max() nor is reassigning a value to the alphabet list allowed.

Examples
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


alphabet_index(alphabet, "Flavio") ➞ "22v"

alphabet_index(alphabet, "Andrey") ➞ "25y"

alphabet_index(alphabet, "Oscar") ➞ "19s"

sorted() is not best practice.
'''

def alphabet_index(alphabet, string):
    max_value=-1
    character=''
    for i in string:
        if alphabet.index(i.lower())>max_value:
            max_value=alphabet.index(i.lower())
            character=i.lower()
    result=str(max_value+1)+character
    return result


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]

# Test-case 1
print(alphabet_index(alphabet, "Flavio"))

# Test-case 2
print(alphabet_index(alphabet, "Andrey"))

# Test-case 3
print(alphabet_index(alphabet, "Oscar"))