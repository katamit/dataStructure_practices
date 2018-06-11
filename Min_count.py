
import math
def get_min_coins(sum, denomiations):
	denomiations = sorted(denomiations, reverse = True)
	
	min_number = math.inf
	orders = {}
	for i in range(len(denomiations)):
		current_num = 0
		copy_sum = sum
		sequence = []
		for den in denomiations[i:]:
			# if copy_sum > 0:
			divi = copy_sum// den
			current_num += divi 
			copy_sum = copy_sum%den
			sequence.append((den, divi))
			if copy_sum <= 0 and current_num < min_number:
				min_number = current_num
				if min_number in orders:
					orders[min_number].append()
				else:
					orders[min_number] = [sequence]
				break

	return min_number, orders[min_number]

print(get_min_coins(12,[8,5,1]))

