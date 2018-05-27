# This program is to demonstrate the principle of Merge Sort in python
# Merge sort is not an inplace algorithm, whihc means it requires extra space for sorting.

#TIME COMPLEXITY IS 0(nlog(n))

def merge_sort(unsorted_list):
	if len(unsorted_list) == 1:
		return unsorted_list

	mid_point = len(unsorted_list)//2

	left_sorted_list = merge_sort(unsorted_list[:mid_point])
	right_sorted_list = merge_sort(unsorted_list[mid_point:])


	return merge(left_sorted_list, right_sorted_list)


def merge(left_list, right_list):


	sorted_list = []
	left_list_index = 0
	right_list_index = 0

	while left_list_index < len(left_list) and right_list_index < len(right_list):
		if left_list[left_list_index] < right_list[right_list_index]:
			sorted_list.append(left_list[left_list_index])
			left_list_index += 1
		else:
			sorted_list.append(right_list[right_list_index])
			right_list_index += 1

	sorted_list = sorted_list + left_list[left_list_index:]
	sorted_list = sorted_list + right_list[right_list_index:]

	return sorted_list


def test():

	# this is done to increase the default recursion limit to rest our quicksor against 
	# list built-in sort functionality for time comparison
	# import sys
	# sys.setrecursionlimit(1000000)
	# print(sys.getrecursionlimit())


	import time
	a = [6,2,7,89,23,80,342,12,6,0,1,5,2,67,23,4,5,12,3,4,667,23,78,2,9,3,63,23]
	start =time.time()
	# Notice here since merge sort is not inplace it produces a new list of sorted elements
	# i.e is needs to be reassigned to initial variable
	a = merge_sort(a)
	print('Time it took to sort using our merge_sort  %s seconds'%(time.time()-start))

	# print(a)
	a = [6,2,7,89,23,80,342,12,6,0,1,5,2,67,23,4,5,12,3,4,667,23,78,2,9,3,63,23]
	start =time.time()
	a.sort()
	print('Time it took to sort using inbuilt sort %s seconds'%(time.time()-start))	

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
	a = merge_sort(a)
	print('Time it took to sort 100000 items using our merge_sort  %s seconds'%(time.time()-start))

test()


# Results 

# Time it took to sort using our merge_sort  0.00019907951355 seconds
# Time it took to sort using inbuilt sort 8.10623168945e-06 seconds
# Time it took to sort 100000 items using sort() function of list 0.0194790363312 seconds
# Time it took to sort 100000 items using our merge_sort  0.561465024948 seconds