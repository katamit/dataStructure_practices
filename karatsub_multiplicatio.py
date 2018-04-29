# coding: utf-8
from math import ceil, log10
import  random
def karatsuba(x, y):
    # Base condiotion check
    if x < 10 or y < 10 :
        return x*y
    # set n. the number of digits in the highest input number
    n  = max(int(log10(x) +1), int(log10(y)+1))

    # rounds up n/2
    n_2 = int(ceil(n/2))
    
    # adds 1 is n is uneven
    n = n if n%2 == 0 else n+1

    # splits the input numbers
    a, b = divmod(x, 10**n_2)
    c, d = divmod(y, 10**n_2)

    # performing the 3 recursive steps of karatsuab algorithm.
    ac = karatsuba(a,c)
    bd = karatsuba(b,d)
    ad_bc = karatsuba( (a+b), (c+d)) - ac - bd
    
    # pefroms the multiplication
    return 10**n*ac + bd + 10**n_2*ad_bc


def test():
    x = random.randint(1, 10**10)
    y = random.randint(1, 10**10)
    print("Testing with x = {0} and y = {1}".format(x,y))
    expected = x*y
    result = karatsuba(x,y)
    if result == expected:
        return "successful"
    return "failed"
 
print(test())
print(test())
