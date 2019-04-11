def shell_sort(array):
	length = len(array)
	gap = round(length/2)
	while gap >0:
		for i in range(gap):
			for j in range(i,length,gap):
				k=j
				while k>0:
					if array[k]<array[k-gap]:
						x = array[k]
						array[k]=array[k-gap]
						array[k-gap]=x
						k = k-gap
					else:
						break
		gap= gap//2
	return array

