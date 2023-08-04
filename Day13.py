'''
********DAY 13********
Python coding question:
Write a function that capitalizes the first and fourth letters of a name.

TC 1:capitalize("chandrali")
  'ChaNdrali'
TC 2:capitalize("roy")
   'Name is too short!'
'''

def capitalize(string):
    if len(string)>=4:
        return string[0].upper()+string[1:3]+string[3].upper()+string[4:]
    else:
        return 'Name is too short!'

# Test-case 1
print(capitalize("chandrali"))
# Test-case 2
print(capitalize("roy"))