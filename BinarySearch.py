# coding: utf-8
def binary(arr, start, end, value):
    # print('start',start,end)
    mid = (end+start)//2
    if end < start:
        # print('first if')
        return None
    if arr[mid] == value:
        return True
    elif arr[mid] > value:
        end = mid -1
    else:
        start = mid +1
    return binary(arr, start, end, value)

    
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,7))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,8))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,1))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,11))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,2))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,3))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,4))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,5))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,6))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,7))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,8))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,9))
print(binary([1,2,3,4,5,6,7,8,9,10],0,9,10))
