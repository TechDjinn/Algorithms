def gcd(a, b):
    """
    Description:
        Finds the greatest common denominator of two positive integers.

    Arguments:
        a (int): one of the numbers.
        b (int): the other the numbers.

    Returns:
        int: the greatest common denominator

    Explaination of principle:
        The Euclidean algorithm is based on the principle 
        that the greatest common divisor of two numbers 
        does not change if the larger number is replaced by 
        its difference with the smaller number.
    """
    assert isinstance(a, int) and a > 0, "'a' must be a positive int"
    assert isinstance(b, int) and b > 0, "'b' must be a positive int"
    
    # Tip: See explaination of principle in docstring.
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

