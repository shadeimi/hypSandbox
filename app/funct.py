
def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("Number must be >= 0")

    total = 1
    for _ in range(1, num + 1):
        total *= _
    return total


def palindrome(n: int):
    temp = n
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev*10+dig
        n = n//10
    return rev
