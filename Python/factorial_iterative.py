def factorial_iterative(n):
	"""
	Description:
		Calculate and return the factorial of 'n' (n!);
		using a iterative approach.
		Time complexity: O(n)
	
	Arguments:
		n: Integer >= 0
	
	Returns:
		int: Factorial of 'n' (n!)
	"""
	assert isinstance(n, int) and n >= 0, "n must be positive int"
	
	# Find n! using an iterative approach.
	result = 1
	for i in range(1, n + 1):
		result *= i

	return result