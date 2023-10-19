def linear_search(element_to_find, list_to_search):
    """
    Description:
        Perform a linear search to find the target element in the content.

    Arguments:
        element_to_find (any): The element to search for.
        list_to_search (list): The list in which to perform the search.

    Returns:
        bool: True if the target element is found, False otherwise.
    """
    for item in list_to_search:
        if item == element_to_find:
            return True
    
    return False