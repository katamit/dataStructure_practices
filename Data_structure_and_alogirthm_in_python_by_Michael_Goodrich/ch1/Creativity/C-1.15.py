# coding: utf-8
def is_all_distinct(seq):
    '''takes a sequence of number and determines if all the numbers are different from each other'''
    return False if len(seq) != len(set(seq)) else True
print(is_all_distinct([1,2,3,4,3]), is_all_distinct([1,2,3]))
