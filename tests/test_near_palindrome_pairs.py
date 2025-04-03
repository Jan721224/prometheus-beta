import pytest
from src.near_palindrome_pairs import find_near_palindrome_pairs

def test_find_near_palindrome_pairs_basic():
    """Test basic functionality of finding near-palindrome pairs."""
    result = find_near_palindrome_pairs(["racecar", "hello", "level", "world"])
    assert len(result) == 1
    assert sorted(result[0]) == sorted(["hello", "world"])

def test_find_near_palindrome_pairs_multiple():
    """Test finding multiple near-palindrome pairs."""
    result = find_near_palindrome_pairs(["abc", "cba", "abb", "baa"])
    assert len(result) == 2

def test_find_near_palindrome_pairs_no_pairs():
    """Test case with no near-palindrome pairs."""
    result = find_near_palindrome_pairs(["python", "code", "test"])
    assert len(result) == 0

def test_find_near_palindrome_pairs_empty_list():
    """Test with an empty input list."""
    result = find_near_palindrome_pairs([])
    assert len(result) == 0

def test_find_near_palindrome_pairs_single_char():
    """Test with single character strings."""
    result = find_near_palindrome_pairs(["a", "b", "c"])
    assert len(result) == 0

def test_find_near_palindrome_pairs_case_sensitive():
    """Ensure the function is case-sensitive."""
    result = find_near_palindrome_pairs(["Abc", "abc"])
    assert len(result) == 0

def test_different_length_strings():
    """Test with strings of different lengths."""
    result = find_near_palindrome_pairs(["hello", "world", "a", "ab"])
    # At least one pair should be possible
    assert len(result) > 0