import pytest
from app.funct import factorial

"""
    test cases are boring to write
    random, unbiased test examples are hard to come up with
    the test suite will quickly balloon in size so it will be hard to read and maintain going forward
    again, it's boring!
    it's hard to flesh out edge cases
"""

def test_factorial_less_than_0():
    with pytest.raises(ValueError):
        assert factorial(-1) == 1


def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(7) == 5040
    assert factorial(12) == 479001600
    assert factorial(44) == 2658271574788448768043625811014615890319638528000000000