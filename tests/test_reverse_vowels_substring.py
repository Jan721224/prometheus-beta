import pytest
from src.reverse_vowels_substring import reverse_vowels_substring

def test_reverse_vowels_basic():
    """Test basic vowel reversal in a substring"""
    assert reverse_vowels_substring("hello world", 0, 5) == "holle world"

def test_reverse_vowels_entire_string():
    """Test vowel reversal for the entire string"""
    assert reverse_vowels_substring("hello", 0, 5) == "holle"

def test_reverse_vowels_partial_string():
    """Test vowel reversal in part of the string"""
    assert reverse_vowels_substring("hello world", 2, 7) == "hello world"

def test_reverse_vowels_no_vowels():
    """Test string with no vowels"""
    assert reverse_vowels_substring("rhythm", 0, 6) == "rhythm"

def test_reverse_vowels_mixed_case():
    """Test with mixed case vowels"""
    assert reverse_vowels_substring("HeLLo WoRLd", 0, 6) == "HoLLe WoRLd"

def test_reverse_vowels_all_vowels():
    """Test string with only vowels"""
    assert reverse_vowels_substring("aeiou", 0, 5) == "uoiea"

def test_invalid_start_index():
    """Test invalid start index"""
    with pytest.raises(ValueError):
        reverse_vowels_substring("hello", -1, 5)

def test_invalid_end_index():
    """Test invalid end index"""
    with pytest.raises(ValueError):
        reverse_vowels_substring("hello", 0, 6)

def test_start_index_greater_than_end():
    """Test start index greater than end index"""
    with pytest.raises(ValueError):
        reverse_vowels_substring("hello", 3, 2)

def test_empty_string():
    """Test empty string"""
    assert reverse_vowels_substring("", 0, 0) == ""

def test_single_vowel_substring():
    """Test substring with a single vowel"""
    assert reverse_vowels_substring("hello world", 4, 5) == "hello world"