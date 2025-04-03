def remove_even_numbers_and_sum(arr):
    """
    Remove even numbers from the input array and return their sum.

    Args:
        arr (list): Input list of integers.

    Returns:
        int: Sum of even numbers removed from the input list.

    Raises:
        TypeError: If input is not a list or contains non-integer elements.
    """
    # Validate input is a list
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    # Validate all elements are integers
    if not all(isinstance(x, int) for x in arr):
        raise TypeError("All elements must be integers")
    
    # Separate even and odd numbers
    even_numbers = [x for x in arr if x % 2 == 0]
    odd_numbers = [x for x in arr if x % 2 != 0]
    
    # Update original list to contain only odd numbers
    arr.clear()
    arr.extend(odd_numbers)
    
    # Return sum of even numbers
    return sum(even_numbers)