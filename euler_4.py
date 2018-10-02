def largest_palindrome(n):
	x=0
	largest_bound = 10**n - 1
	lowest_bound = 10**(n-1)
	for m in range(largest_bound,lowest_bound - 1,-1):
		for n in range(largest_bound,lowest_bound - 1,-1):
			y = m*n
			if str(y)==str(y)[::-1]:
				if y > x:
					x=y
	return x


print(largest_palindrome(3))