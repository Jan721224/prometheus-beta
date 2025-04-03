def prime_factors(n):
    """
    Decompose a positive integer into its prime factors.
    
    Args:
        n (int): A positive integer to factorize.
    
    Returns:
        list: A list of prime factors in ascending order.
    
    Raises:
        ValueError: If the input is not a positive integer.
    """
    # Validate input
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    # List to store prime factors
    factors = []
    
    # Start with the smallest prime factor, 2
    divisor = 2
    
    # Continue factorizing while the number is greater than 1
    while divisor * divisor <= n:
        # If divisor divides n evenly
        if n % divisor == 0:
            # Add the divisor to factors
            factors.append(divisor)
            # Divide n by the divisor
            n //= divisor
        else:
            # If not divisible, move to next potential divisor
            divisor += 1
    
    # If n is greater than 1, it is a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors