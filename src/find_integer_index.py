def find_integer_index(nums, target):
    """
    Find the index of the first occurrence of a target value in a list of integers.

    Args:
        nums (list): A list of integers to search through
        target (int): The integer value to find in the list

    Returns:
        int: The index of the first occurrence of the target value,
             or -1 if the target is not found in the list

    Examples:
        >>> find_integer_index([1, 2, 3, 4, 5], 3)
        2
        >>> find_integer_index([1, 2, 3, 4, 5], 6)
        -1
        >>> find_integer_index([], 1)
        -1
    """
    # Check for empty list first
    if not nums:
        return -1
    
    # Iterate through the list with enumeration to get both index and value
    for index, value in enumerate(nums):
        if value == target:
            return index
    
    # If target is not found, return -1
    return -1