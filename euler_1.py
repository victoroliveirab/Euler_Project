#from datetime import datetime
#startTime = datetime.now()
n=3
x = 10**n
x-=1
x3 = x
x5 = x
x15 = x
while (x3%3 != 0):
	x3-=1

while (x5%5 != 0):
	x5-=1

while (x15%15 != 0):
	x15-=1

sum_of_m_3 = (3 + x3)*(x3/3)//2
#print(sum_of_m_3)
sum_of_m_5 = (5 + x5)*(x5/5)//2
#print(sum_of_m_5)
sum_of_m_15 = (15 + x15)*(x15/15)//2
#print(sum_of_m_15)

total = sum_of_m_3+sum_of_m_5-sum_of_m_15

print(total)

#print(datetime.now() - startTime)