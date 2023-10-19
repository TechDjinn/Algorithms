def factorial_recursive(n):
	"""
	Description:
        Calculate and return the factorial of 'n' (n!),
		using a recursive approach.
	
	Arguments:
        n: Integer >= 0

    Returns:
        int: Factorial of 'n' (n!)
    """
	assert isinstance(n, int) and n >= 0
	
	# Find n! using recursion.
	if n <= 1:
		return 1
	else:
		return n * factorial_recursive(n-1)