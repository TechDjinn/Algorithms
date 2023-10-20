from math import sqrt 

def isPrime(candidate):
    """
    Description:
        Check if the provided integer is a prime number.
        Time complexity: approximately O(sqrt(n))

    Arguments:
        candidate (int): number to check >= 0

    Returns:
        bool: True if the candidate is prime. False otherwise.
    """
    err_msg = "Invalid input: 'candidate' must be a non-negative integer."
    assert isinstance(candidate, int), err_msg
    assert candidate >= 0, err_msg

    # Special cases
    if candidate <= 1:
        return False
    elif candidate == 2:
        return True
    elif candidate % 2 == 0:
        return False
    
    # Check all odd number up to sqrt of candidate.
    for i in range(3, int(sqrt(candidate) + 1), 2):
        if candidate % i == 0:
            return False
        
    return True