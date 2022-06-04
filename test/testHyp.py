from app.funct import factorial
from hypothesis import given
from hypothesis.strategies import integers
from hypothesis import Verbosity, given, settings
from hypothesis import strategies as st


"""
    This test now asserts that the factorial of a number divided by the factorial of 
    that number minus one is the original number.
"""


@given(integers(min_value=1, max_value=3000))
@settings(verbosity=Verbosity.verbose)
def test_factorial(num: int):
    result = factorial(num) / factorial(num - 1)
    assert num == result

"""
    If a failure had been found, Hypothesis uses Shrinking to find the smallest fail case.
"""

@settings(verbosity=Verbosity.verbose)
@given(st.integers())
def test_shrinking(num: int):
    assert num >= -2
