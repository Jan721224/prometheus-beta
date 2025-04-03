import pytest
from src.smallest_rounding_number import find_smallest_rounding_number

def test_basic_cases():
    # Basic scenarios
    assert find_smallest_rounding_number([1, 2, 3]) == 4  # 1+2+3 = 6, add 4 to make 10
    assert find_smallest_rounding_number([3, 1, 2]) == 4  # Order shouldn't matter
    assert find_smallest_rounding_number([0]) == 5  # Zero case
    assert find_smallest_rounding_number([]) == 5  # Empty list case

def test_already_multiple_of_5():
    # When sum is already a multiple of 5
    assert find_smallest_rounding_number([5, 0]) == 5
    assert find_smallest_rounding_number([10]) == 5

def test_large_numbers():
    # Test with larger numbers
    assert find_smallest_rounding_number([7, 13, 22]) == 3  # 42 + 3 = 45

def test_negative_numbers():
    # Test with negative numbers
    assert find_smallest_rounding_number([-2, -3, 1]) == 4  # Handles negative numbers correctly

def test_error_handling():
    # Type errors
    with pytest.raises(TypeError):
        find_smallest_rounding_number("not a list")
    
    with pytest.raises(TypeError):
        find_smallest_rounding_number(None)
    
    # Value errors
    with pytest.raises(ValueError):
        find_smallest_rounding_number([1, 2, '3'])
    
    with pytest.raises(ValueError):
        find_smallest_rounding_number([1.5, 2, 3])

def test_complex_cases():
    # More complex scenarios
    assert find_smallest_rounding_number([11, 19, 20]) == 5
    assert find_smallest_rounding_number([-5, 10, 2]) == 3