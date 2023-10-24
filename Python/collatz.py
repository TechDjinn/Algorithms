def main():
    # Let's test collatz-function
    print(collatz(5))


def collatz(n):
    """
    Description:
        Function takes a positive integer,
        and returns the Collatz sequence for that integer.
        (e.g. collatz(5) = [5, 16, 8, 4, 2, 1])
    
    Arguments:
        n: Integer >= 1
    
    Returns:
        list: A list of the Collatz sequence for 'n'
    """
    assert isinstance(n, int) and n >= 1, "'n' must be a positivt integer."

    if n == 1:
        return [1]  # Base case
    elif n % 2 == 0:
        return [n] + collatz(int(n/2))
    else:
        return [n] + collatz(n*3 + 1)


if __name__ == "__main__":
    main()