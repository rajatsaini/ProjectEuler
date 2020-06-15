"""
Number found using iterations
"""
import math
numbers = 2000000

primes = []
primes.append(2)
primes.append(3)

flag = True
diff = 2
n = 0
count = 0
for i in range(5,numbers,diff):
	
	if n==2:
		n = 0
		continue

	sqroot = math.sqrt(i) +2 

	for prime in primes:
		if prime > sqroot:
			break
		# print(prime)
		count += 1
		if i%prime==0:
			flag = False
			break

	if flag == True:
		primes.append(i)
	flag = True
	n += 1 

# d = list(primes)
# d.sort()
# print(d)
# print(primes)
print(count)
print(sum(primes))