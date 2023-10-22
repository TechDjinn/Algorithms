def fibonacci(n):
    """
    Description:
        Finds the first 'n' fibonacci numbers.

    Arguments:
        n (int): number of fibonacci numbers.

    Returns:
        list: a list of the first 'n' fibonacci numbers.
    """
    assert isinstance(n, int) and n >= 0, "'n' must be a non-negative int."
    
    fibonacci = [0, 1]

    for i in range(1, n - 1):
        fibonacci.append(fibonacci[i] + fibonacci[i-1])

    return fibonacci[:n]