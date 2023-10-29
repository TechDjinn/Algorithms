def longestCommonPrefix(strs):      
    # Declaration of variable
    i = 0

    # Check for longest common prefix
    for i in range(1, len(strs[0]) + 1):
        # Compare each string agains the prefix of string at index 0.
        for word in strs:
            if word[:i] != strs[0][:i]:
                # Not the same.
                return strs[0][:i-1]
                
    # All strings are equal.
    return strs[0][:i]