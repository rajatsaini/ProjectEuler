"""
Number found using iterations
"""
numbers = 104750

primes = set()
primes.add(2)
primes.add(3)

flag = True

for i in range(5,numbers,2):

	for prime in primes:
		if i%prime==0:
			flag = False
			break

	if flag == True:
		primes.add(i)
	flag = True

d = list(primes)
d.sort()
print(d)
print(len(d))