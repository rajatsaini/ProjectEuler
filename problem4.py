def isPalin(n):
	li = list(str(n))
	li_old = list(str(n))
	li.reverse()
	if li==li_old:
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
