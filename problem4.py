def isPalin(n):
	s = str(n)
	if s==s[::-1]:
		return True
	return False

m = 1

for i in range(999,800,-1):
	for j in range(999,700,-1):
		n = i*j
		if isPalin(n):
			m = n
			break
	if m==n:
		break
print(m)
