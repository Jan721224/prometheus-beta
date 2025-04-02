def fibonacci_sum(n):
    """
    Calculate the sum of the first n numbers in the Fibonacci sequence.

    Args:
        n (int): A positive integer representing the number of Fibonacci 
                 numbers to sum.

    Returns:
        int: The sum of the first n numbers in the Fibonacci sequence.

    Raises:
        ValueError: If n is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n < 1:
        raise ValueError("Input must be a positive integer")

    # Handle special cases
    if n == 1:
        return 0
    if n == 2:
        return 1

    # Initialize Fibonacci sequence and sum
    fib_sequence = [0, 1]
    total_sum = 1  # Start with 1 to account for first Fibonacci number

    # Generate Fibonacci sequence
    while len(fib_sequence) < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
        total_sum += next_fib

    return total_sum