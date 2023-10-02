"""
Module of test for the function multiple from funcoes module
"""
from Multiple import multiple
import pytest

def testMultple5():
    """Test if the number is multiple of 5"""
    resultado = multiple(50)
    assert resultado == 'fizz'

def testMultiple7():
    """Test if the number is multiple of 7"""
    resultado = multiple(49)
    assert resultado == 'buzz'

def testMultple57():
    """Test if the number is multiple of 5 and 7 at the same time"""
    resultado = multiple(70)
    assert resultado == 'fizzbuzz'