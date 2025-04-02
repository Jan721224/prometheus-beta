def search_matrix(matrix, target):
    """
    Search for a target integer in an M x N matrix.
    
    The matrix is assumed to be sorted in ascending order from left to right 
    and top to bottom for an efficient search.
    
    Args:
        matrix (List[List[int]]): A 2D matrix of integers
        target (int): The integer to search for
    
    Returns:
        bool: True if the target exists in the matrix, False otherwise
    
    Raises:
        TypeError: If matrix is not a list of lists or target is not an integer
        ValueError: If the matrix is empty or contains non-integer elements
    
    Time Complexity: O(log(m*n))
    Space Complexity: O(1)
    
    Example:
        >>> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        >>> search_matrix(matrix, 3)
        True
        >>> search_matrix(matrix, 13)
        False
    """
    # Validate input
    if not isinstance(matrix, list) or not matrix:
        return False
    
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("Matrix must be a list of lists")
    
    # Handle empty matrix
    if not matrix[0]:
        return False
    
    # Validate target and matrix elements
    if not isinstance(target, int):
        raise TypeError("Target must be an integer")
    
    # Check if all rows have the same length and contain only integers
    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise ValueError("All rows must have the same length")
    
    if not all(all(isinstance(elem, int) for elem in row) for row in matrix):
        raise ValueError("Matrix must contain only integers")
    
    # Treat matrix as a flattened sorted array
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        # Convert mid to 2D coordinates
        row = mid // n
        col = mid % n
        
        mid_value = matrix[row][col]
        
        if mid_value == target:
            return True
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False