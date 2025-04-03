import pytest
import random
from src.bubble_merge_sort import bubble_merge_sort

def test_basic_sorting():
    """Test basic sorting functionality"""
    input_list = [5, 2, 9, 1, 7, 6]
    expected = sorted(input_list)
    assert bubble_merge_sort(input_list) == expected

def test_already_sorted():
    """Test sorting an already sorted list"""
    input_list = [1, 2, 3, 4, 5]
    assert bubble_merge_sort(input_list) == input_list

def test_reverse_sorted():
    """Test sorting a reverse-sorted list"""
    input_list = [5, 4, 3, 2, 1]
    expected = sorted(input_list)
    assert bubble_merge_sort(input_list) == expected

def test_empty_list():
    """Test sorting an empty list"""
    assert bubble_merge_sort([]) == []

def test_single_element_list():
    """Test sorting a list with a single element"""
    input_list = [42]
    assert bubble_merge_sort(input_list) == input_list

def test_duplicate_elements():
    """Test sorting a list with duplicate elements"""
    input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    expected = sorted(input_list)
    assert bubble_merge_sort(input_list) == expected

def test_large_random_list():
    """Test sorting a large random list"""
    input_list = [random.randint(-1000, 1000) for _ in range(1000)]
    expected = sorted(input_list)
    assert bubble_merge_sort(input_list) == expected

def test_negative_numbers():
    """Test sorting a list with negative numbers"""
    input_list = [-5, -2, -9, -1, -7, -6]
    expected = sorted(input_list)
    assert bubble_merge_sort(input_list) == expected

def test_mixed_numbers():
    """Test sorting a list with mixed positive and negative numbers"""
    input_list = [-5, 2, 0, -3, 7, 1]
    expected = sorted(input_list)
    assert bubble_merge_sort(input_list) == expected

def test_invalid_input_type():
    """Test handling of invalid input type"""
    with pytest.raises(TypeError):
        bubble_merge_sort("not a list")
    with pytest.raises(TypeError):
        bubble_merge_sort(123)
    with pytest.raises(TypeError):
        bubble_merge_sort(None)