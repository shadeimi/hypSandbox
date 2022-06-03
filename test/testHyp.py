from math import sqrt
from app.funct import factorial, palindrome
from hypothesis import given
from hypothesis.strategies import integers


@given(integers(min_value=1, max_value=3000))
def test_prod(num: int):
    assert sqrt(pow(num, 2)) == num


@given(integers(min_value=1, max_value=3000))
def test_factorial(num: int):
    result = factorial(num) / factorial(num - 1)
    assert num == result


@given(integers(min_value=1, max_value=3000))
def test_palindrome(num: int):
    assert palindrome(num) == num
