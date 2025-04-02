import pytest
from src.find_integer_index import find_integer_index

def test_find_integer_index_basic():
    """Test basic functionality of finding an existing integer in the list."""
    assert find_integer_index([1, 2, 3, 4, 5], 3) == 2
    assert find_integer_index([1, 2, 3, 4, 5], 1) == 0
    assert find_integer_index([1, 2, 3, 4, 5], 5) == 4

def test_find_integer_index_not_found():
    """Test when the target integer is not in the list."""
    assert find_integer_index([1, 2, 3, 4, 5], 6) == -1
    assert find_integer_index([1, 2, 3, 4, 5], 0) == -1

def test_find_integer_index_empty_list():
    """Test behavior with an empty list."""
    assert find_integer_index([], 1) == -1

def test_find_integer_index_multiple_occurrences():
    """Test that the function returns the first occurrence."""
    assert find_integer_index([1, 2, 3, 2, 1], 2) == 1

def test_find_integer_index_types():
    """Test that the function works with different integer types."""
    assert find_integer_index([1, 2, 3, 4, 5], 3) == 2
    assert find_integer_index([-1, -2, 0, 1, 2], -2) == 1