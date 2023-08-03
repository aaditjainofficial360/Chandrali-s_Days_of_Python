'''
********DAY 5********
Python coding question:
Write a function takes a two-word string and returns True if both words begin with same letter
animal_crackers('Crazy Chocolate') --> True
animal_crackers('Lazy Dog') --> False
'''

def animal_crackers(string):
    return string.split()[0][0].lower()==string.split()[1][0].lower()

print(animal_crackers('Crazy Chocolate'))
print(animal_crackers('Lazy Dog'))