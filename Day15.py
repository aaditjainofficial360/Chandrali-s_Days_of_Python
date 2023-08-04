'''
********DAY 15********
Python coding question:

Print only the words that start with "s" in a sentence.

Input:
Salad is healthy snack.

Output:
Salad
snack
'''

def printing_s_words(string):
    for i in string.split():
        if i[0].lower()=='s':
            print(i)
    return ''

Sample_string='Salad is healthy snack'

print(printing_s_words(Sample_string))