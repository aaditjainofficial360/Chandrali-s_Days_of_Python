'''
********DAY 21********
Python coding question:

Write a Python code to accept a string and count the number of vowels and consonants.
Print them separately.
'''

def count_them(string):
    vowels = ['a','e','i','o','u']
    vowel_count=0
    consonant_count=0
    for i in string.split():
        for j in i:
            if j.lower() in vowels:
                vowel_count+=1
            else:
                consonant_count+=1
    print('Consonant Count:',consonant_count)
    print('Vowel Count:',vowel_count)
    return ''
# Test-case 1
print(count_them('Aadit is great'))

# Test-case 2
print(count_them('Mummy'))
