"""
Prime Numbers are of the form 6k<+->1
a = 6k-1
b = 6k+1
"""
number = 600851475143

largest_prime = 1
k = 1

while k < number:
	k6 = k*6   # Just to avoid the multiple multiplication operations
	a = k6 - 1
	b = k6 + 1

	if number%a == 0:
		number = number/a
		largest_prime = a
	elif number%b == 0:
		number = number/b
		largest_prime = b
	k += 1


print(largest_prime)
