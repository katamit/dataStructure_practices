## This file demonstrate one of the most popular and effecient sorting algorithm quick sort
##Quick sort works on the principle of divide and conquer

## selection of the pivot point play a major role in quick sort performance

def quickSort(arr, first, last):
	if last <= first:
		return

	partition_index = partition(arr, first, last)
	quickSort(arr, first, partition_index-1)
	quickSort(arr, partition_index+1, last)


def partition(arr, first, last):
	pivot_index = last
	pivot_value = arr[pivot_index]

	left_index = first
	right_index = last-1

	while True:

		while arr[left_index] <= pivot_value and left_index < last:
			left_index += 1

		while arr[right_index] >= pivot_value and right_index > first:
			right_index -= 1

		if left_index < right_index:
			arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
		else:
			# arr[pivot_index], arr[right_index] = arr[right_index], pivot_value
			# return right_index
			arr[pivot_index], arr[left_index] = arr[left_index], pivot_value
			return left_index



def test():

	# this is done to increase the default recursion limit to rest our quicksor against 
	# list built-in sort functionality for time comparison
	import sys
	sys.setrecursionlimit(1000000)
	# print(sys.getrecursionlimit())


	import time
	a = [6,2,7,89,23,80,342,12,6,0,1,5,2,67,23,4,5,12,3,4,667,23,78,2,9,3,63,23]
	start =time.time()
	quickSort(a, 0, len(a)-1)
	print('Time it took to sort using inbuilt sort %s seconds'%(time.time()-start))

	# print(a)
	a = [6,2,7,89,23,80,342,12,6,0,1,5,2,67,23,4,5,12,3,4,667,23,78,2,9,3,63,23]
	start =time.time()
	a.sort()
	print('Time it took to sort using our quicksort %s seconds'%(time.time()-start))	


	import random

	a = []
	for _ in range(10**5):
		a.append(random.randint(1, 10*9))
	start =time.time()
	a.sort()
	print('Time it took to sort 100000 items using sort() function of list %s seconds'%(time.time()-start))
	
	a = []
	for _ in range(10**5):
		a.append(random.randint(1, 10*9))
	start =time.time()
	quickSort(a, 0, len(a)-1)
	print('Time it took to sort 100000 items using our quickSort %s seconds'%(time.time()-start))

test()


#obtained results

# Time it took to sort using inbuilt sort 6.914138793945312e-05 seconds
# Time it took to sort using our quicksort  9.5367431640625e-06 seconds
# Time it took to sort 100000 items using sort() function of list 0.024422407150268555 seconds
# Time it took to sort 100000 items using our quickSort 5.488919258117676 seconds


# In built sort looks way faster than quicksort,--> as per above observation 200+ times faster for arrray
# of size 100000 elements. This differnce is not big in case of list of small sizes.