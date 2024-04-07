def binarySearch(array, target, ascending_order = True):
	"""
	Search a sorted list 'array' for 'target'. 
	Returns index of 'target' if found. Else -1 to indicate not found.

	Parameters:
		array (list): sorted list to search.
		target (number): the element to search for.
		ascending_order (bool, optional): how list is sorted.

	Returns:
		integer: index of occurrence; or -1 if not found.
	
	Behavior:
		Search a sorted list for the specified target.

	Usage:
		/ Ascending ordered list
		binarySearch(array, target)

		/ Descending ordered list
		binarySearch(array, target, ascending_order = False)
	"""
	low = 0
	high = len(array) - 1
	middle = (high - low) // 2

	while low <= high:
		middle = int((low + high) / 2)

		# List in ascending order:
		if ascending_order:
			if array[middle] < target:
				low = middle + 1
			elif array[middle] > target:
				high = middle - 1
			else:
				return middle

		# List in descending order:
		else:
			if array[middle] > target:
				low = middle + 1
			elif array[middle] < target:
				high = middle - 1
			else:
				return middle

	# Target is not in the list/array
	return -1