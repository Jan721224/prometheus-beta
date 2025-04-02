def reverse_vowels_substring(s: str, start: int, end: int) -> str:
    """
    Reverse the vowels within a specified substring of a given string.

    Args:
        s (str): The input string
        start (int): The starting index of the substring (inclusive)
        end (int): The ending index of the substring (exclusive)

    Returns:
        str: A new string with vowels in the specified substring reversed

    Raises:
        ValueError: If start or end indices are out of bounds
        ValueError: If start index is greater than end index
    """
    # Validate input indices
    if start < 0 or end > len(s) or start > end:
        raise ValueError("Invalid substring indices")

    # Define vowels (both lowercase and uppercase)
    vowels = set('aeiouAEIOU')

    # Convert string to list for easy manipulation
    chars = list(s)

    # Create a list of vowel indices in the substring
    vowel_indices = [i for i in range(start, end) if chars[i] in vowels]

    # Get the vowels in the substring and reverse them
    substring_vowels = [chars[i] for i in vowel_indices]
    substring_vowels.reverse()

    # Create a new list to build the result
    result_chars = chars.copy()

    # Replace vowels in the substring with reversed vowels
    for original_index, reversed_vowel in zip(vowel_indices, substring_vowels):
        result_chars[original_index] = reversed_vowel

    return ''.join(result_chars)