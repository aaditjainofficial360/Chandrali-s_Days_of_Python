'''
********DAY 20********
Python coding question:

Write a function in Python that accepts a credit card number.
It should return a string where all the characters are hidden with an asterisk except the last four.
For example, if the function gets sent "4444444444444444", then it should return "4444".
'''

def credit_card(credit_card_number):
    return '*'*len(str(credit_card_number))-4+str(credit_card_number)[-4:]


# Test-case 1
print(credit_card(4444444444444444))