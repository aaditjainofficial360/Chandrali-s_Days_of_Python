'''
********DAY 11********
Python coding question:

Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
'''

def paper_doll(string):
    result_string=''
    for i in string:
        result_string+=i*3
    return result_string

print(paper_doll('Hello'))
print(paper_doll('Mississippi'))
