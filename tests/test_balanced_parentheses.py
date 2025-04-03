import pytest
from src.balanced_parentheses import is_balanced_parentheses

def test_basic_balanced_parentheses():
    """Test basic balanced parentheses scenarios"""
    assert is_balanced_parentheses("()") == True
    assert is_balanced_parentheses("[]") == True
    assert is_balanced_parentheses("{}") == True

def test_multiple_balanced_parentheses():
    """Test multiple balanced parentheses scenarios"""
    assert is_balanced_parentheses("()[]{}") == True
    assert is_balanced_parentheses("([{}])") == True
    assert is_balanced_parentheses("{[()]}") == True

def test_nested_balanced_parentheses():
    """Test nested balanced parentheses"""
    assert is_balanced_parentheses("({[]})") == True
    assert is_balanced_parentheses("[({})]") == True

def test_unbalanced_parentheses():
    """Test unbalanced parentheses scenarios"""
    assert is_balanced_parentheses("(]") == False
    assert is_balanced_parentheses("([)]") == False
    assert is_balanced_parentheses("(()") == False
    assert is_balanced_parentheses(")") == False
    assert is_balanced_parentheses("(") == False

def test_empty_and_non_parenthesis_strings():
    """Test edge cases with empty and non-parenthesis strings"""
    assert is_balanced_parentheses("") == True
    assert is_balanced_parentheses("hello") == True
    assert is_balanced_parentheses("h(e)llo") == True
    assert is_balanced_parentheses("h(e[l]lo)") == True

def test_complex_unbalanced_scenarios():
    """Test more complex unbalanced scenarios"""
    assert is_balanced_parentheses("{[}]") == False
    assert is_balanced_parentheses("({[}])") == False
    assert is_balanced_parentheses("({{)}}") == False