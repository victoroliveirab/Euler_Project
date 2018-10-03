from functools import reduce

bound = 20

def primes_up_to(bound):
	a = [True]*(bound+1)
	a[0]=a[1]=False
	
	for i in range(2,bound+1):
		if a[i] is True:
			for j in range(i**2,bound+1,i):
				#print(j)
				a[j] = False

	primes=[]
	for i in range(len(a)):
		if a[i]:
			primes.append(i)
	return primes

primes = primes_up_to(bound)
powers = []
for p in primes:
	root = p**int(pow(bound,1/p)) 
	powers.append(root)
	# once the p-th root of bound truncated is equal to 1,
	# all the subsequent roots are also truncated to 1
	if root == p:
		powers.extend(primes[len(powers):])
		break

prod = reduce(lambda x,y: x*y, powers, 1)
print(prod)




