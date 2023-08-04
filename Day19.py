'''
********DAY 19********
Python coding question:

BLACKJACK: Given three integers between 1 and 11,
if their sum is less than or equal to 21, return their sum.
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
'''

def blackjack(num1,num2,num3):
    if num1+num2+num3<=21:
        return num1+num2+num3
    else:
        if num1==11 or num2==11 or num3==11:
            return num1+num2+num3-10
        else:
            return 'BUST'

# Test-case 1
print(blackjack(5,6,7))

# Test-case 2
print(blackjack(9,9,9))

# Test-case 3
print(blackjack(9,9,11))
