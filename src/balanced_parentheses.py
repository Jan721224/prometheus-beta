def is_balanced_parentheses(s: str) -> bool:
    """
    Check if all parentheses in the given string are balanced.

    This function validates that every opening parenthesis has a corresponding 
    closing parenthesis in the correct order, supporting multiple types of 
    parentheses: (), [], and {}.

    Args:
        s (str): Input string to check for balanced parentheses

    Returns:
        bool: True if all parentheses are balanced, False otherwise

    Examples:
        >>> is_balanced_parentheses("()")
        True
        >>> is_balanced_parentheses("()[]{}")
        True
        >>> is_balanced_parentheses("(]")
        False
        >>> is_balanced_parentheses("([)]")
        False
        >>> is_balanced_parentheses("{[]}")
        True
    """
    # Dictionary to map closing to opening parentheses
    parentheses_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Stack to keep track of opening parentheses
    stack = []
    
    # Iterate through each character in the string
    for char in s:
        # If it's a closing parenthesis
        if char in parentheses_map:
            # If stack is empty or top of stack doesn't match corresponding opening parenthesis
            if not stack or stack[-1] != parentheses_map[char]:
                return False
            # Remove the matching opening parenthesis from stack
            stack.pop()
        
        # If it's an opening parenthesis, add to stack
        elif char in ['(', '[', '{']:
            stack.append(char)
    
    # Return True if stack is empty (all parentheses matched)
    return len(stack) == 0