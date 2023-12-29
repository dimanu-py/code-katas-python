import pytest
from leap_year import is_leap_year


@pytest.mark.parametrize("year", [1993, 1997, 2001, 2005, 2009])
def test_not_leap_year(year: int):
    """Asserts that a year is not leap because is not divisible by 4"""
    assert is_leap_year(year) == False

@pytest.mark.parametrize("year", [1996, 2004, 2008, 2012, 2016])
def test_leap_year_divisible_by_4(year: int):
    """Asserts that a year is leap when is divisible by 4"""
    assert is_leap_year(year) == True


@pytest.mark.parametrize("year", [1700, 1800, 1900, 2100, 2200])
def test_not_leap_year_divisible_by_100(year: int):
    """Asserts that a year is not leap when is divisible by 100 but not by 400"""
    assert is_leap_year(year) == False


@pytest.mark.parametrize("year", [1600, 2000, 2400, 2800, 3200])
def test_leap_year_divisible_by_100_and_400(year: int):
    """Asserts that a year is leap when is divisible by 4 and by 400"""
    assert is_leap_year(year) == True
