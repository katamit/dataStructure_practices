# coding: utf-8
def sumSquareOdd(n):
    '''takes a positive integer n and returns sum of dquares of all the odd positive integers smaller than n'''
    if n < 0:
        return 'Needs a positive number. But Negative given'
    else:
        return sum([x**2 for x in range(1, n) if x%2 != 0])
    
    
print(sumSquareOdd(4))
