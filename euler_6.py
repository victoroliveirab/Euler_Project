def sum_of_squares(num):
	return sum(x**2 for x in range(num+1))

def square_of_sum(num):
	return sum(x for x in range(num+1)) ** 2


def difference(num):
	return square_of_sum(num) - sum_of_squares(num)


print(difference(100))
