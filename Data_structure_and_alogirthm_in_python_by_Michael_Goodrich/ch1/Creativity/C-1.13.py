# coding: utf-8
def list_reverse(data):
    '''takes a list reverses the elements and return the reversed list'''
    end = len(data) -1
    for i in range(len(data)//2):
        data[i],data[end-i] =data[end-i], data[i]
    return data
 
print(list_reverse([1,2,3,4]), list_reverse([1,2,3,4,5]))
a = [1,3,4,6]
a.reverse()
print(a)
