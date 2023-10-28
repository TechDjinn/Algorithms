def twoSum(nums, target):
    """
    Description:
        Given a list of integers 'nums' and an integer 'tagret',
        return indices of the two numbers that add up to target.
        If no such indices exist the function returns an empty list.
        Time complexity: O(n^2) | Ω(1)

    Arguments:
        nums (list): list of integers
        target (int): integer that the two indices shall sum.

    Returns:
        list: list of the two indices for the two numbers, or empty list.
    """
    # Check each pair to find the matching pair.
    for i in range(len(nums)-1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                # Found! Return indices.
                return [i, j]

    # None exsist, so return an empty list.
    return []