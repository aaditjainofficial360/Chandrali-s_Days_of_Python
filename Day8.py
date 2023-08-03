'''
********DAY 8********
Python coding question:

Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
Expected Output :
No. of Upper case characters : 4
No. of Lower case Characters : 33
'''

def count_letters(string):
    upper_count=0
    lower_count=0
    for words in string.split():
        for character in words:
            if character.isupper():
                upper_count+=1
            elif character.islower():
                lower_count+=1
    print('No of Upper case characters :',upper_count)
    print('No of Lower case Characters :',lower_count)



Sample_String ='Hello Mr. Rogers, how are you this fine Tuesday?'
count_letters(Sample_String)