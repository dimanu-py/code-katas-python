import pytest
from leap_year import is_leap_year

def test_not_leap_year():
    """Asserts that a year is not leap"""
    assert is_leap_year(2015) == False


def test_leap_year_divisible_by_four():
    """Asserts that a year is leap"""
    assert is_leap_year(1996) == True
