import pytest
from fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    "number, expected", 
    [(1, "1"), (2, "2"), (4, "4")]
)
def test_return_number(number, expected):
    result = fizzbuzz(number)
    assert result == expected

@pytest.mark.parametrize(
    "number", 
    [3, 6, 9, 12, 18]
)
def test_fizz(number):
    result = fizzbuzz(number)
    assert result == "fizz"
    
@pytest.mark.parametrize(
    "number", 
    [5, 10, 20, 25, 35]
)    
def test_buzz(number):
    result = fizzbuzz(number)
    assert result == "buzz"
    
@pytest.mark.parametrize(
    "number", 
    [15, 30, 45, 60, 75]
)
def test_fizzbuzz(number):
    result = fizzbuzz(number)
    assert result == "fizzbuzz"