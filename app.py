def factorial(n):
    """Returns the factorial of a number n."""
    if n == 0 or n == 1:
        return 1
    elif n < 0:
        raise ValueError("Input must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_positive(n):
    """Returns True if the number is positive, False otherwise."""
    return n > 0


def main():
    num = 5
    if is_positive(num):
        print(f"The factorial of {num} is {factorial(num)}")
    else:
        print("The number must be positive.")


if __name__ == '__main__':
    main()
