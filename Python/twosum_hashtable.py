def twoSum(nums, target):
    """
    Description:
        Given a list of integers 'nums' and an integer 'tagret',
        return indices of the two numbers that add up to target.
        If no such indices exist the function returns an empty list.
        Time complexity: O(n) | Ω(1)

    Arguments:
        nums (list): list of integers
        target (int): integer that the two indices shall sum.

    Returns:
        list: list of the two indices for the two numbers, or empty list.
    """
    # Dict/hashtable for numbers already seen; and their index.
    seen = {}

    # Go through each element in the list.
    for i in range(len(nums)):
        # Check if a match is in the dict/hashtable.
        if target - nums[i] in seen:
            # Found! Return the indices.
            return [seen[target - nums[i]], i]
            
        # Add to dict/hashtable.
        seen[nums[i]] = i

    # None exsist, so return an empty list.
    return []