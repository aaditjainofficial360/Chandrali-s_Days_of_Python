'''
********DAY 28********
Python coding question:

Given a sentence or cluster of words, find out if there are any integers inside the string. Print out the total number of integers. If there’s at least 1 integer present, find the sum of all of the integers found and print out the sum.

For example:
If string = “200 plus 500 is equal to”
2 integers found
sum: 700
'''

def total_sum(string):
    total_sum=0
    count=0
    for i in string.split():
        if i.isdigit():
            total_sum+=int(i)
            count+=1
    print(f'{count} integers found')
    print('sum:',total_sum)
    return ''

# Test-case 1
sample_string = "200 plus 500 is equal to"
print(total_sum(sample_string))

# Test-case 2
sample_string_new= "I have only 500 rupees. In addition 1000 rupees, I have got from my aunt."
print(total_sum(sample_string_new))