import pytest
from leap_year import Year

def test_not_leap_year():
    """Asserts that a year is not leap"""
    year = Year()
    assert year.is_leap_year(2015) == False