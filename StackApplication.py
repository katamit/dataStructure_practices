
#this program demonstrate the practical implemetation of Stack.
# In a bracket balance check application
# stack are use at number of places other than these mainly:
	# Function calls
	# Recursion
	# Browser Back and forward button

from stack import Stack

def check_brackets(statement):
	stack = Stack()
	for ch in statement:
		if ch in ('{','[','('):
			stack.push(ch)
		elif ch in ('}',']',')'):
			last = stack.pop()
			if last == '{' and ch == '}':
				continue
			elif last == '[' and ch == ']':
				continue
			elif last == '(' and ch == ')':
				continue
			else:
				return False
	if stack._Stack__size == 0:
		return True
	else:
		return False


s1 = ("{(foo)(bar)}[hello](((this)is)a)test",
	 "{(foo)(bar)}[hello](((this)is)atest",
	 "{(foo)(bar)}[hello](((this)is)a)test))")


for s in s1:
	m = check_brackets(s)
	print("{}: {}".format(s,m))
	 