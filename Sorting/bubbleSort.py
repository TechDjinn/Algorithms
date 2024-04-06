def main():
	# Example lists
	list_1 = [4, 6, 2, 4, 6, 8, 3]
	list_2 = [7, 15, 9, 5, 12, 19, 0, 11]
	list_3 = []
	list_4 = [14]
	list_5 = [8, 2, 12, 15, 4, 5, 21, 17]
	list_6 = [2, 7, 13, 12, 9, 7, 11, 12]

	# Print the four example lists (unsorted)
	print("UNSORTED LISTS")
	print("List #1:", list_1)
	print("List #2:", list_2)
	print("List #3:", list_3)
	print("List #4:", list_4)
	print("List #5:", list_5)
	print("List #6:", list_6)

	# Sort the example lists
	list_1 = bubbleSort(list_1)
	list_2 = bubbleSort(list_2, reverse = False)
	list_3 = bubbleSort(list_3)
	list_4 = bubbleSort(list_4)
	list_5 = bubbleSort(list_5, reverse = True)
	list_6 = bubbleSort(list_6, True)

	# Print the four example lists (sorted ascending)
	print("\nSORTED LISTS | (Ascending order)")
	print("List #1:", list_1)
	print("List #2:", list_2)
	print("List #3:", list_3)
	print("List #4:", list_4)

	# Print the four example lists (sorted descending)
	print("\nSORTED LISTS | (Descending order)")
	print("List #5:", list_5)
	print("List #6:", list_6)


def bubbleSort(arr, reverse = False):
	"""
	Sorts a list in ascending or descending order; using BubbleSort.

	Parameters:
		arr (list): input list to be sorted.
		reverse (bool, optional): ascending order if False (default).

	Returns:
		list: The sorted list in the specified order (ascending/descending)
	
	Behavior:
		1) If the input list 'arr' is empty or contains single element,
		it's considered sorted.

		2) The 'reverse' parameter controls the sorting order.
		False (default): ascending order (smallest to largest)
		True: descending order (largest to smallest)

	Usage:
		# Sort in ascending order
		sorted_list = bubbleSort([5, 8, 2, 9, 12])

		# Sort in descending order
		sorted_list = bubbleSort([5, 8, 2, 9, 12], reverse = True)
	"""
	# If list is empty or have just one element; then already sorted.
	if len(arr) <= 1:
		return arr

	# Sort the list in correct order.
	for i in range(len(arr) - 1):
		# We'll fill the end with more and more correctly placed elements.
		for j in range(len(arr) - (i + 1)):
			if reverse == False:
				# If left element is bigger than the right; swap them.
				if arr[j] > arr[j + 1]:
					# Swapping elements.
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
			else:
				# If left element is smaller than the right; swap them.
				if arr[j] < arr[j + 1]:
					# Swapping elements.
					arr[j], arr[j + 1] = arr[j + 1], arr[j]

	# Return the list; that's now actually sorted.
	return arr


if __name__ == "__main__":
	main()