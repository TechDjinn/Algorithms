def selectionSort(array):
	N = len(array)
	for i in range(N - 1):
		# Find index of the minimum element in the unsorted portion.
		min_index = i
		for j in range(i + 1, N):
			if array[j] < array[min_index]:
				min_index = j
		# Swap the minimum element to right index.
		array[i], array[min_index] = array[min_index], array[i]

	return array