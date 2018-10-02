def fib(bound):
	l=[0,1]
	s=0
	while l[-1] <= bound:
		l.append(l[-1] + l[-2])
		if not l[-1]%2:
			s+=l[-1]
	return s

print(fib(4000000))
