##This technique stars from the initial problem set and divides it into small subproblems.
# After the solution of s abuprogram has been determined, we store the result to that particular subprolem. 
# In the furture, when this subproblem is encountered, we only return the pre-computed result

# Here we use the fibonacci series calcuation to demonstrate the MEMOIZATION TECHNIQUE

#EX of fibonacci series : 1 1 2 3 5 8
# i.e fin(n) = fib(n-1) + fib(n-2)


#without momization
def fib(n):
	if n <= 2:
		return 1

	return fib(n-1) + fib(n-2)

# using memoization 
look_up = {}
def dyna_fib(n):
	if n <= 2:
		look_up[n]  =1
	if n not in look_up:
		look_up[n] = dyna_fib(n-1) + dyna_fib(n-2)
	return look_up[n]


#using memoization with tabular data
def tabular_fib(n):
	results = [1,1]

	for i in range(2, n):
		results.append( results[i-1] + results[i-2] )

	return results[-1]


def test():
	print('40th number calucation in fibonacci series without MEMOIZATION')
	import time
	start = time.time()
	print(fib(40))
	print('time it took to calculate the 100th fibonacci number %s seconds'%(time.time() - start))

	print('-'*70)

	print('40th number calucation in fibonacci series with MEMOIZATION')
	import time
	start = time.time()
	print(dyna_fib(40))
	print('time it took to calculate the 100th fibonacci number %s seconds'%(time.time() - start))

	print('-'*70)

	print('40th number calucation in fibonacci series with tabular MEMOIZATION')
	import time
	start = time.time()
	print(tabular_fib(40))
	print('time it took to calculate the 100th fibonacci number %s seconds'%(time.time() - start))

test()

#Result

# 40th number calucation in fibonacci series without MEMOIZATION
# 102334155
# time it took to calculate the 100th fibonacci number 24.0931310654 seconds
# ----------------------------------------------------------------------
# 40th number calucation in fibonacci series with MEMOIZATION
# 102334155
# time it took to calculate the 40th fibonacci number 2.8133392334e-05 seconds
# ----------------------------------------------------------------------
# 40th number calucation in fibonacci series with tabular MEMOIZATION
# 102334155
# time it took to calculate the 40th fibonacci number 2.09808349609e-05 seconds
