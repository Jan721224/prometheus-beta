def find_smallest_rounding_number(arr):
    """
    Find the smallest positive integer that, when added to the sum of all numbers 
    in an array, results in a multiple of 5.
    
    Args:
        arr (list): A list of integers
    
    Returns:
        int: The smallest positive integer that rounds the sum to a multiple of 5
    
    Raises:
        TypeError: If input is not a list
        ValueError: If list contains non-integer elements
    """
    # Input validation
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Check for non-integer elements
    if not all(isinstance(x, int) for x in arr):
        raise ValueError("All elements must be integers")
    
    # Calculate the current sum of the array
    current_sum = sum(arr)
    
    # Find the smallest positive number to round to next multiple of 5
    remainder = current_sum % 5
    if remainder == 0:
        return 5
    
    return 5 - remainder