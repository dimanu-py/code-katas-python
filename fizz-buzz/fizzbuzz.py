

def fizzbuzz(number: int) -> str:
    if number % 3 == 0:
        return "fizz"
    if number == 5:
        return "buzz"
    else:
        return str(number)
