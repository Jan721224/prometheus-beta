def reverse_string(input_str: str) -> str:
    """
    Reverse the given input string.

    Args:
        input_str (str): The input string to be reversed.

    Returns:
        str: The reversed version of the input string.

    Raises:
        TypeError: If the input is not a string.
    """
    # Check if input is a string
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string")
    
    # Return the reversed string
    return input_str[::-1]