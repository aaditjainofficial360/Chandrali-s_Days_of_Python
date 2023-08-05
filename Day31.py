'''
********DAY 31********
Python coding question:

Print list in reverse order using a loop.

Expected input:
list1 = [10, 20, 30, 40, 50]

Expected output:
50
40
30
20
10
'''

def print_reverse(lst):
    for i in lst[::-1]:
        print(i)
    return ''

# Test-case 1
sample_list= [10, 20, 30, 40, 50]
print_reverse(sample_list)