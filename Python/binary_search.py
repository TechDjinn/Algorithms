def binary_search(element_to_find, list_to_search):
    """
    Description:
        Perform a binary search to find if the target element is in the list.
        Time complexity: O(log n)

    Arguments:
        element_to_find (any): The element to search for.
        list_to_search (list): The list in which to perform the search.

    Returns:
        bool: True if the target element is found. False otherwise.

    IMPORTANT:
        Please observe that the list MUST be sorted in acending order.
    """
    assert isinstance(list_to_search, list), "'list_to_search' must a list."

    # Handle edge cases:
    # Empty list or element is outside of the range of the list.
    if list_to_search == []:
        return False
    if element_to_find > list_to_search[-1]:
        return False
    if element_to_find < list_to_search[0]:
        return False
    
    low = 0
    high = len(list_to_search) - 1

    while low <= high:
        middle = (low + high) // 2

        if list_to_search[middle] == element_to_find:
            return True
        elif list_to_search[middle] > element_to_find:
            high = middle - 1   # Search left half.
        else:
            low = middle + 1    # Search right half.

    return False