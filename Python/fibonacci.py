def fibonacci(n):
    """
    Description:
        Finds the first 'n' fibonacci numbers.

    Arguments:
        n (int): number of fibonacci numbers.

    Returns:
        list: a list of the first 'n' fibonacci numbers.
    """
    assert isinstance(n, int) and n >= 1, "'n' must be a positive int."
    
    fibonacci_list = [0, 1]
    a = fibonacci_list[0]
    b = fibonacci_list[1]
    c = a + b

    while len(fibonacci_list) < n:
        fibonacci_list.append(c)
        (a, b) = (b, c)
        c = a + b

    return fibonacci_list[:n]