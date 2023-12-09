from fizzbuzz import fizzbuzz


def test_return_number():
    numbers = fizzbuzz(1)
    assert numbers == "1"
    
    numbers = fizzbuzz(2)
    assert numbers == "2"

    numbers = fizzbuzz(2)
    assert numbers == "2"
    
    numbers = fizzbuzz(4)
    assert numbers == "4"
    
def test_fizz():
    numbers = fizzbuzz(3)
    assert numbers == "fizz"
    
    numbers = fizzbuzz(6)
    assert numbers == "fizz"
    
    numbers = fizzbuzz(9)
    assert numbers == "fizz"
    
    numbers = fizzbuzz(12)
    assert numbers == "fizz"