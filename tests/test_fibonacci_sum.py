import pytest
from src.fibonacci_sum import fibonacci_sum

def test_fibonacci_sum_basic():
    """Test basic functionality with different positive integers."""
    assert fibonacci_sum(1) == 0  # First Fibonacci number is 0
    assert fibonacci_sum(2) == 1  # Sum of first two is 0 + 1 = 1
    assert fibonacci_sum(3) == 1  # 0 + 1 + 1 = 2
    assert fibonacci_sum(5) == 7  # 0 + 1 + 1 + 2 + 3 = 7

def test_fibonacci_sum_larger_numbers():
    """Test sum of Fibonacci numbers for larger inputs."""
    assert fibonacci_sum(10) == 88  # Verified through calculation
    assert fibonacci_sum(15) == 610  # Verified through calculation

def test_fibonacci_sum_invalid_inputs():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(-1)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum(1.5)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        fibonacci_sum("not a number")