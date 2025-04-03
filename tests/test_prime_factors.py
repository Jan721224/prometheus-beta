import pytest
from src.prime_factors import prime_factors

def test_prime_factors_basic():
    """Test basic prime factorization scenarios."""
    assert prime_factors(120) == [2, 2, 2, 3, 5]
    assert prime_factors(84) == [2, 2, 3, 7]
    assert prime_factors(13) == [13]  # Prime number
    assert prime_factors(1) == []  # Edge case

def test_prime_factors_large_numbers():
    """Test prime factorization of larger numbers."""
    assert prime_factors(2310) == [2, 3, 5, 7, 11]
    assert prime_factors(24) == [2, 2, 2, 3]

def test_prime_factors_error_handling():
    """Test error handling for invalid inputs."""
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factors(0)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factors(-10)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factors(3.14)
    
    with pytest.raises(ValueError, match="Input must be a positive integer"):
        prime_factors("not a number")