def isPalindrome(candidate, case_sensitive = False, ignore_spaces = True):
    """
    Description:
        Check if 'candidate' string or integer is a palindrome.
        (by default not case-sensitive and ignores spaces)

    Arguments:
        candidate (str OR int): element to check.
        case_sensitive (bool): determine if case-sensitive [Optional]
        ignore_spaces (bool): determine if spaces is ignored [Optional]

    Returns:
        bool: True if the element is a palindrome. False otherwise.
    """
    # Assert that 'candidate' is a string or an integer.
    assert type(candidate) in [str, int], "'candidate' must be int OR str"

    # Typecasting integer to string
    if type(candidate) == int:
        candidate = str(candidate)

    # Handle optional arguments
    if case_sensitive == False:
        # Force all characters to lowercase.
        candidate = candidate.lower()
    if ignore_spaces == True:
        # Remove all spaces / ignores spaces in string.
        candidate = "".join(candidate.split())

    # Handle empty string
    if len(candidate) == 0:
        return False
    
    # Recursion
    elif len(candidate) == 1:
        return True
    elif len(candidate) == 2:
        return candidate[0] == candidate[-1]
    else:
        bool_1 = candidate[0] == candidate[-1]
        bool_2 = isPalindrome(candidate[1:-1], case_sensitive, ignore_spaces)
        return bool_1 and bool_2