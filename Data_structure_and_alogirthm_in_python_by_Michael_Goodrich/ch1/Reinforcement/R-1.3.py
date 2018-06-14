# coding: utf-8
def minmax(data):
    ''' takes a  sequence of one or more numbers'''
    min = data[0]
    max = data[0]
    for val in data:
        if val < min:
            min = val
        elif val > max:
            max = val
    return min, max
print(minmax([2,56,32,52,34,6,34,6,323,34]))
