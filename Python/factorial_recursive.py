def factorial_recursive(n):
	"""
	Description:
		Calculate and return the factorial of 'n' (n!);
		using a recusive approach.
		Time complexity: O(n)
	
	Arguments:
		n: Integer >= 0
	
	Returns:
		int: Factorial of 'n' (n!)
	"""
	assert isinstance(n, int) and n >= 0, "n must be positive int"
	
	# Find n! using recursion.
	if n <= 1:
		return 1
	else:
		return n * factorial_recursive(n - 1)