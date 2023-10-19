def binary_search(element_to_find, list_to_search):
    """
    Description:
        Perform a binary search to find if the target element is in the list.

    Args:
        element_to_find (any): The element to search for.
        list_to_search (list): The list in which to perform the search.

    Returns:
        bool: True if the target element is found, False otherwise.
    """
    assert isinstance(list_to_search, list); "'list_to_search' must a list."
    
    low = 0
    high = len(list_to_search) - 1

    while low <= high:
        middle = (low + high) // 2

        if list_to_search[middle] == element_to_find:
            return True
        elif list_to_search[middle] > element_to_find:
            high = middle - 1
        else:
            low = middle + 1

    return False