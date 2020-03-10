import sample

def test_returns_num():
    assert sample.FizzBuzz(2) == 2


def test_when_divisible_by_three_return_fizz():
    assert sample.FizzBuzz(9) == "Fizz"