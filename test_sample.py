import sample

def test_returns_num():
    assert sample.FizzBuzz(2) == 2


def test_when_divisible_by_three_return_fizz():
    assert sample.FizzBuzz(9) == "Fizz"

def test_when_divisible_by_five_return_buzz():
    assert sample.FizzBuzz(10) == "Buzz"

def test_when_divisible_by_five_and_three_return_fizzbuzz():
    assert sample.FizzBuzz(15) == "FizzBuzz"