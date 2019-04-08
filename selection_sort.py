##### O(n^2)
##### Descend

def selection_sort(a):
	length = len(a)
	for i in range(length):
		for j in range(i+1,length):
			if a[i]>a[j]:
				b = a[i]
				a[i] = a[j]
				a[j] = b
	return a





