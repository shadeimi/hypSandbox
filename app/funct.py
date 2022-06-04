
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Number must be >= 0")

    total = 1
    for _ in range(1, num + 1):
        total *= _
    return total

