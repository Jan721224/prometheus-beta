import pytest
from src.matrix_search import search_matrix

def test_search_matrix_basic():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 13) == False

def test_search_matrix_edge_cases():
    # Empty matrix
    assert search_matrix([], 5) == False
    
    # Single row matrix
    matrix_single_row = [[1,3,5,7]]
    assert search_matrix(matrix_single_row, 3) == True
    assert search_matrix(matrix_single_row, 8) == False
    
    # Single column matrix
    matrix_single_col = [[1],[3],[5],[7]]
    assert search_matrix(matrix_single_col, 3) == True
    assert search_matrix(matrix_single_col, 8) == False

def test_search_matrix_boundary_values():
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    
    # First element
    assert search_matrix(matrix, 1) == True
    
    # Last element
    assert search_matrix(matrix, 60) == True
    
    # Values just outside the matrix
    assert search_matrix(matrix, 0) == False
    assert search_matrix(matrix, 61) == False

def test_search_matrix_error_handling():
    # Invalid matrix type
    with pytest.raises(TypeError):
        search_matrix("not a matrix", 5)
    
    # Invalid matrix structure
    with pytest.raises(TypeError):
        search_matrix([1, 2, 3], 5)
    
    # Inconsistent row lengths
    with pytest.raises(ValueError):
        search_matrix([[1,2], [3,4,5]], 5)
    
    # Non-integer elements
    with pytest.raises(ValueError):
        search_matrix([[1,2], [3,'a']], 5)
    
    # Invalid target type
    with pytest.raises(TypeError):
        search_matrix([[1,2], [3,4]], '5')

def test_search_matrix_large_matrix():
    # Create a large sorted matrix
    large_matrix = [[i*10 + j for j in range(10)] for i in range(100)]
    
    # Test multiple values including edge cases
    assert search_matrix(large_matrix, 0) == True
    assert search_matrix(large_matrix, 999) == True
    assert search_matrix(large_matrix, 1000) == False
    assert search_matrix(large_matrix, -1) == False