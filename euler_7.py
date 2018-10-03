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



bound = 1000000 #try and error found
print(primes_up_to(bound)[10000])
