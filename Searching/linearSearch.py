def main():
	# Example lists
	sorted_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	sorted_2 = [10, 20, 30, 40, 50, 60, 70, 80]
	unsorted_1 = [1, 6, 3, 2, 9, 0, 5, 7, 4, 8]
	unsorted_2 = [10, 80, 60, 30, 20, 70, 50, 40]

	target_1 = 8
	target_2 = 60

	# Print the four example lists; and target
	print("TARGETS")
	print("Target_1:", target_1)
	print("Target_2:", target_2)
	print("")

	print("LISTS")
	print("Sorted #1:", sorted_1)
	result = linearSearch(sorted_1, target_1)
	if result != -1:
		print(f"\t{target_1} | index {result}")
	else:
		print(f"\t{target_1} is not in the list.")
	result = linearSearch(sorted_1, target_2)
	if result != -1:
		print(f"\t{target_2} | index {result}")
	else:
		print(f"\t{target_2} is not in the list.")

	print("Sorted #2:", sorted_2)
	result = linearSearch(sorted_2, target_1)
	if result != -1:
		print(f"\t{target_1} | index {result}")
	else:
		print(f"\t{target_1} is not in the list.")
	result = linearSearch(sorted_2, target_2)
	if result != -1:
		print(f"\t{target_2} | index {result}")
	else:
		print(f"\t{target_2} is not in the list.")

	print("Unsorted #1:", unsorted_1)
	result = linearSearch(unsorted_1, target_1)
	if result != -1:
		print(f"\t{target_1} | index {result}")
	else:
		print(f"\t{target_1} is not in the list.")
	result = linearSearch(unsorted_1, target_2)
	if result != -1:
		print(f"\t{target_2} | index {result}")
	else:
		print(f"\t{target_2} is not in the list.")

	print("Unsorted #2:", unsorted_2)
	result = linearSearch(unsorted_2, target_1)
	if result != -1:
		print(f"\t{target_1} | index {result}")
	else:
		print(f"\t{target_1} is not in the list.")
	result = linearSearch(unsorted_2, target_2)
	if result != -1:
		print(f"\t{target_2} | index {result}")
	else:
		print(f"\t{target_2} is not in the list.")


def linearSearch(lst, target):
	"""
	Search a list for 'target' using LinearSearch.
	If found: return index of first occurrence. If not: return -1

	Parameters:
		lst (list): input list to be searched.
		target (integer): number to search for.

	Returns:
		integer: index of first occurrence; or -1 if not found.
	
	Behavior:
		If found: function returns the index of the first occurrence.
		If not found: return -1 to indicate 'target' is not in the list.

	Usage:
		linearSearch(list, target)
	"""
	for index in range(len(lst)):
		if lst[index] == target:
			return index

	# Target is not in the list; return error-code
	return -1


if __name__ == "__main__":
	main()