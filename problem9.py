for k in range(300,650):
	for i in range(100,300):
		for j in range(300,500):
			if (i**2 )+ (j**2) == k**2:
				if i+j+k == 1000:
					print(i,j,k)