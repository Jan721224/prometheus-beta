import pytest
from src.shortest_palindrome_substrings import find_shortest_palindrome_substrings

def test_basic_palindromes():
    """Test basic palindromic substring scenarios"""
    assert sorted(find_shortest_palindrome_substrings("aabaa")) == ['a', 'aa']
    assert sorted(find_shortest_palindrome_substrings("abcd")) == ['a', 'b', 'c', 'd']

def test_empty_string():
    """Test empty string input"""
    assert find_shortest_palindrome_substrings("") == []

def test_single_character():
    """Test single character input"""
    assert find_shortest_palindrome_substrings("a") == ['a']

def test_multiple_palindromes():
    """Test string with multiple shortest palindromes"""
    assert sorted(find_shortest_palindrome_substrings("racecar")) == ['a', 'c', 'r', 'racecar']

def test_repeated_characters():
    """Test string with repeated characters"""
    assert sorted(find_shortest_palindrome_substrings("aaaa")) == ['a', 'aa']

def test_invalid_input():
    """Test invalid input type"""
    with pytest.raises(TypeError):
        find_shortest_palindrome_substrings(123)
    with pytest.raises(TypeError):
        find_shortest_palindrome_substrings(None)

def test_complex_palindromes():
    """Test more complex palindrome scenarios"""
    assert sorted(find_shortest_palindrome_substrings("abaxyzzyxf")) == ['a', 'b', 'x', 'y', 'z']