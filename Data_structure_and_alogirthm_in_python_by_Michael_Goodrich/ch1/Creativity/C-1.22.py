# coding: utf-8
def dot_product(a, b):
    '''takes two array a and b of length n , and return the dot product of a and b
    such that c[i] = a[i].b[i]
    '''
    if len(a) == len(b):
        c = []
        for i in range(len(a)):
            c.append(a[i]*b[i])
        return c
    else:
        return 'Input arrays must be of same lengths'
    
print(dot_product([1,2,3],[3,2,1]),dot_product([1],[2,4]))
