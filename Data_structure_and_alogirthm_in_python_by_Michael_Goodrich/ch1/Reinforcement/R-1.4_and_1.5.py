# coding: utf-8
def sumSquare(n):
    '''takes a positive integer n and returns sum of dquares of all the positive integers smaller than n'''
    if n < 0:
        return 'Needs a positive number. But Negative given'
    else:
        return sum([x**2 for x in range(1, n)])
    
print(sumSquare(4))
