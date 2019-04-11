def insert_sort(a):
	length= len(a)
	for i in range(length):
		j=i
		while j-1>=0:
			if a[j]<a[j-1]:
				b = a[j-1]
				a[j-1] = a[j]
				a[j] = b
				j -=1
			else:
				break
	return a

