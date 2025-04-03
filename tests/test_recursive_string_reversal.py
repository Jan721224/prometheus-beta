import pytest
from src.recursive_string_reversal import recursive_reverse_string

def test_recursive_reverse_string_basic():
    """Test basic string reversal"""
    assert recursive_reverse_string("hello") == "olleh"
    assert recursive_reverse_string("world") == "dlrow"

def test_recursive_reverse_string_mixed_case():
    """Test string reversal with mixed case"""
    assert recursive_reverse_string("Hello World") == "dlroW olleH"
    assert recursive_reverse_string("PyThOn") == "nOhTyP"

def test_recursive_reverse_string_single_char():
    """Test single character string"""
    assert recursive_reverse_string("a") == "a"
    assert recursive_reverse_string("Z") == "Z"

def test_recursive_reverse_string_empty_string():
    """Test empty string"""
    assert recursive_reverse_string("") == ""

def test_recursive_reverse_string_with_spaces():
    """Test string with multiple spaces"""
    assert recursive_reverse_string("a b c") == "c b a"

def test_recursive_reverse_string_invalid_input():
    """Test invalid input raises appropriate exceptions"""
    # Non-string input
    with pytest.raises(TypeError, match="Input must be a string"):
        recursive_reverse_string(123)
    
    # Invalid characters
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello123")
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello!")
    with pytest.raises(ValueError, match="Input must contain only letters and spaces"):
        recursive_reverse_string("hello_world")