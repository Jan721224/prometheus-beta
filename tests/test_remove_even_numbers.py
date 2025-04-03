import pytest
from src.remove_even_numbers import remove_even_numbers_and_sum

def test_remove_even_numbers_basic():
    """Test basic functionality of removing even numbers and returning their sum."""
    arr = [1, 2, 3, 4, 5, 6]
    result = remove_even_numbers_and_sum(arr)
    assert result == 12  # sum of 2, 4, 6
    assert arr == [1, 3, 5]  # only odd numbers remain

def test_remove_even_numbers_no_evens():
    """Test case where no even numbers are present."""
    arr = [1, 3, 5, 7]
    result = remove_even_numbers_and_sum(arr)
    assert result == 0
    assert arr == [1, 3, 5, 7]

def test_remove_even_numbers_only_evens():
    """Test case where only even numbers are present."""
    arr = [2, 4, 6, 8]
    result = remove_even_numbers_and_sum(arr)
    assert result == 20
    assert arr == []

def test_remove_even_numbers_empty_list():
    """Test behavior with an empty list."""
    arr = []
    result = remove_even_numbers_and_sum(arr)
    assert result == 0
    assert arr == []

def test_remove_even_numbers_invalid_input_type():
    """Test error handling for non-list inputs."""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_even_numbers_and_sum("not a list")

def test_remove_even_numbers_non_integer_elements():
    """Test error handling for non-integer elements."""
    with pytest.raises(TypeError, match="All elements must be integers"):
        remove_even_numbers_and_sum([1, 2, "3", 4])

def test_remove_even_numbers_negative():
    """Test functionality with negative numbers."""
    arr = [-1, -2, -3, -4, 0, 1, 2]
    result = remove_even_numbers_and_sum(arr)
    assert result == -4  # -2, -4, 0, 2
    assert arr == [-1, -3, 1]