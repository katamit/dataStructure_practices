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
	a = [6,2,7,89,23,80,342,12,6,0,1,5,2,67,23,4,5,12,3,4,667,23,78,2,9,3,63,23]
	quickSort(a, 0, len(a)-1)
	print(a)

test()