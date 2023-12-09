from fizzbuzz import fizzbuzz


def test_return_1():
    numbers = fizzbuzz(1)
    assert numbers == "1"
    
def test_return_2():
    numbers = fizzbuzz(2)
    assert numbers == "2"
